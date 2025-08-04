#!/bin/bash
# Test script for code generation feature

echo "=== Testing Code Generation Feature ==="
echo "Command: claude-code \"Create a Python script that analyzes text files and counts word frequency, save it as mwe/word_counter.py\""
echo ""
echo "Expected behavior:"
echo "- Claude Code will create a new Python file"
echo "- The script should:"
echo "  * Read text files"
echo "  * Count word frequencies"
echo "  * Display results sorted by frequency"
echo "  * Handle command line arguments"
echo "- Save to mwe/word_counter.py"
echo ""
echo "To run this test:"
echo "claude-code \"Create a Python script that analyzes text files and counts word frequency, save it as mwe/word_counter.py\""