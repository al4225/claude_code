#!/bin/bash
# Test script for code explanation feature

echo "=== Testing Code Explanation Feature ==="
echo "Command: claude-code \"Please explain how the code in mwe/calculator.py works\""
echo ""
echo "Expected behavior:"
echo "- Claude Code will read the calculator.py file"
echo "- Provide a detailed explanation of:"
echo "  * The purpose of each function"
echo "  * How the calculate() function routes operations"
echo "  * The overall structure and design"
echo ""
echo "To run this test:"
echo "claude-code \"Please explain how the code in mwe/calculator.py works\""