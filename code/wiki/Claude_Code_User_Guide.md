# Claude Code User Guide - Making Programming Simple

## Table of Contents
1. [Introduction](#introduction)
2. [Why Choose Claude Code](#why-choose-claude-code)
3. [Installation Guide](#installation-guide)
4. [Getting Started](#getting-started)
5. [Core Features Demo](#core-features-demo)
6. [Slash Commands Reference](#slash-commands-reference)
7. [Keyboard Shortcuts](#keyboard-shortcuts)
8. [Best Practices](#best-practices)
9. [FAQ](#faq)

## Introduction

### What is Claude Code?
Claude Code is a powerful AI programming assistant that helps you:
- 🤖 Understand and explain code
- 🐛 Debug and fix errors
- ✏️ Write and edit code
- 📁 Directly manipulate the file system
- 🔄 Use Git for version control
- 📊 Generate charts and documentation

Think of it as your programming partner that understands your needs and helps you complete programming tasks!

## Why Choose Claude Code?

### Key Advantages
1. **Intelligent Understanding** - Understands natural language descriptions, no complex commands needed
2. **Full-Stack Capabilities** - From frontend to backend, Python to JavaScript, Claude Code can help
3. **Real-time Operations** - Create, edit, and run code directly
4. **Error-Friendly** - Automatically finds and fixes common errors
5. **Learning Assistant** - Explains code in detail to help you learn programming

### Who Should Use It?
- 👶 Programming Beginners: Learn programming through natural language
- 👨‍💻 Professional Developers: Boost development efficiency
- 🎓 Students: Complete programming assignments and projects
- 🔬 Researchers: Quickly implement algorithms and data processing

## Installation Guide

### Prerequisites: Install Node.js (Version 18 or Higher)

#### Windows Users (Using WSL)
```bash
# 1. First install WSL (run in PowerShell as Administrator)
wsl --install

# 2. After restarting, open WSL terminal
# 3. Install Node.js in WSL
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# 4. Verify installation
node --version  # Should show v18.x.x or higher
```

#### Mac Users
```bash
# Using Homebrew
brew install node@18

# Or download installer from official website
# Visit https://nodejs.org/ to download LTS version

# Verify installation
node --version
```

#### Linux Users
```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# CentOS/RHEL/Fedora
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo yum install nodejs

# Verify installation
node --version
```

### Installing Claude Code

```bash
# Install globally using npm
npm install -g @anthropic-ai/claude-code

# Verify installation
claude-code --version
```

### Setting Up API Key
```bash
# Get API key from: https://console.anthropic.com/
# Set environment variable

# Linux/Mac/WSL
export ANTHROPIC_API_KEY="your-api-key"

# Add to config file for permanent setup
echo 'export ANTHROPIC_API_KEY="your-api-key"' >> ~/.bashrc
source ~/.bashrc
```

## Getting Started

### Basic Environment Setup

1. **Create Working Directory**
```bash
mkdir my-first-project
cd my-first-project
```

2. **Start Claude Code**
```bash
claude-code
```

3. **Basic Interaction Example**
```
You: Hello! Please create a simple Python program that prints "Hello World"

Claude: I'll help you create a simple Python program.

[Creates hello.py]
print("Hello World")

You: Run this program

Claude: [Runs python hello.py]
Hello World
```

## Core Features Demo

### 1. Code Explanation
```bash
# Test command
claude-code "Please explain how the code in mwe/calculator.py works"
```

### 2. Debugging
```bash
# Test command
claude-code "My mwe/buggy_code.py has errors, please help me debug"
```

### 3. Writing New Code
```bash
# Test command
claude-code "Help me write a simple todo list manager in Python, save it to mwe/todo_app.py"
```

### 4. Editing Existing Code
```bash
# Test command
claude-code "Add multiplication and division functions to mwe/calculator.py"
```

### 5. Git Integration
```bash
# Test command
claude-code "Help me commit all changes with message 'Add new features'"
```

### 6. Chart Generation
```bash
# Test command
claude-code "Use matplotlib to create a bar chart showing monthly sales data, save to test/outputs/sales_chart.png"
```

### 7. Testing and Debugging
```bash
# Test command
claude-code "Write unit tests for mwe/calculator.py"
```

### 8. Documentation Generation
```bash
# Test command
claude-code "Generate API documentation for all Python files in mwe directory"
```

### 9. Code Review
```bash
# Test command
claude-code "Review the code quality of mwe/calculator.py and suggest improvements"
```

## Slash Commands Reference

| Command | Function | Example |
|---------|----------|---------|
| `/help` | Show help information | `/help` |
| `/new` | Create new file | `/new python script.py` |
| `/edit` | Edit file | `/edit calculator.py` |
| `/run` | Run code | `/run python script.py` |
| `/test` | Run tests | `/test` |
| `/git` | Git operations | `/git status` |
| `/search` | Search code | `/search "function calculate"` |
| `/explain` | Explain code | `/explain calculator.py` |
| `/debug` | Debug code | `/debug error.py` |
| `/docs` | Generate documentation | `/docs generate` |

## Keyboard Shortcuts

| Shortcut | Function |
|----------|----------|
| `Ctrl+C` | Interrupt current operation |
| `Ctrl+D` | Exit Claude Code |
| `Ctrl+L` | Clear screen |
| `Tab` | Auto-complete |
| `↑/↓` | Browse command history |

## Best Practices

### 1. Clear Instruction Format
```
❌ Bad example:
"write code"

✅ Good example:
"Please create a Python function that takes two number parameters, returns their sum, and includes error handling"
```

### 2. Plan Before Execute
```
Recommended workflow:
1. "Help me plan the implementation steps for a user login system"
2. "Now let's implement step 1: create user model"
3. "Continue with step 2: create login interface"
```

### 3. Provide Context
```
✅ "Add a new API endpoint /users to the existing Flask application"
✅ "Write tests for calculator.py using pytest framework"
```

### 4. Iterative Improvement
```
1. "Create a simple calculator"
2. "Add square root functionality"
3. "Add history feature"
4. "Optimize the UI design"
```

### 5. Use Code Review
```
Regular use:
"Review the code I just wrote, check for potential issues"
"How's the performance of this code? Any optimization suggestions?"
```

## FAQ

### Q: What programming languages does Claude Code support?
A: Supports almost all mainstream languages including Python, JavaScript, Java, C++, Go, Rust, etc.

### Q: How large of a project can it handle?
A: Can handle projects of all sizes, from single files to large codebases.

### Q: How is my code security protected?
A: Claude Code runs locally, your code is not uploaded to the cloud (unless you explicitly request it).

### Q: What to do when encountering errors?
A: Simply tell Claude Code about the error you're facing, and it will help analyze and solve it.

---

## Video Tutorial

<div align="center">
  <img src="test/outputs/demo_animation.gif" alt="Claude Code Demo Animation" width="800">
  
  *Complete demonstration from installation to usage*
</div>

## Additional Resources

- 📚 [Official Documentation](https://docs.anthropic.com/claude-code)
- 💬 [Community Forum](https://community.anthropic.com)
- 🐛 [Report Issues](https://github.com/anthropics/claude-code/issues)
- 📧 [Contact Support](support@anthropic.com)

---

Remember: Claude Code is your programming partner, don't be afraid to try and ask questions! 🚀