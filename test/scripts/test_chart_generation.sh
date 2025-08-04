#!/bin/bash
# Test script for chart generation feature

echo "=== Testing Chart Generation Feature ==="
echo "Command: claude-code \"Create a Python script that generates a bar chart showing monthly sales data (Jan: 15000, Feb: 18000, Mar: 22000, Apr: 19000, May: 24000, Jun: 26000) using matplotlib, save the chart as test/outputs/sales_chart.png\""
echo ""
echo "Expected behavior:"
echo "- Claude Code will create a Python script"
echo "- Use matplotlib to generate a bar chart"
echo "- Include proper labels and title"
echo "- Save the output to test/outputs/sales_chart.png"
echo "- The chart should be visually appealing with:"
echo "  * Clear axis labels"
echo "  * Title"
echo "  * Different colors for bars"
echo ""
echo "To run this test:"
echo "claude-code \"Create a Python script that generates a bar chart showing monthly sales data (Jan: 15000, Feb: 18000, Mar: 22000, Apr: 19000, May: 24000, Jun: 26000) using matplotlib, save the chart as test/outputs/sales_chart.png\""