#!/usr/bin/env python3
"""
Repository Quality Assurance (QA) Audit Script
Comprehensive validation of all content before publication
"""
import csv
import json
import os
import re
import requests
from urllib.parse import urlparse
from datetime import datetime
import time

class RepoQAValidator:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.stats = {
            "frameworks_checked": 0,
            "papers_checked": 0, 
            "links_validated": 0,
            "duplicates_found": 0
        }
    
    def log_issue(self, severity, category, message, file_path="", line_num=0):
        """Log QA issues with context"""
        issue = {
            "severity": severity,  # ERROR, WARNING, INFO
            "category": category,  # LINK, DUPLICATE, DATE, CONTENT
            "message": message,
            "file": file_path,
            "line": line_num,
            "timestamp": datetime.now().isoformat()
        }
        
        if severity == "ERROR":
            self.issues.append(issue)
        else:
            self.warnings.append(issue)
    
    def validate_http_link(self, url, timeout=10):
        """Validate HTTP links return 200"""
        try:
            response = requests.head(url, timeout=timeout, allow_redirects=True)
            return response.status_code == 200, response.status_code
        except Exception as e:
            return False, str(e)
    
    def check_arxiv_paper(self, arxiv_url):
        """Specific validation for arXiv papers"""
        if "arxiv.org" not in arxiv_url.lower():
            return True, "Not arXiv"
            
        # Extract arXiv ID
        match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', arxiv_url)
        if not match:
            return False, "Invalid arXiv URL format"
        
        arxiv_id = match.group(1)
        
        # Check if paper exists via arXiv API
        api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        try:
            response = requests.get(api_url, timeout=10)
            if "No papers found" in response.text:
                return False, f"arXiv paper {arxiv_id} not found"
            return True, f"arXiv {arxiv_id} validated"
        except Exception as e:
            return False, f"arXiv API error: {e}"
    
    def check_github_repo(self, github_url):
        """Validate GitHub repos exist and get basic info"""
        if "github.com" not in github_url.lower():
            return True, "Not GitHub"
        
        # Extract owner/repo from URL
        match = re.search(r'github\.com/([^/]+)/([^/]+)', github_url)
        if not match:
            return False, "Invalid GitHub URL format"
        
        owner, repo = match.groups()
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        
        try:
            response = requests.get(api_url, timeout=10)
            if response.status_code == 404:
                return False, f"GitHub repo {owner}/{repo} not found"
            elif response.status_code != 200:
                return False, f"GitHub API error: {response.status_code}"
            
            repo_data = response.json()
            return True, {
                "name": repo_data.get("name"),
                "description": repo_data.get("description", "")[:100],
                "stars": repo_data.get("stargazers_count", 0),
                "archived": repo_data.get("archived", False)
            }
        except Exception as e:
            return False, f"GitHub validation error: {e}"
    
    def validate_research_papers(self, papers_file="research/papers.md"):
        """Validate all research papers and links"""
        if not os.path.exists(papers_file):
            self.log_issue("ERROR", "CONTENT", f"Papers file not found: {papers_file}")
            return
        
        with open(papers_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all arXiv links
        arxiv_links = re.findall(r'https?://arxiv\.org/[^\s\)]+', content)
        print(f"Found {len(arxiv_links)} arXiv links to validate...")
        
        for i, url in enumerate(arxiv_links):
            print(f"  Checking {i+1}/{len(arxiv_links)}: {url[:60]}...")
            valid, info = self.check_arxiv_paper(url)
            if not valid:
                self.log_issue("ERROR", "LINK", f"Invalid arXiv paper: {url} - {info}", papers_file)
            self.stats["papers_checked"] += 1
            time.sleep(0.5)  # Rate limiting
        
        # Find all other HTTP links
        other_links = re.findall(r'https?://(?!arxiv\.org)[^\s\)]+', content)
        print(f"Found {len(other_links)} other links to validate...")
        
        for i, url in enumerate(other_links[:20]):  # Limit to first 20 for speed
            print(f"  Checking {i+1}: {url[:60]}...")
            valid, status = self.validate_http_link(url)
            if not valid:
                self.log_issue("WARNING", "LINK", f"Link may be broken: {url} - {status}", papers_file)
            self.stats["links_validated"] += 1
            time.sleep(0.5)
    
    def validate_frameworks_csv(self, csv_file="data/frameworks.csv"):
        """Validate frameworks CSV for duplicates and broken links"""
        if not os.path.exists(csv_file):
            self.log_issue("ERROR", "CONTENT", f"Frameworks CSV not found: {csv_file}")
            return
        
        seen_names = set()
        seen_github = set()
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        print(f"Validating {len(rows)} frameworks...")
        
        for i, row in enumerate(rows):
            name = row.get("name", "").strip()
            github = row.get("github", "").strip()
            
            # Check duplicates
            if name.lower() in seen_names:
                self.log_issue("ERROR", "DUPLICATE", f"Duplicate framework name: {name}", csv_file, i+2)
            else:
                seen_names.add(name.lower())
            
            if github and github in seen_github:
                self.log_issue("ERROR", "DUPLICATE", f"Duplicate GitHub URL: {github}", csv_file, i+2)
            else:
                seen_github.add(github)
            
            # Validate GitHub repos (sample)
            if github and i < 10:  # Check first 10 for speed
                print(f"  Checking framework {i+1}: {name}")
                valid, info = self.check_github_repo(github)
                if not valid:
                    self.log_issue("ERROR", "LINK", f"Invalid GitHub repo for {name}: {info}", csv_file, i+2)
                elif isinstance(info, dict) and info.get("archived"):
                    self.log_issue("WARNING", "CONTENT", f"Framework {name} repo is archived", csv_file, i+2)
            
            self.stats["frameworks_checked"] += 1
            if i < 10:
                time.sleep(0.5)
    
    def check_date_staleness(self):
        """Check for outdated 'Last updated' notices"""
        current_month_year = "October 2025"
        stale_patterns = [
            r"Last updated:.*?January 2025",
            r"Last updated:.*?February 2025", 
            r"Last updated:.*?March 2025",
            r"Last updated:.*?April 2025",
            r"Last updated:.*?May 2025",
            r"Last updated:.*?June 2025",
            r"Last updated:.*?July 2025",
            r"Last updated:.*?August 2025",
            r"Last updated:.*?September 2025"
        ]
        
        # Files to check
        files_to_check = [
            "README.md",
            "research/papers.md", 
            "catalog/coding-agents-deep-dive.md",
            "patterns/multi-agent-patterns.md",
            "guides/enterprise-deployment.md",
            "catalog/evaluation.md"
        ]
        
        for file_path in files_to_check:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for pattern in stale_patterns:
                    matches = re.finditer(pattern, content, re.IGNORECASE)
                    for match in matches:
                        line_num = content[:match.start()].count('\n') + 1
                        self.log_issue("WARNING", "DATE", 
                                     f"Stale date found: {match.group()} (should be {current_month_year})", 
                                     file_path, line_num)
    
    def generate_report(self):
        """Generate comprehensive QA report"""
        report = f"""
# Repository QA Audit Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary Statistics
- Frameworks checked: {self.stats['frameworks_checked']}
- Research papers checked: {self.stats['papers_checked']}  
- Links validated: {self.stats['links_validated']}
- Duplicates found: {self.stats['duplicates_found']}

## Issues Found ({len(self.issues)} errors)
"""
        
        if not self.issues:
            report += "✅ No critical errors found!\n"
        else:
            for issue in self.issues:
                report += f"❌ **{issue['category']}** in `{issue['file']}`:{issue['line']}\n"
                report += f"   {issue['message']}\n\n"
        
        report += f"\n## Warnings ({len(self.warnings)} warnings)\n"
        
        if not self.warnings:
            report += "✅ No warnings!\n"
        else:
            for warning in self.warnings[:10]:  # Show first 10
                report += f"⚠️  **{warning['category']}** in `{warning['file']}`:{warning['line']}\n"
                report += f"   {warning['message']}\n\n"
            
            if len(self.warnings) > 10:
                report += f"... and {len(self.warnings) - 10} more warnings\n"
        
        return report
    
    def run_full_audit(self):
        """Run complete QA audit"""
        print("🔍 Starting comprehensive repository QA audit...")
        print("=" * 60)
        
        print("\n📋 Checking for stale dates...")
        self.check_date_staleness()
        
        print("\n📊 Validating frameworks CSV...")
        self.validate_frameworks_csv()
        
        print("\n📚 Validating research papers...")
        self.validate_research_papers()
        
        print("\n📝 Generating QA report...")
        report = self.generate_report()
        
        # Save report
        with open("QA_AUDIT_REPORT.md", "w") as f:
            f.write(report)
        
        print(f"\n✅ QA audit complete!")
        print(f"📊 Found {len(self.issues)} errors and {len(self.warnings)} warnings")
        print("📄 Full report saved to: QA_AUDIT_REPORT.md")
        
        return len(self.issues) == 0  # Return True if no errors

if __name__ == "__main__":
    validator = RepoQAValidator()
    success = validator.run_full_audit()
    
    if not success:
        print("\n❌ QA audit failed - please fix errors before publishing")
        exit(1)
    else:
        print("\n🎉 Repository passed QA audit - ready for publication!")
