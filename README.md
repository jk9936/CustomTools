# 🚀 Dashboard Generator Service

Welcome! This project lets you quickly turn your JSON data into beautiful, interactive HTML dashboards with just a single command. Whether you’re a developer, analyst, or just want to visualize data, you’ll be up and running in minutes.

---

## 🌟 Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd DashboardService
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Generate a sample dashboard:**
   ```bash
   python dashboard_generator.py --sample
   python dashboard_generator.py -i output/sample_data.json -o sample_dashboard.html --open
   ```

---

## 📦 Features
- Interactive charts (line, bar, pie, doughnut)
- Colorful metric cards with trends
- Searchable, sortable tables
- Modern, responsive UI
- Fast, easy command-line usage

---

## 🛠️ Usage

### Basic Commands
```bash
# Generate dashboard from JSON file
python dashboard_generator.py -i data.json -o dashboard.html

# Generate and open in browser
python dashboard_generator.py -i data.json -o dashboard.html --open

# Generate sample data
python dashboard_generator.py --sample

# Read from stdin
cat data.json | python dashboard_generator.py -i - -o dashboard.html
```

### Command Line Options
- `-i, --input`: Input JSON file path (use "-" for stdin)
- `-o, --output`: Output HTML file name (default: dashboard.html)
- `--open`: Open the generated dashboard in browser
- `--sample`: Generate sample data file
- `--verbose`: Enable verbose output

---

## 📝 JSON Data Format

Here’s a minimal example:
```json
{
  "title": "My Dashboard",
  "metrics": [
    { "name": "Total Revenue", "value": "₹2,45,000", "trend": "up", "color": "#2ecc71" }
  ],
  "charts": [
    { "title": "Monthly Revenue", "type": "line", "labels": ["Jan", "Feb"], "datasets": [{ "label": "Revenue", "data": [100, 200] }] }
  ]
}
```
See the sample data (`output/sample_data.json`) for a full example.

---

## 🧩 Project Structure

```
DashboardService/
│
├── tools/                  # All tool modules (add new tools here)
│   ├── __init__.py
│   └── dashboard.py        # Dashboard generator logic
│
├── tests/                  # All test files
│   ├── __init__.py
│   └── test_dashboard.py
│
├── templates/              # HTML templates
├── output/                 # Generated output files
├── sample_input.json       # Example input
├── example_usage.py        # Example usage script
├── requirements.txt        # Python dependencies
├── FEATURES.md             # Feature list
├── README.md               # Project documentation
└── dashboard_generator.py  # Backward-compatible stub (uses tools/dashboard.py)
```

---

## 🛠️ Adding New Tools
- Add your new tool as a Python file in the `tools/` directory (e.g., `tools/my_new_tool.py`).
- Write your tool logic as a class or functions.
- Add tests for your tool in the `tests/` directory.
- Import and use your tool in a new or existing entry point script as needed.

---

## 🧪 Running Tests

To run the included tests:
```bash
python tests/test_dashboard.py
```

---

## 🤝 Contributing
- Found a bug or have an idea? Open an issue or pull request!
- All contributions are welcome.

---

## ❓ Getting Help
- **Questions?** Open an issue on GitHub.
- **Need a feature?** Suggest it via an issue or discussion.
- **Stuck?** Check the sample data and usage examples above.

---

## 📄 License
MIT License. See [LICENSE](LICENSE) for details. 