#!/usr/bin/env python3
"""
Framework Recommendation Engine

Scores frameworks based on user requirements and suggests best matches.
Reads from compare/catalog.json or generates it if missing.
"""
import json
import os
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
import argparse

@dataclass
class UserRequirements:
    use_case: str  # "research", "coding", "multi_agent", "enterprise", "prototype"
    experience: str  # "beginner", "intermediate", "advanced"
    deployment: str  # "local", "cloud", "hybrid"
    budget: str  # "low", "medium", "high"
    timeline: str  # "hours", "days", "weeks"
    team_size: int
    programming_language: str  # "python", "typescript", "any"
    requires_mcp: bool
    requires_computer_use: bool
    enterprise_features: bool

class FrameworkRecommendationEngine:
    def __init__(self, catalog_path: str = "compare/catalog.json"):
        self.catalog = self.load_catalog(catalog_path)
        self.frameworks = self.catalog.get("frameworks", [])
        
        # Scoring weights
        self.weights = {
            "use_case_match": 0.25,
            "experience_fit": 0.20,
            "deployment_match": 0.15,
            "maturity": 0.15,
            "community": 0.10,
            "requirements": 0.10,
            "maintenance": 0.05
        }
        
    def load_catalog(self, path: str) -> Dict:
        if not os.path.exists(path):
            # Generate catalog if missing
            os.system("python scripts/generate_catalog_json.py")
        
        with open(path, 'r') as f:
            return json.load(f)
    
    def score_framework(self, framework: Dict, requirements: UserRequirements) -> Tuple[float, Dict[str, float]]:
        """Score a framework against user requirements"""
        scores = {}
        
        # Use case matching
        scores["use_case_match"] = self._score_use_case(
            framework, requirements.use_case
        )
        
        # Experience level fit
        scores["experience_fit"] = self._score_experience(
            framework, requirements.experience
        )
        
        # Deployment compatibility
        scores["deployment_match"] = self._score_deployment(
            framework, requirements.deployment
        )
        
        # Maturity assessment
        scores["maturity"] = self._score_maturity(
            framework, requirements.timeline
        )
        
        # Community & popularity
        scores["community"] = self._score_community(framework)
        
        # Specific requirements
        scores["requirements"] = self._score_requirements(
            framework, requirements
        )
        
        # Maintenance status
        scores["maintenance"] = self._score_maintenance(framework)
        
        # Calculate weighted total
        total_score = sum(
            scores[key] * self.weights[key] 
            for key in scores
        )
        
        return total_score, scores
    
    def _score_use_case(self, framework: Dict, use_case: str) -> float:
        category = framework.get("category", "").lower()
        tags = framework.get("tags", "").lower()
        
        use_case_mapping = {
            "research": ["research", "survey", "analysis"],
            "coding": ["coding", "software", "programming"],
            "multi_agent": ["multi-agent", "collaboration", "team"],
            "enterprise": ["enterprise", "production", "business"],
            "prototype": ["experimental", "prototype", "lightweight"]
        }
        
        keywords = use_case_mapping.get(use_case, [])
        matches = sum(1 for kw in keywords if kw in category or kw in tags)
        return min(matches / len(keywords), 1.0) if keywords else 0.5
    
    def _score_experience(self, framework: Dict, experience: str) -> float:
        maturity = framework.get("maturity", "").lower()
        stars = self._parse_stars(framework.get("stars", "0"))
        
        if experience == "beginner":
            # Prefer mature, well-documented frameworks
            if maturity == "production" and stars > 20000:
                return 0.9
            elif maturity in ["production", "beta"] and stars > 10000:
                return 0.7
            else:
                return 0.3
        elif experience == "intermediate":
            # Balance of features and ease of use
            if maturity in ["production", "beta"] and stars > 5000:
                return 0.8
            else:
                return 0.5
        else:  # advanced
            # All frameworks suitable for advanced users
            return 0.8 if maturity != "broken" else 0.2
    
    def _score_deployment(self, framework: Dict, deployment: str) -> float:
        fw_deployment = framework.get("deployment", "").lower()
        
        if deployment == "local":
            return 1.0 if "local" in fw_deployment else 0.3
        elif deployment == "cloud":
            return 1.0 if "cloud" in fw_deployment else 0.4
        else:  # hybrid
            return 1.0 if "hybrid" in fw_deployment or "/" in fw_deployment else 0.6
    
    def _score_maturity(self, framework: Dict, timeline: str) -> float:
        maturity = framework.get("maturity", "").lower()
        
        maturity_scores = {
            "production": {"hours": 0.9, "days": 1.0, "weeks": 1.0},
            "beta": {"hours": 0.6, "days": 0.8, "weeks": 0.9},
            "experimental": {"hours": 0.2, "days": 0.5, "weeks": 0.7}
        }
        
        return maturity_scores.get(maturity, {}).get(timeline, 0.5)
    
    def _score_community(self, framework: Dict) -> float:
        stars = self._parse_stars(framework.get("stars", "0"))
        
        if stars >= 50000:
            return 1.0
        elif stars >= 20000:
            return 0.8
        elif stars >= 5000:
            return 0.6
        elif stars >= 1000:
            return 0.4
        else:
            return 0.2
    
    def _score_requirements(self, framework: Dict, requirements: UserRequirements) -> float:
        score = 1.0
        tags = framework.get("tags", "").lower()
        
        # MCP requirement
        if requirements.requires_mcp:
            if "mcp" not in tags:
                score -= 0.4
        
        # Computer use requirement
        if requirements.requires_computer_use:
            if "computer" not in tags and "gui" not in tags:
                score -= 0.4
        
        # Enterprise features
        if requirements.enterprise_features:
            if "enterprise" not in tags and "production" not in framework.get("maturity", "").lower():
                score -= 0.3
        
        # Programming language preference
        if requirements.programming_language != "any":
            lang = framework.get("language", "").lower()
            if requirements.programming_language.lower() not in lang:
                score -= 0.2
        
        return max(score, 0.0)
    
    def _score_maintenance(self, framework: Dict) -> float:
        # Simple heuristic based on recent activity
        # In real implementation, would parse last_commit date
        return 0.8  # Placeholder
    
    def _parse_stars(self, stars_str: str) -> int:
        """Parse stars string to integer"""
        try:
            stars_str = str(stars_str).lower().replace(",", "")
            if "k" in stars_str:
                return int(float(stars_str.replace("k", "")) * 1000)
            else:
                return int(stars_str)
        except:
            return 0
    
    def recommend(self, requirements: UserRequirements, top_k: int = 5) -> List[Dict]:
        """Get top recommendations based on requirements"""
        scored_frameworks = []
        
        for framework in self.frameworks:
            total_score, detailed_scores = self.score_framework(framework, requirements)
            
            scored_frameworks.append({
                "framework": framework,
                "total_score": total_score,
                "detailed_scores": detailed_scores,
                "recommendation_reason": self._generate_reason(framework, requirements, detailed_scores)
            })
        
        # Sort by total score
        scored_frameworks.sort(key=lambda x: x["total_score"], reverse=True)
        
        return scored_frameworks[:top_k]
    
    def _generate_reason(self, framework: Dict, requirements: UserRequirements, scores: Dict[str, float]) -> str:
        """Generate human-readable recommendation reason"""
        name = framework.get("name", "Unknown")
        top_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:2]
        
        reasons = []
        for score_type, score_value in top_scores:
            if score_value > 0.7:
                if score_type == "use_case_match":
                    reasons.append(f"excellent fit for {requirements.use_case} use cases")
                elif score_type == "experience_fit":
                    reasons.append(f"well-suited for {requirements.experience} developers")
                elif score_type == "maturity":
                    reasons.append("production-ready and stable")
                elif score_type == "community":
                    reasons.append("strong community support")
        
        if not reasons:
            reasons.append("solid general-purpose option")
        
        return f"{name} is recommended because it offers " + " and ".join(reasons) + "."

