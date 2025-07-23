#!/usr/bin/env python3
"""
Example Usage of Dashboard Generator
Shows how to use the dashboard generator programmatically
"""

import json
from dashboard_generator import DashboardGenerator

def create_custom_dashboard():
    """Example of creating a custom dashboard"""
    
    # Create your data
    custom_data = {
        "title": "My Custom Dashboard",
        "description": "A personalized dashboard example",
        "metrics": [
            {
                "name": "Active Users",
                "value": "12,345",
                "change": "+5%",
                "trend": "up",
                "color": "#3498db"
            },
            {
                "name": "Revenue",
                "value": "$98,765",
                "change": "+12%",
                "trend": "up",
                "color": "#2ecc71"
            },
            {
                "name": "Conversion Rate",
                "value": "3.2%",
                "change": "-0.1%",
                "trend": "down",
                "color": "#e74c3c"
            }
        ],
        "charts": [
            {
                "title": "Weekly Performance",
                "type": "line",
                "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                "datasets": [{
                    "label": "Performance Score",
                    "data": [65, 70, 80, 75, 85, 90, 88],
                    "borderColor": "#3498db",
                    "backgroundColor": "rgba(52, 152, 219, 0.2)",
                    "fill": True
                }]
            },
            {
                "title": "Category Breakdown",
                "type": "pie",
                "labels": ["Category A", "Category B", "Category C", "Category D"],
                "datasets": [{
                    "data": [30, 25, 25, 20],
                    "backgroundColor": ["#3498db", "#2ecc71", "#f39c12", "#e74c3c"]
                }]
            }
        ],
        "tables": [
            {
                "title": "Recent Activities",
                "headers": ["Time", "User", "Action", "Status"],
                "rows": [
                    ["10:30 AM", "John Doe", "Login", "Success"],
                    ["10:25 AM", "Jane Smith", "Purchase", "Completed"],
                    ["10:20 AM", "Bob Johnson", "Registration", "Pending"],
                    ["10:15 AM", "Alice Brown", "Update Profile", "Success"]
                ],
                "searchable": True,
                "sortable": True
            }
        ],
        "cards": [
            {
                "title": "System Health",
                "content": "All systems operational. CPU: 45%, Memory: 62%",
                "type": "success",
                "icon": "💚"
            },
            {
                "title": "Pending Tasks",
                "content": "You have 7 pending tasks that need attention",
                "type": "warning",
                "icon": "⚠️"
            }
        ],
        "alerts": [
            {
                "type": "info",
                "message": "📈 Performance improved by 15% this week",
                "icon": "info-circle"
            }
        ]
    }
    
    # Initialize generator
    generator = DashboardGenerator()
    
    # Process and generate dashboard
    processed_data = generator.process_data(custom_data)
    output_path = generator.generate_dashboard(processed_data, "custom_dashboard.html")
    
    print(f"✅ Custom dashboard created: {output_path}")
    return output_path

def create_minimal_dashboard():
    """Example of creating a minimal dashboard"""
    
    minimal_data = {
        "title": "Minimal Dashboard",
        "metrics": [
            {"name": "Total", "value": "100", "color": "#3498db"},
            {"name": "Active", "value": "85", "color": "#2ecc71"}
        ],
        "charts": [
            {
                "title": "Simple Chart",
                "type": "bar",
                "labels": ["A", "B", "C"],
                "datasets": [{
                    "label": "Values",
                    "data": [10, 20, 30],
                    "backgroundColor": "#3498db"
                }]
            }
        ]
    }
    
    generator = DashboardGenerator()
    processed_data = generator.process_data(minimal_data)
    output_path = generator.generate_dashboard(processed_data, "minimal_dashboard.html")
    
    print(f"✅ Minimal dashboard created: {output_path}")
    return output_path

def create_from_json_file():
    """Example of creating dashboard from JSON file"""
    
    # Create a sample JSON file
    sample_data = {
        "title": "JSON File Dashboard",
        "description": "Dashboard created from JSON file",
        "metrics": [
            {
                "name": "File Size",
                "value": "2.5 MB",
                "color": "#9b59b6"
            }
        ],
        "charts": [
            {
                "title": "File Types",
                "type": "doughnut",
                "labels": ["JSON", "HTML", "CSS", "JS"],
                "datasets": [{
                    "data": [40, 30, 20, 10],
                    "backgroundColor": ["#3498db", "#2ecc71", "#f39c12", "#e74c3c"]
                }]
            }
        ]
    }
    
    # Save to JSON file
    json_file = "sample_input.json"
    with open(json_file, 'w') as f:
        json.dump(sample_data, f, indent=2)
    
    # Load and generate dashboard
    generator = DashboardGenerator()
    raw_data = generator.load_json_data(json_file)
    processed_data = generator.process_data(raw_data)
    output_path = generator.generate_dashboard(processed_data, "json_file_dashboard.html")
    
    print(f"✅ JSON file dashboard created: {output_path}")
    return output_path

if __name__ == "__main__":
    print("🚀 Dashboard Generator Usage Examples")
    print("="*40)
    
    # Example 1: Custom dashboard
    print("\n1. Creating custom dashboard...")
    custom_path = create_custom_dashboard()
    
    # Example 2: Minimal dashboard
    print("\n2. Creating minimal dashboard...")
    minimal_path = create_minimal_dashboard()
    
    # Example 3: From JSON file
    print("\n3. Creating dashboard from JSON file...")
    json_path = create_from_json_file()
    
    print("\n🎉 All examples completed!")
    print("\nGenerated dashboards:")
    print(f"• Custom: {custom_path}")
    print(f"• Minimal: {minimal_path}")
    print(f"• JSON File: {json_path}")
    
    print("\nTo view dashboards, run:")
    print(f"open {custom_path}")
    print(f"open {minimal_path}")
    print(f"open {json_path}") 