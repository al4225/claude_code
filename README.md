# Claude Code User Guide Project

This project contains a comprehensive guide for using Claude Code, designed to help beginners and even middle school students learn how to use this powerful AI programming assistant.

## Project Structure

```
claude_code/
├── mwe/                    # Minimal Working Examples
│   ├── calculator.py       # Basic calculator for testing
│   ├── buggy_code.py      # Intentionally buggy code for debugging demos
│   ├── todo_app.py        # Complete todo list application
│   └── README.md          # MWE directory documentation
│
├── test/                   # Test scripts and outputs
│   ├── scripts/           # Test scenario scripts
│   │   ├── test_code_explanation.sh
│   │   ├── test_debugging.sh
│   │   ├── test_code_generation.sh
│   │   ├── test_code_editing.sh
│   │   ├── test_git_integration.sh
│   │   ├── test_chart_generation.sh
│   │   ├── test_unit_testing.sh
│   │   ├── test_documentation.sh
│   │   ├── test_code_review.sh
│   │   └── run_all_tests.sh
│   └── outputs/           # Test outputs directory
│       └── demo_script.txt
│
├── code/                   # Main code and documentation
│   ├── wiki/              # Wiki documentation
│   │   ├── Claude_Code_User_Guide.md
│   │   ├── slash_commands_reference.md
│   │   └── best_practices.md
│   └── utils/             # Utility scripts
│       └── create_demo_animation.py
│
├── cheatsheet.txt         # Quick reference guide
└── README.md             # This file
```

## Quick Start

1. **Read the Main Guide**: Start with `code/wiki/Claude_Code_User_Guide.md`
2. **Check the Cheatsheet**: Keep `cheatsheet.txt` handy for quick reference
3. **Try the Examples**: Run the examples in the `mwe/` directory
4. **Run Tests**: Use scripts in `test/scripts/` to test different features

## Key Documents

- **Main User Guide**: `code/wiki/Claude_Code_User_Guide.md` - Complete guide from installation to advanced usage
- **Slash Commands**: `code/wiki/slash_commands_reference.md` - All available slash commands
- **Best Practices**: `code/wiki/best_practices.md` - Query formats and usage recommendations
- **Quick Reference**: `cheatsheet.txt` - One-page quick reference

## Testing Claude Code Features

Each test script in `test/scripts/` demonstrates a specific feature:

```bash
# Make scripts executable
chmod +x test/scripts/*.sh

# View a test description
bash test/scripts/test_code_explanation.sh

# Run the actual test in Claude Code
claude-code "Please explain how the code in mwe/calculator.py works"
```

## Example Commands to Try

Here are some commands you can copy and paste into Claude Code:

### Basic Operations
- `"Create a Python hello world program"`
- `"Explain the code in mwe/calculator.py"`
- `"Run mwe/todo_app.py"`

### Debugging
- `"Help me debug mwe/buggy_code.py"`
- `"Fix the errors in buggy_code.py"`

### Code Generation
- `"Create a simple web server using Flask"`
- `"Write a function to validate email addresses"`

### Git Operations
- `"Show git status"`
- `"Commit all changes with message 'Initial commit'"`

### Advanced Features
- `"Review mwe/todo_app.py for code quality"`
- `"Generate API documentation for all Python files in mwe/"`
- `"Write unit tests for calculator.py"`

## Tips for Success

1. **Be Specific**: Instead of "fix bug", say "fix the TypeError in line 42"
2. **Provide Context**: Mention the framework, language, and existing code
3. **Start Simple**: Begin with basic tasks and gradually increase complexity
4. **Use Natural Language**: Claude Code understands everyday language
5. **Ask for Explanations**: Don't hesitate to ask why something works

## Need Help?

- Check the main guide: `code/wiki/Claude_Code_User_Guide.md`
- Review best practices: `code/wiki/best_practices.md`
- Consult the cheatsheet: `cheatsheet.txt`
- Report issues: https://github.com/anthropics/claude-code/issues

Happy coding with Claude Code! 🚀