# Codebase Analyzer 🔍

A local dev tool that provides codebase analysis for AI coding agents.

## What it does

This tool helps AI coding agents (like those in Cursor IDE or Claude Code) get a complete understanding of your entire codebase instead of working with isolated code snippets. It:

1. 📦 Creates a complete snapshot of your codebase using Repomix
2. 🤖 Sends the entire codebase to Google Gemini for analysis
3. 🧠 Returns comprehensive insights about code structure, dependencies, and architecture
4. 🧹 Automatically cleans up temporary files

## Prerequisites

### 1. Install Repomix
Check out the [Repomix Repo](https://github.com/yamadashy/repomix)

### 2. Get Google Gemini API Key

### 3. Python Dependencies
```bash
conda activate your_env && pip install google-genai python-dotenv
```

## Setup

1. Put `codeingest.py` in your codebase

2. Set up `.env` with API key, a `.repomixignore` to omit files you don't want to include:

Example `.repomixignore`:
```
*.log
node_modules/
.env
dist/
coverage/
```

3. Set up the system prompt for your coding tool (like Cursor or Claude Code) with below provided system prompt.

## System Prompt for AI Coding Agents

**Important:** Add this to your AI coding agent's system prompt (Cursor, Claude Code, etc.) to enable codebase analysis capabilities:

```markdown
**Codebase Analysis Tool Available**: You have access to a powerful local codebase analysis tool called `codeingest` that provides comprehensive understanding of entire codebases using Repomix + Google Gemini. This tool is essential for complex debugging, architecture understanding, and planning tasks that require full codebase context rather than isolated code snippets. Use it when you need to understand interdependencies, trace issues across multiple files, or plan changes that could have ripple effects.

**Usage**: `python3 codeingest.py --instruction "your detailed question/request"`

You can reference certain directoreis and files too inside your instruction.

**Advanced Options:**

`python3 codeingest.py --instruction "your question" --verbose`

`python3 codeingest.py --help`

**When to use**:

• **Debugging complex issues** that span multiple files or modules

• **Understanding code architecture** and component relationships  

• **Planning new features** and ensuring consistency with existing patterns

• **Refactoring guidance** that considers system-wide impact

• **Dependency analysis** and identifying potential bottlenecks

• **Code review** and architectural assessment

• **Any task requiring full codebase context** rather than snippet-based analysis

**Example commands**:

* `python3 codeingest.py --instruction "Analyze the authentication flow and identify why sessions are timing out randomly"`

* `python3 codeingest.py --instruction "I need to add caching. Show me existing patterns and suggest where to implement Redis integration"`

* `python3 codeingest.py --instruction "Explain the database schema relationships and how they map to the API endpoints"`
```

---

## How It Works

1. **Repomix Snapshot**: Creates a complete, AI-friendly representation of your codebase
2. **Gemini Analysis**: Sends the entire codebase context to Google's advanced language model
3. **Comprehensive Response**: Returns detailed insights about code structure, dependencies, and architectural patterns
4. **Clean Cleanup**: Automatically removes temporary files

---

**Happy Coding! 🚀**

*This tool is designed to supercharge your development workflow by giving AI agents the full context they need to provide meaningful assistance.*