def main():
    parser = argparse.ArgumentParser(description="Get AI agent framework recommendations")
    parser.add_argument("--use_case", choices=["research", "coding", "multi_agent", "enterprise", "prototype"], default="prototype")
    parser.add_argument("--experience", choices=["beginner", "intermediate", "advanced"], default="intermediate")
    parser.add_argument("--deployment", choices=["local", "cloud", "hybrid"], default="local")
    parser.add_argument("--budget", choices=["low", "medium", "high"], default="medium")
    parser.add_argument("--timeline", choices=["hours", "days", "weeks"], default="days")
    parser.add_argument("--language", default="python")
    parser.add_argument("--mcp", action="store_true", help="Requires MCP support")
    parser.add_argument("--computer_use", action="store_true", help="Requires computer use capabilities")
    parser.add_argument("--enterprise", action="store_true", help="Requires enterprise features")
    parser.add_argument("--top_k", type=int, default=5, help="Number of recommendations")
    
    args = parser.parse_args()
    
    requirements = UserRequirements(
        use_case=args.use_case,
        experience=args.experience,
        deployment=args.deployment,
        budget=args.budget,
        timeline=args.timeline,
        team_size=1,  # Could be added as argument
        programming_language=args.language,
        requires_mcp=args.mcp,
        requires_computer_use=args.computer_use,
        enterprise_features=args.enterprise
    )
    
    engine = FrameworkRecommendationEngine()
    recommendations = engine.recommend(requirements, args.top_k)
    
    print(f"\n🎯 Top {len(recommendations)} Recommendations for {args.use_case} use case:\n")
    
    for i, rec in enumerate(recommendations, 1):
        fw = rec["framework"]
        score = rec["total_score"]
        reason = rec["recommendation_reason"]
        
        print(f"{i}. **{fw.get('name', 'Unknown')}** (Score: {score:.2f})")
        print(f"   GitHub: {fw.get('github', 'N/A')}")
        print(f"   Stars: {fw.get('stars', 'N/A')} | Maturity: {fw.get('maturity', 'N/A')}")
        print(f"   Reason: {reason}")
        print()
    
    # Show detailed scores for top recommendation
    if recommendations:
        print("\n📊 Detailed scoring for top recommendation:")
        top_rec = recommendations[0]
        detailed = top_rec["detailed_scores"]
        
        for score_type, score_value in sorted(detailed.items(), key=lambda x: x[1], reverse=True):
            print(f"   {score_type.replace('_', ' ').title()}: {score_value:.2f}")

if __name__ == "__main__":
    main()
