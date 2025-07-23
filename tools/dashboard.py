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
        self.template_dir = Path(__file__).parent.parent / "templates"
        self.output_dir = Path(__file__).parent.parent / "output"
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
        processed_cards = []
        for card in cards:
            processed_cards.append(card)
        return processed_cards
    
    def get_dashboard_template(self):
        # ... existing code ...
        pass
    
    def generate_dashboard(self, data, output_file):
        # ... existing code ...
        pass
    
    def create_sample_data(self):
        # ... existing code ...
        pass

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