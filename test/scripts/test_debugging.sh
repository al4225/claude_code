#!/bin/bash
# Test script for debugging feature

echo "=== Testing Debugging Feature ==="
echo "Command: claude-code \"My mwe/buggy_code.py has errors when I run it, please help me debug and fix the issues\""
echo ""
echo "Expected behavior:"
echo "- Claude Code will analyze buggy_code.py"
echo "- Identify the following bugs:"
echo "  * Zero division error in divide_numbers()"
echo "  * Index error in find_max() with empty list"
echo "  * Logic error in find_max() (using == instead of =)"
echo "  * Missing vowels in count_vowels()"
echo "- Provide fixed version of the code"
echo "- Explain each fix"
echo ""
echo "To run this test:"
echo "claude-code \"My mwe/buggy_code.py has errors when I run it, please help me debug and fix the issues\""