#!/usr/bin/env python3
"""
Test script for Dashboard Generator
Demonstrates various dashboard configurations
"""

import json
import os
import sys
from pathlib import Path
from dashboard_generator import DashboardGenerator

def create_test_data():
    """Create various test data configurations"""
    
    # Test 1: Sales Dashboard
    sales_data = {
        "title": "Sales Performance Dashboard",
        "description": "Q4 2024 Sales Analytics and KPIs",
        "metrics": [
            {
                "name": "Total Revenue",
                "value": "₹15,75,000",
                "change": "+23%",
                "trend": "up",
                "color": "#2ecc71"
            },
            {
                "name": "New Customers",
                "value": "2,847",
                "change": "+15%",
                "trend": "up",
                "color": "#3498db"
            },
            {
                "name": "Orders",
                "value": "1,256",
                "change": "-2%",
                "trend": "down",
                "color": "#e74c3c"
            },
            {
                "name": "Conversion Rate",
                "value": "4.2%",
                "change": "+0.8%",
                "trend": "up",
                "color": "#f39c12"
            }
        ],
        "charts": [
            {
                "title": "Monthly Revenue Trend",
                "type": "line",
                "labels": ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "datasets": [{
                    "label": "Revenue (₹)",
                    "data": [1200000, 1350000, 1100000, 1450000, 1650000, 1575000],
                    "borderColor": "#3498db",
                    "backgroundColor": "rgba(52, 152, 219, 0.1)",
                    "fill": True
                }]
            },
            {
                "title": "Product Categories Distribution",
                "type": "doughnut",
                "labels": ["Electronics", "Clothing", "Books", "Home & Garden", "Sports"],
                "datasets": [{
                    "data": [40, 25, 15, 12, 8],
                    "backgroundColor": [
                        "#3498db", "#2ecc71", "#f39c12", "#e74c3c", "#9b59b6"
                    ]
                }]
            },
            {
                "title": "Weekly Sales Comparison",
                "type": "bar",
                "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
                "datasets": [{
                    "label": "This Month",
                    "data": [380000, 420000, 390000, 385000],
                    "backgroundColor": "#3498db"
                }, {
                    "label": "Last Month",
                    "data": [350000, 380000, 360000, 370000],
                    "backgroundColor": "#95a5a6"
                }]
            }
        ],
        "tables": [
            {
                "title": "Top Performing Products",
                "headers": ["Product", "Units Sold", "Revenue", "Growth", "Category"],
                "rows": [
                    ["iPhone 15 Pro", "245", "₹2,45,000", "+15%", "Electronics"],
                    ["MacBook Pro M3", "132", "₹1,98,000", "+8%", "Electronics"],
                    ["Nike Air Max", "89", "₹89,000", "+12%", "Sports"],
                    ["Samsung 4K TV", "156", "₹1,56,000", "+25%", "Electronics"],
                    ["Levi's Jeans", "78", "₹39,000", "+5%", "Clothing"],
                    ["Python Programming Book", "234", "₹23,400", "+18%", "Books"],
                    ["Coffee Maker", "67", "₹67,000", "+3%", "Home & Garden"]
                ],
                "searchable": True,
                "sortable": True
            }
        ],
        "cards": [
            {
                "title": "System Status",
                "content": "All payment systems operational. Last sync: 5 minutes ago",
                "type": "success",
                "icon": "✅"
            },
            {
                "title": "Inventory Alert",
                "content": "3 products running low on stock. Reorder recommended.",
                "type": "warning",
                "icon": "⚠️"
            },
            {
                "title": "Customer Feedback",
                "content": "Average rating: 4.7/5 stars from 1,234 reviews",
                "type": "info",
                "icon": "⭐"
            }
        ],
        "alerts": [
            {
                "type": "success",
                "message": "🎉 Monthly sales target exceeded by 23%!",
                "icon": "check-circle"
            },
            {
                "type": "warning",
                "message": "📦 Low inventory alert for iPhone 15 Pro (5 units remaining)",
                "icon": "exclamation-triangle"
            }
        ]
    }
    
    # Test 2: Website Analytics Dashboard
    analytics_data = {
        "title": "Website Analytics Dashboard",
        "description": "Real-time website performance and user engagement metrics",
        "metrics": [
            {
                "name": "Page Views",
                "value": "1,25,430",
                "change": "+12%",
                "trend": "up",
                "color": "#3498db"
            },
            {
                "name": "Unique Visitors",
                "value": "45,231",
                "change": "+8%",
                "trend": "up",
                "color": "#2ecc71"
            },
            {
                "name": "Bounce Rate",
                "value": "32%",
                "change": "-5%",
                "trend": "up",
                "color": "#f39c12"
            },
            {
                "name": "Avg. Session Duration",
                "value": "3:45",
                "change": "+15%",
                "trend": "up",
                "color": "#9b59b6"
            }
        ],
        "charts": [
            {
                "title": "Daily Visitors (Last 7 Days)",
                "type": "line",
                "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                "datasets": [{
                    "label": "Visitors",
                    "data": [1200, 1900, 3000, 5000, 2000, 3000, 4500],
                    "borderColor": "#e74c3c",
                    "backgroundColor": "rgba(231, 76, 60, 0.1)",
                    "fill": True
                }]
            },
            {
                "title": "Traffic Sources",
                "type": "pie",
                "labels": ["Direct", "Search", "Social", "Email", "Referral"],
                "datasets": [{
                    "data": [35, 30, 20, 10, 5],
                    "backgroundColor": [
                        "#3498db", "#2ecc71", "#f39c12", "#e74c3c", "#9b59b6"
                    ]
                }]
            }
        ],
        "tables": [
            {
                "title": "Top Pages",
                "headers": ["Page", "Views", "Unique Views", "Bounce Rate", "Avg. Time"],
                "rows": [
                    ["/home", "25,430", "18,234", "25%", "2:45"],
                    ["/products", "18,234", "15,123", "30%", "3:20"],
                    ["/about", "12,345", "10,987", "40%", "1:30"],
                    ["/contact", "8,765", "7,654", "35%", "2:15"],
                    ["/blog", "6,543", "5,432", "45%", "4:20"]
                ],
                "searchable": True,
                "sortable": True
            }
        ],
        "cards": [
            {
                "title": "Server Status",
                "content": "All servers running smoothly. Uptime: 99.9%",
                "type": "success",
                "icon": "🟢"
            },
            {
                "title": "CDN Performance",
                "content": "Average load time: 1.2s across all regions",
                "type": "info",
                "icon": "⚡"
            }
        ],
        "alerts": [
            {
                "type": "info",
                "message": "📊 Monthly traffic increased by 12% compared to last month",
                "icon": "info-circle"
            }
        ]
    }
    
    # Test 3: Simple Dashboard
    simple_data = {
        "title": "Simple Dashboard",
        "description": "Basic dashboard with minimal data",
        "metrics": [
            {
                "name": "Users",
                "value": "1,234",
                "color": "#3498db"
            },
            {
                "name": "Revenue",
                "value": "$12,345",
                "color": "#2ecc71"
            }
        ],
        "charts": [
            {
                "title": "Monthly Growth",
                "type": "bar",
                "labels": ["Jan", "Feb", "Mar"],
                "datasets": [{
                    "label": "Growth",
                    "data": [10, 20, 30],
                    "backgroundColor": "#3498db"
                }]
            }
        ]
    }
    
    return {
        "sales": sales_data,
        "analytics": analytics_data,
        "simple": simple_data
    }

