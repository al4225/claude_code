#!/bin/bash
# Test script for Git integration

echo "=== Testing Git Integration Feature ==="
echo ""
echo "Setup (run these first):"
echo "cd mwe && git init"
echo ""
echo "Test Commands:"
echo "1. Status check: claude-code \"Show me the git status of the mwe directory\""
echo "2. Stage files: claude-code \"Add all Python files in mwe to git staging\""
echo "3. Commit: claude-code \"Create a git commit with message 'Initial commit: Add calculator and todo app'\""
echo "4. Log: claude-code \"Show me the git log\""
echo ""
echo "Expected behavior:"
echo "- Claude Code will execute git commands"
echo "- Provide clear output of git operations"
echo "- Handle staging and committing files"
echo "- Show commit history"