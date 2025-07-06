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

3. Set up the system prompt for your coding tool (like Cursor or Claude Code) with the provided system prompt in [Cursor System Prompt](coding_agent_system_prompt.md).

---

## How It Works

1. **Repomix Snapshot**: Creates a complete, AI-friendly representation of your codebase
2. **Gemini Analysis**: Sends the entire codebase context to Google's advanced language model
3. **Comprehensive Response**: Returns detailed insights about code structure, dependencies, and architectural patterns
4. **Clean Cleanup**: Automatically removes temporary files

---

**Happy Coding! 🚀**

*This tool is designed to supercharge your development workflow by giving AI agents the full context they need to provide meaningful assistance.*