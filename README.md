# Dashboard Generator Service

A Python console application that converts JSON data into beautiful, interactive HTML dashboards.

## Features

- 📊 **Interactive Charts** - Line, Bar, Pie, and Doughnut charts using Chart.js
- 📈 **Key Metrics Display** - Colorful metric cards with trend indicators
- 📋 **Data Tables** - Searchable and sortable tables
- 🎨 **Beautiful UI** - Modern, responsive design with animations
- 🚀 **Fast Generation** - Quick conversion from JSON to HTML
- 🔍 **Search & Sort** - Built-in table search and sorting functionality
- 📱 **Mobile Responsive** - Works on all device sizes
- 🎯 **Easy to Use** - Simple command-line interface

## Installation

1. Install Python 3.7 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

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

## JSON Data Format

The input JSON should follow this structure:

```json
{
  "title": "My Dashboard",
  "description": "Dashboard description",
  "metrics": [
    {
      "name": "Total Revenue",
      "value": "₹2,45,000",
      "change": "+15%",
      "trend": "up",
      "color": "#2ecc71"
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
        "fill": true
      }]
    }
  ],
  "tables": [
    {
      "title": "Top Products",
      "headers": ["Product", "Sales", "Revenue", "Growth"],
      "rows": [
        ["iPhone 15", "245", "₹2,45,000", "+15%"],
        ["MacBook Pro", "132", "₹1,98,000", "+8%"]
      ],
      "searchable": true,
      "sortable": true
    }
  ],
  "cards": [
    {
      "title": "System Status",
      "content": "All systems operational",
      "type": "success",
      "icon": "✅"
    }
  ],
  "alerts": [
    {
      "type": "success",
      "message": "Monthly target achieved! 🎉",
      "icon": "check-circle"
    }
  ]
}
```

## Data Structure Details

### Metrics
- `name`: Display name for the metric
- `value`: The metric value (can include currency symbols)
- `change`: Percentage change (optional)
- `trend`: "up", "down", or "neutral" (optional)
- `color`: Hex color code for the metric card (optional)

### Charts
- `title`: Chart title
- `type`: Chart type ("line", "bar", "pie", "doughnut")
- `labels`: Array of labels for the chart
- `datasets`: Chart.js dataset format

### Tables
- `title`: Table title
- `headers`: Array of column headers
- `rows`: Array of arrays containing row data
- `searchable`: Enable search functionality (default: true)
- `sortable`: Enable column sorting (default: true)

### Cards
- `title`: Card title
- `content`: Card content/description
- `type`: "info", "success", "warning", "error"
- `icon`: Emoji or icon for the card

### Alerts
- `type`: "success", "warning", "error", "info"
- `message`: Alert message
- `icon`: FontAwesome icon name (optional)

## Examples

### Generate Sample Dashboard
```bash
python dashboard_generator.py --sample
python dashboard_generator.py -i output/sample_data.json -o sample_dashboard.html --open
```

### Custom Data Example
```json
{
  "title": "Website Analytics",
  "description": "Monthly website performance metrics",
  "metrics": [
    {
      "name": "Page Views",
      "value": "125,430",
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
    }
  ],
  "charts": [
    {
      "title": "Daily Visitors",
      "type": "line",
      "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
      "datasets": [{
        "label": "Visitors",
        "data": [1200, 1900, 3000, 5000, 2000, 3000, 4500],
        "borderColor": "#e74c3c",
        "backgroundColor": "rgba(231, 76, 60, 0.1)",
        "fill": true
      }]
    }
  ]
}
```

## Output

The generated HTML dashboard includes:
- Modern, responsive design
- Interactive charts powered by Chart.js
- Searchable and sortable tables
- Animated metric cards
- Professional styling with gradients and shadows
- Mobile-friendly layout
- Loading animations
- FontAwesome icons

## Directory Structure

```
DashboardService/
├── dashboard_generator.py    # Main application
├── requirements.txt          # Dependencies
├── README.md                # This file
├── templates/               # Template directory (auto-created)
└── output/                  # Output directory (auto-created)
    ├── dashboard.html       # Generated dashboards
    └── sample_data.json     # Sample data file
```

## Features in Detail

### Interactive Charts
- Powered by Chart.js library
- Supports line, bar, pie, and doughnut charts
- Responsive and interactive
- Customizable colors and styling

### Data Tables
- Built-in search functionality
- Column sorting (numeric and alphabetic)
- Responsive design
- Hover effects and alternating row colors

### Metric Cards
- Animated gradient backgrounds
- Trend indicators with arrows
- Color-coded based on performance
- Shimmer animation effects

### Responsive Design
- Works on desktop, tablet, and mobile
- Flexible grid layout
- Optimized for all screen sizes

## Contributing

Feel free to submit issues and pull requests to improve the dashboard generator!

## License

This project is open source and available under the MIT License. 