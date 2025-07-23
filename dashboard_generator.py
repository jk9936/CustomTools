#!/usr/bin/env python3
"""
Dashboard Generator Service
A Python console application that takes JSON data and generates HTML dashboards.
"""

import json
import argparse
import sys
import os
from datetime import datetime
from pathlib import Path
from jinja2 import Template
import webbrowser

class DashboardGenerator:
    def __init__(self):
        self.template_dir = Path(__file__).parent / "templates"
        self.output_dir = Path(__file__).parent / "output"
        self.ensure_directories()
    
    def ensure_directories(self):
        """Create necessary directories if they don't exist"""
        self.template_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
    
    def load_json_data(self, file_path):
        """Load JSON data from file or stdin"""
        try:
            if file_path == '-':
                # Read from stdin
                data = json.load(sys.stdin)
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            return data
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing JSON: {e}")
            sys.exit(1)
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
            sys.exit(1)
    
    def process_data(self, raw_data):
        """Process raw JSON data into dashboard-ready format"""
        processed = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'title': raw_data.get('title', 'Data Dashboard'),
            'description': raw_data.get('description', 'Generated dashboard from JSON data'),
            'metrics': self._process_metrics(raw_data.get('metrics', [])),
            'charts': self._process_charts(raw_data.get('charts', [])),
            'tables': self._process_tables(raw_data.get('tables', [])),
            'cards': self._process_cards(raw_data.get('cards', [])),
            'alerts': raw_data.get('alerts', [])
        }
        return processed
    
    def _process_metrics(self, metrics):
        """Process metrics data"""
        processed_metrics = []
        for metric in metrics:
            processed_metrics.append({
                'name': metric.get('name', 'Metric'),
                'value': metric.get('value', 0),
                'unit': metric.get('unit', ''),
                'change': metric.get('change', None),
                'trend': metric.get('trend', 'neutral'),  # up, down, neutral
                'color': metric.get('color', '#3498db')
            })
        return processed_metrics
    
    def _process_charts(self, charts):
        """Process charts data"""
        processed_charts = []
        for chart in charts:
            processed_charts.append({
                'id': f"chart_{len(processed_charts) + 1}",
                'title': chart.get('title', 'Chart'),
                'type': chart.get('type', 'line'),  # line, bar, pie, doughnut
                'labels': chart.get('labels', []),
                'datasets': chart.get('datasets', []),
                'width': chart.get('width', '100%'),
                'height': chart.get('height', '400px')
            })
        return processed_charts
    
    def _process_tables(self, tables):
        """Process table data"""
        processed_tables = []
        for table in tables:
            processed_tables.append({
                'title': table.get('title', 'Data Table'),
                'headers': table.get('headers', []),
                'rows': table.get('rows', []),
                'searchable': table.get('searchable', True),
                'sortable': table.get('sortable', True)
            })
        return processed_tables
    
    def _process_cards(self, cards):
        """Process card data"""
        processed_cards = []
        for card in cards:
            processed_cards.append({
                'title': card.get('title', 'Card'),
                'content': card.get('content', ''),
                'type': card.get('type', 'info'),  # info, success, warning, error
                'icon': card.get('icon', '📊')
            })
        return processed_cards
    
    def get_dashboard_template(self):
        """Get the HTML template for the dashboard"""
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            border-radius: 15px;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            opacity: 0.9;
            font-size: 1.1em;
        }
        
        .timestamp {
            text-align: right;
            color: #7f8c8d;
            font-size: 0.9em;
            margin-bottom: 20px;
        }
        
        .grid {
            display: grid;
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .grid-2 { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
        .grid-3 { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
        .grid-4 { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.15);
        }
        
        .metric-card {
            text-align: center;
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white;
            position: relative;
            overflow: hidden;
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: shimmer 3s infinite;
        }
        
        @keyframes shimmer {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .metric-value {
            font-size: 2.5em;
            font-weight: bold;
            margin: 10px 0;
            position: relative;
            z-index: 1;
        }
        
        .metric-name {
            font-size: 1.2em;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        
        .metric-change {
            font-size: 0.9em;
            margin-top: 10px;
            position: relative;
            z-index: 1;
        }
        
        .trend-up { color: #2ecc71; }
        .trend-down { color: #e74c3c; }
        .trend-neutral { color: #f39c12; }
        
        .chart-container {
            position: relative;
            height: 400px;
            margin: 20px 0;
        }
        
        .chart-title {
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 15px;
            color: #2c3e50;
            text-align: center;
        }
        
        .table-container {
            overflow-x: auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .data-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }
        
        .data-table th {
            background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            position: sticky;
            top: 0;
        }
        
        .data-table td {
            padding: 12px 15px;
            border-bottom: 1px solid #ecf0f1;
            transition: background-color 0.3s ease;
        }
        
        .data-table tr:hover td {
            background-color: #f8f9fa;
        }
        
        .data-table tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        .search-box {
            width: 100%;
            padding: 10px 15px;
            border: 2px solid #bdc3c7;
            border-radius: 25px;
            font-size: 1em;
            margin-bottom: 20px;
            transition: border-color 0.3s ease;
        }
        
        .search-box:focus {
            outline: none;
            border-color: #3498db;
        }
        
        .alert {
            padding: 15px 20px;
            border-radius: 10px;
            margin: 10px 0;
            font-weight: 500;
        }
        
        .alert-info { background: #d4edda; color: #155724; border-left: 4px solid #28a745; }
        .alert-warning { background: #fff3cd; color: #856404; border-left: 4px solid #ffc107; }
        .alert-error { background: #f8d7da; color: #721c24; border-left: 4px solid #dc3545; }
        .alert-success { background: #d1ecf1; color: #0c5460; border-left: 4px solid #17a2b8; }
        
        .section-title {
            font-size: 1.8em;
            color: #2c3e50;
            margin: 30px 0 20px 0;
            padding-bottom: 10px;
            border-bottom: 3px solid #3498db;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
            color: #7f8c8d;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @media (max-width: 768px) {
            .container { padding: 15px; }
            .header h1 { font-size: 2em; }
            .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
            .metric-value { font-size: 2em; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{{ title }}</h1>
            <p>{{ description }}</p>
        </div>
        
        <div class="timestamp">
            <i class="fas fa-clock"></i> Generated on: {{ timestamp }}
        </div>
        
        {% if alerts %}
        <div class="alerts-section">
            {% for alert in alerts %}
            <div class="alert alert-{{ alert.type }}">
                <i class="fas fa-{{ alert.icon | default('info-circle') }}"></i>
                {{ alert.message }}
            </div>
            {% endfor %}
        </div>
        {% endif %}
        
        {% if metrics %}
        <h2 class="section-title">
            <i class="fas fa-chart-line"></i> Key Metrics
        </h2>
        <div class="grid grid-4">
            {% for metric in metrics %}
            <div class="card metric-card" style="background: linear-gradient(135deg, {{ metric.color }} 0%, {{ metric.color }}dd 100%);">
                <div class="metric-name">{{ metric.name }}</div>
                <div class="metric-value">{{ metric.value }}{{ metric.unit }}</div>
                {% if metric.change %}
                <div class="metric-change trend-{{ metric.trend }}">
                    <i class="fas fa-arrow-{{ 'up' if metric.trend == 'up' else 'down' if metric.trend == 'down' else 'right' }}"></i>
                    {{ metric.change }}
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        {% endif %}
        
        {% if charts %}
        <h2 class="section-title">
            <i class="fas fa-chart-bar"></i> Charts
        </h2>
        <div class="grid grid-2">
            {% for chart in charts %}
            <div class="card">
                <div class="chart-title">{{ chart.title }}</div>
                <div class="chart-container">
                    <canvas id="{{ chart.id }}"></canvas>
                </div>
            </div>
            {% endfor %}
        </div>
        {% endif %}
        
        {% if cards %}
        <h2 class="section-title">
            <i class="fas fa-th-large"></i> Information Cards
        </h2>
        <div class="grid grid-3">
            {% for card in cards %}
            <div class="card">
                <h3>{{ card.icon }} {{ card.title }}</h3>
                <div>{{ card.content }}</div>
            </div>
            {% endfor %}
        </div>
        {% endif %}
        
        {% if tables %}
        <h2 class="section-title">
            <i class="fas fa-table"></i> Data Tables
        </h2>
        {% for table in tables %}
        <div class="card">
            <h3>{{ table.title }}</h3>
            {% if table.searchable %}
            <input type="text" class="search-box" placeholder="Search in {{ table.title }}..." 
                   onkeyup="searchTable(this, 'table{{ loop.index }}')">
            {% endif %}
            <div class="table-container">
                <table class="data-table" id="table{{ loop.index }}">
                    <thead>
                        <tr>
                            {% for header in table.headers %}
                            <th {% if table.sortable %}onclick="sortTable({{ loop.index0 }}, 'table{{ loop.index }}')" style="cursor: pointer;"{% endif %}>
                                {{ header }}
                                {% if table.sortable %}<i class="fas fa-sort"></i>{% endif %}
                            </th>
                            {% endfor %}
                        </tr>
                    </thead>
                    <tbody>
                        {% for row in table.rows %}
                        <tr>
                            {% for cell in row %}
                            <td>{{ cell }}</td>
                            {% endfor %}
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        {% endfor %}
        {% endif %}
        
        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p>Loading dashboard...</p>
        </div>
    </div>
    
    <script>
        // Initialize charts
        {% for chart in charts %}
        const ctx{{ loop.index }} = document.getElementById('{{ chart.id }}').getContext('2d');
        new Chart(ctx{{ loop.index }}, {
            type: '{{ chart.type }}',
            data: {
                labels: {{ chart.labels | tojson }},
                datasets: {{ chart.datasets | tojson }}
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    tooltip: {
                        mode: 'index',
                        intersect: false,
                    }
                },
                scales: {
                    {% if chart.type in ['line', 'bar'] %}
                    y: {
                        beginAtZero: true
                    }
                    {% endif %}
                }
            }
        });
        {% endfor %}
        
        // Search functionality
        function searchTable(input, tableId) {
            const filter = input.value.toLowerCase();
            const table = document.getElementById(tableId);
            const rows = table.getElementsByTagName('tr');
            
            for (let i = 1; i < rows.length; i++) {
                const cells = rows[i].getElementsByTagName('td');
                let found = false;
                
                for (let j = 0; j < cells.length; j++) {
                    if (cells[j].textContent.toLowerCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }
                
                rows[i].style.display = found ? '' : 'none';
            }
        }
        
        // Sort functionality
        function sortTable(columnIndex, tableId) {
            const table = document.getElementById(tableId);
            const tbody = table.getElementsByTagName('tbody')[0];
            const rows = Array.from(tbody.getElementsByTagName('tr'));
            
            rows.sort((a, b) => {
                const aText = a.getElementsByTagName('td')[columnIndex].textContent.trim();
                const bText = b.getElementsByTagName('td')[columnIndex].textContent.trim();
                
                // Try to parse as numbers
                const aNum = parseFloat(aText);
                const bNum = parseFloat(bText);
                
                if (!isNaN(aNum) && !isNaN(bNum)) {
                    return aNum - bNum;
                }
                
                return aText.localeCompare(bText);
            });
            
            rows.forEach(row => tbody.appendChild(row));
        }
        
        // Loading animation
        document.addEventListener('DOMContentLoaded', function() {
            const loading = document.getElementById('loading');
            loading.style.display = 'block';
            
            setTimeout(() => {
                loading.style.display = 'none';
            }, 1000);
        });
        
        console.log('📊 Dashboard loaded successfully!');
    </script>
</body>
</html>
        """
    
    def generate_dashboard(self, data, output_file):
        """Generate HTML dashboard from processed data"""
        template = Template(self.get_dashboard_template())
        html_content = template.render(**data)
        
        output_path = self.output_dir / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return output_path
    
    def create_sample_data(self):
        """Create sample JSON data for testing"""
        sample_data = {
            "title": "Sales Dashboard",
            "description": "Monthly sales performance and analytics",
            "metrics": [
                {
                    "name": "Total Revenue",
                    "value": "₹2,45,000",
                    "change": "+15%",
                    "trend": "up",
                    "color": "#2ecc71"
                },
                {
                    "name": "New Customers",
                    "value": "1,247",
                    "change": "+8%",
                    "trend": "up",
                    "color": "#3498db"
                },
                {
                    "name": "Orders",
                    "value": "856",
                    "change": "-3%",
                    "trend": "down",
                    "color": "#e74c3c"
                },
                {
                    "name": "Conversion Rate",
                    "value": "3.2%",
                    "change": "+0.5%",
                    "trend": "up",
                    "color": "#f39c12"
                }
            ],
            "charts": [
                {
                    "title": "Monthly Revenue",
                    "type": "line",
                    "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                    "datasets": [{
                        "label": "Revenue (₹)",
                        "data": [180000, 190000, 210000, 220000, 235000, 245000],
                        "borderColor": "#3498db",
                        "backgroundColor": "rgba(52, 152, 219, 0.1)",
                        "fill": True
                    }]
                },
                {
                    "title": "Product Categories",
                    "type": "pie",
                    "labels": ["Electronics", "Clothing", "Books", "Home", "Sports"],
                    "datasets": [{
                        "data": [35, 25, 15, 15, 10],
                        "backgroundColor": [
                            "#3498db", "#2ecc71", "#f39c12", "#e74c3c", "#9b59b6"
                        ]
                    }]
                }
            ],
            "tables": [
                {
                    "title": "Top Products",
                    "headers": ["Product", "Sales", "Revenue", "Growth"],
                    "rows": [
                        ["iPhone 15", "245", "₹2,45,000", "+15%"],
                        ["MacBook Pro", "132", "₹1,98,000", "+8%"],
                        ["iPad Air", "89", "₹89,000", "+12%"],
                        ["AirPods Pro", "156", "₹46,800", "+25%"],
                        ["Apple Watch", "78", "₹39,000", "+5%"]
                    ],
                    "searchable": True,
                    "sortable": True
                }
            ],
            "cards": [
                {
                    "title": "System Status",
                    "content": "All systems operational. Last backup: 2 hours ago",
                    "type": "success",
                    "icon": "✅"
                },
                {
                    "title": "Pending Tasks",
                    "content": "5 pending orders need attention",
                    "type": "warning",
                    "icon": "⚠️"
                }
            ],
            "alerts": [
                {
                    "type": "success",
                    "message": "Monthly target achieved! 🎉",
                    "icon": "check-circle"
                },
                {
                    "type": "warning",
                    "message": "Low inventory alert for 3 products",
                    "icon": "exclamation-triangle"
                }
            ]
        }
        
        sample_path = self.output_dir / "sample_data.json"
        with open(sample_path, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, indent=2, ensure_ascii=False)
        
        return sample_path

def main():
    parser = argparse.ArgumentParser(
        description='Dashboard Generator - Convert JSON data to HTML dashboards',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python dashboard_generator.py -i data.json -o dashboard.html
  python dashboard_generator.py -i data.json -o dashboard.html --open
  python dashboard_generator.py --sample
  cat data.json | python dashboard_generator.py -i - -o dashboard.html
        """
    )
    
    parser.add_argument(
        '-i', '--input',
        help='Input JSON file path (use "-" for stdin)',
        default=None
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output HTML file name (default: dashboard.html)',
        default='dashboard.html'
    )
    
    parser.add_argument(
        '--open',
        action='store_true',
        help='Open the generated dashboard in browser'
    )
    
    parser.add_argument(
        '--sample',
        action='store_true',
        help='Generate sample data file'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    generator = DashboardGenerator()
    
    if args.sample:
        sample_path = generator.create_sample_data()
        print(f"✅ Sample data created: {sample_path}")
        print(f"💡 Try: python dashboard_generator.py -i {sample_path} -o sample_dashboard.html --open")
        return
    
    if not args.input:
        print("❌ Error: Input file required. Use -i option or --sample to generate sample data.")
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.verbose:
            print(f"📖 Loading data from: {args.input}")
        
        raw_data = generator.load_json_data(args.input)
        
        if args.verbose:
            print("🔄 Processing data...")
        
        processed_data = generator.process_data(raw_data)
        
        if args.verbose:
            print(f"🎨 Generating dashboard: {args.output}")
        
        output_path = generator.generate_dashboard(processed_data, args.output)
        
        print(f"✅ Dashboard generated successfully!")
        print(f"📄 Output file: {output_path}")
        print(f"📊 Contains: {len(processed_data['metrics'])} metrics, {len(processed_data['charts'])} charts, {len(processed_data['tables'])} tables")
        
        if args.open:
            webbrowser.open(f"file://{output_path.absolute()}")
            print("🌐 Dashboard opened in browser")
            
    except Exception as e:
        print(f"❌ Error generating dashboard: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 