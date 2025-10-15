# 🧮 Interactive Comparison (New)

Explore frameworks by capability, maturity, language, deployment, and MCP support.

- UI: `compare/index.html`
- Data: `compare/catalog.json` (auto-generated)
- Generator: `scripts/generate_catalog_json.py`

To update the data locally:
```bash
python scripts/generate_catalog_json.py
```

Or simply push changes to `data/**` to auto-regenerate via CI.
