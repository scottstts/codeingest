# Codebase Analyzer 🔍

A powerful local development tool that combines **Repomix** and **Google Gemini** to provide comprehensive codebase analysis for AI coding agents and developers. Perfect for debugging, planning, and understanding complex codebases.

## What it does

This tool helps AI coding agents (like those in Cursor IDE or Claude Code) get a complete understanding of your entire codebase instead of working with isolated code snippets. It:

1. 📦 Creates a complete snapshot of your codebase using Repomix
2. 🤖 Sends the entire codebase to Google Gemini for analysis
3. 🧠 Returns comprehensive insights about code structure, dependencies, and architecture
4. 🧹 Automatically cleans up temporary files

## Prerequisites

### 1. Install Repomix
Check out the [Repomix Repo](https://github.com/yamadashy/repomix)

```bash
# Install repomix globally
npm install -g repomix

# Or install via other methods
brew install repomix        # macOS with Homebrew
yarn global add repomix     # Using Yarn
```

### 2. Get Google Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Copy the API key for in .env

### 3. Python Dependencies
```bash
pip install google-genai python-dotenv
```

## Installation

1. **put `codeingest.py:** in your codebase

2. **Set up your API key:**

## Usage

### Basic Usage
```bash
# Analyze codebase with a specific question
python3 codeingest.py --instruction "Explain the overall architecture and main components"
```

### Real-world Examples

**For Debugging:**
```bash
python3 codeingest.py --instruction "I'm running into a bug where user authentication fails intermittently. Help me understand the complete auth flow across the codebase and identify potential race conditions or state management issues."
```

**For Code Planning:**
```bash
python3 codeingest.py --instruction "I need to add a new API endpoint for file uploads. Show me the existing API patterns, middleware structure, and where I should implement this feature to maintain consistency."
```

**For Architecture Understanding:**
```bash
python3 codeingest.py --instruction "I'm new to this codebase. Give me a comprehensive breakdown of the project structure, main components, data flow, and how different modules interact with each other."
```

**For Refactoring:**
```bash
python3 codeingest.py --instruction "I want to extract the database logic into a separate service layer. Analyze all database interactions across the codebase and suggest a refactoring strategy."
```

### Advanced Options
```bash
# Enable verbose output for debugging
python3 codeingest.py --instruction "your question" --verbose

# Get help
python3 codeingest.py --help
```

## Integration with AI Coding Agents

This tool is designed to work seamlessly with AI coding agents in IDEs like Cursor. The agent can call this tool to get comprehensive codebase understanding:

```bash
# Example: Agent discovering how to implement a feature
python3 codeingest.py --instruction "I need to implement user roles and permissions. Analyze the current user management system and suggest how to extend it with role-based access control."
```

The agent can then use the detailed analysis to make informed decisions about code changes, debugging approaches, or architectural modifications.

## System Prompt for AI Coding Agents

**Important:** Add this to your AI coding agent's system prompt (Cursor, Claude Code, etc.) to enable codebase analysis capabilities:

```markdown
**Codebase Analysis Tool Available**: You have access to a powerful local codebase analysis tool called `codeingest` that provides comprehensive understanding of entire codebases using Repomix + Google Gemini. This tool is essential for complex debugging, architecture understanding, and planning tasks that require full codebase context rather than isolated code snippets. Use it when you need to understand interdependencies, trace issues across multiple files, or plan changes that could have ripple effects.

**Usage**: `python3 codeingest.py --instruction "your detailed question/request"`

You can reference certain directoreis and files too inside your instruction.

**When to use**:
• **Debugging complex issues** that span multiple files or modules
• **Understanding code architecture** and component relationships  
• **Planning new features** and ensuring consistency with existing patterns
• **Refactoring guidance** that considers system-wide impact
• **Dependency analysis** and identifying potential bottlenecks
• **Code review** and architectural assessment
• **Any task requiring full codebase context** rather than snippet-based analysis

**Example commands**:
• `python3 codeingest.py --instruction "Analyze the authentication flow and identify why sessions are timing out randomly"`
• `python3 codeingest.py --instruction "I need to add caching. Show me existing patterns and suggest where to implement Redis integration"`
• `python3 codeingest.py --instruction "Explain the database schema relationships and how they map to the API endpoints"`
```

---

## How It Works

1. **Repomix Snapshot**: Creates a complete, AI-friendly representation of your codebase
2. **Gemini Analysis**: Sends the entire codebase context to Google's advanced language model
3. **Comprehensive Response**: Returns detailed insights about code structure, dependencies, and architectural patterns
4. **Clean Cleanup**: Automatically removes temporary files

## Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Repomix Configuration
The tool uses your existing repomix configuration if available. You can customize what gets included in the analysis by:

1. **Using .gitignore**: Repomix automatically respects your .gitignore files
2. **Creating .repomixignore**: Add additional patterns to exclude
3. **Repomix config**: Create a `repomix.config.json` for advanced settings

Example `.repomixignore`:
```
*.log
node_modules/
.env
dist/
coverage/
```

## Troubleshooting

### Common Issues

**"repomix is not installed"**
```bash
# Install repomix
npm install -g repomix
# Verify installation
repomix --version
```

**"GEMINI_API_KEY environment variable not set"**
- Make sure your .env file is in the same directory as the script
- Or export the API key: `export GEMINI_API_KEY="your_key"`

**"Error running repomix"**
- Ensure you're in a directory with code files
- Check that repomix can access the current directory
- Verify your repomix configuration

**Large Codebase Issues**
- Consider using repomix ignore patterns to exclude unnecessary files
- Break down very large codebases into smaller analysis chunks
- Use `--verbose` flag to see what's being processed

### Performance Tips

1. **Exclude unnecessary files**: Use `.repomixignore` to exclude logs, build artifacts, etc.
2. **Focus your questions**: More specific instructions yield better, faster results
3. **Use in CI/CD**: Great for automated code reviews and documentation generation

## Security Considerations

- ⚠️ **Never commit API keys** to version control
- 🔒 **Review codebase content** before analysis if working with sensitive code
- 🛡️ **Use .repomixignore** to exclude sensitive files and directories
- 🔐 **Consider using environment-specific configurations** for different deployment contexts

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool!

## License

This project is open source. Please check the license file for details.

---

**Happy Coding! 🚀**

*This tool is designed to supercharge your development workflow by giving AI agents the full context they need to provide meaningful assistance.*