def run_tests():
    """Run dashboard generation tests"""
    print("🧪 Running Dashboard Generator Tests...")
    
    generator = DashboardGenerator()
    test_data = create_test_data()
    
    # Use the generator's output directory
    output_dir = generator.output_dir
    
    test_results = []
    
    for test_name, data in test_data.items():
        try:
            print(f"\n📊 Generating {test_name} dashboard...")
            
            # Process data
            processed_data = generator.process_data(data)
            
            # Generate dashboard
            output_file = f"{test_name}_dashboard.html"
            output_path = generator.generate_dashboard(processed_data, output_file)
            
            # Verify file was created
            if output_path.exists():
                file_size = output_path.stat().st_size
                print(f"✅ {test_name} dashboard created: {output_path}")
                print(f"   File size: {file_size:,} bytes")
                print(f"   Metrics: {len(processed_data['metrics'])}")
                print(f"   Charts: {len(processed_data['charts'])}")
                print(f"   Tables: {len(processed_data['tables'])}")
                
                test_results.append({
                    "name": test_name,
                    "status": "✅ PASSED",
                    "file": output_path,
                    "size": file_size
                })
            else:
                test_results.append({
                    "name": test_name,
                    "status": "❌ FAILED",
                    "file": None,
                    "size": 0
                })
                
        except Exception as e:
            print(f"❌ Error generating {test_name} dashboard: {e}")
            test_results.append({
                "name": test_name,
                "status": f"❌ ERROR: {e}",
                "file": None,
                "size": 0
            })
    
    # Print summary
    print("\n" + "="*50)
    print("📋 TEST RESULTS SUMMARY")
    print("="*50)
    
    for result in test_results:
        print(f"{result['status']} {result['name']}")
        if result['file']:
            print(f"   📄 File: {result['file']}")
            print(f"   📊 Size: {result['size']:,} bytes")
    
    print(f"\n🎯 Total tests: {len(test_results)}")
    passed = sum(1 for r in test_results if "PASSED" in r['status'])
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {len(test_results) - passed}")
    
    return test_results

if __name__ == "__main__":
    results = run_tests()
    
    # If all tests passed, offer to open dashboards
    if all("PASSED" in r['status'] for r in results):
        print("\n🌐 All tests passed! Would you like to open the dashboards?")
        print("Run these commands to view the generated dashboards:")
        for result in results:
            if result['file']:
                print(f"   open {result['file']}")
    else:
        print("\n⚠️  Some tests failed. Check the error messages above.")
        sys.exit(1) 