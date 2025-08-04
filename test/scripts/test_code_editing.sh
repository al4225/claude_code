#!/bin/bash
# Test script for code editing feature

echo "=== Testing Code Editing Feature ==="
echo "Command: claude-code \"Add multiplication and division functions to mwe/calculator.py, and update the calculate function to support them\""
echo ""
echo "Expected behavior:"
echo "- Claude Code will read the existing calculator.py"
echo "- Add two new functions:"
echo "  * multiply(a, b)"
echo "  * divide(a, b) with zero division check"
echo "- Update calculate() to handle 'multiply' and 'divide' operations"
echo "- Update the main block to demonstrate new operations"
echo ""
echo "To run this test:"
echo "claude-code \"Add multiplication and division functions to mwe/calculator.py, and update the calculate function to support them\""