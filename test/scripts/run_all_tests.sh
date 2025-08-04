#!/bin/bash
# Master script to demonstrate all Claude Code features

echo "==================================="
echo "Claude Code Feature Test Suite"
echo "==================================="
echo ""
echo "This script provides commands to test all major Claude Code features."
echo "Run each command separately in your terminal with Claude Code."
echo ""

# Make all test scripts executable
chmod +x test_*.sh

# List all available tests
echo "Available tests:"
echo "1. Code Explanation - ./test_code_explanation.sh"
echo "2. Debugging - ./test_debugging.sh"
echo "3. Code Generation - ./test_code_generation.sh"
echo "4. Code Editing - ./test_code_editing.sh"
echo "5. Git Integration - ./test_git_integration.sh"
echo "6. Chart Generation - ./test_chart_generation.sh"
echo "7. Unit Testing - ./test_unit_testing.sh"
echo "8. Documentation - ./test_documentation.sh"
echo "9. Code Review - ./test_code_review.sh"
echo ""
echo "To view a test description, run:"
echo "bash ./test_<feature_name>.sh"
echo ""
echo "Example workflow:"
echo "1. Start Claude Code: claude-code"
echo "2. Copy and paste the test command from the test script"
echo "3. Observe Claude Code's response"
echo "4. Check the output in test/outputs/ directory"