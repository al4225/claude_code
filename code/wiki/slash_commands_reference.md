# Claude Code Slash Commands Reference

## Complete Command List

### File Operations

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/new` | Create a new file | `/new [type] <filename>` | `/new python calculator.py` |
| `/open` | Open and display a file | `/open <filename>` | `/open main.py` |
| `/edit` | Edit an existing file | `/edit <filename>` | `/edit config.json` |
| `/save` | Save current changes | `/save` | `/save` |
| `/delete` | Delete a file | `/delete <filename>` | `/delete temp.txt` |

### Code Execution

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/run` | Execute code or script | `/run <command>` | `/run python app.py` |
| `/test` | Run test suite | `/test [file/directory]` | `/test tests/` |
| `/debug` | Start debugging session | `/debug <filename>` | `/debug buggy.py` |
| `/shell` | Execute shell command | `/shell <command>` | `/shell ls -la` |

### Code Analysis

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/explain` | Explain code functionality | `/explain <filename>` | `/explain algorithm.py` |
| `/search` | Search in codebase | `/search "<pattern>"` | `/search "TODO"` |
| `/find` | Find files by name | `/find <pattern>` | `/find *.py` |
| `/analyze` | Analyze code quality | `/analyze <filename>` | `/analyze main.py` |

### Git Operations

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/git` | Execute git command | `/git <command>` | `/git status` |
| `/commit` | Create a commit | `/commit "<message>"` | `/commit "Fix bug"` |
| `/push` | Push to remote | `/push [branch]` | `/push main` |
| `/pull` | Pull from remote | `/pull [branch]` | `/pull main` |
| `/branch` | Manage branches | `/branch <action>` | `/branch create feature` |

### Documentation

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/docs` | Generate documentation | `/docs <action>` | `/docs generate` |
| `/comment` | Add comments to code | `/comment <filename>` | `/comment utils.py` |
| `/readme` | Create/update README | `/readme [template]` | `/readme standard` |

### Project Management

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/project` | Project operations | `/project <action>` | `/project init` |
| `/todo` | Manage TODOs | `/todo <action>` | `/todo list` |
| `/deps` | Manage dependencies | `/deps <action>` | `/deps install` |

### AI Assistance

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/suggest` | Get code suggestions | `/suggest <context>` | `/suggest optimize` |
| `/refactor` | Refactor code | `/refactor <filename>` | `/refactor legacy.py` |
| `/review` | Code review | `/review <filename>` | `/review pr_changes.py` |
| `/complete` | Auto-complete code | `/complete` | `/complete` |

### System Commands

| Command | Description | Syntax | Example |
|---------|-------------|---------|---------|
| `/help` | Show help | `/help [command]` | `/help git` |
| `/clear` | Clear screen | `/clear` | `/clear` |
| `/exit` | Exit Claude Code | `/exit` | `/exit` |
| `/config` | Manage configuration | `/config <setting>` | `/config api_key` |

## Command Shortcuts

Some commands have shorter aliases for convenience:

- `/e` → `/edit`
- `/r` → `/run`
- `/s` → `/save`
- `/g` → `/git`
- `/h` → `/help`
- `/q` → `/exit`

## Command Chaining

You can chain multiple commands using `&&`:

```
/edit main.py && /run python main.py && /test
```

## Command History

- Use `↑` and `↓` arrows to navigate command history
- `/history` to view recent commands
- `/history clear` to clear command history

## Custom Commands

You can create custom slash commands by adding them to your `.claude-code/commands.json`:

```json
{
  "custom_commands": {
    "/build": "npm run build && npm test",
    "/deploy": "git push origin main && npm run deploy",
    "/format": "prettier --write . && eslint --fix ."
  }
}
```

## Tips

1. **Tab Completion**: Press `Tab` to auto-complete file names and commands
2. **Wildcards**: Use `*` for pattern matching in file operations
3. **Quotes**: Use quotes for arguments with spaces: `/commit "Fix critical bug"`
4. **Relative Paths**: Commands support both relative and absolute paths
5. **Background Execution**: Add `&` to run commands in background: `/run python server.py &`