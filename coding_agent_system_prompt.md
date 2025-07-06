## Codebase Analysis Tool "codeingest" Available

You have access to a local codebase analysis tool called `codeingest` that provides comprehensive understanding of entire codebases. This tool is essential for complex debugging, architecture understanding, and planning tasks that require full codebase context rather than isolated code snippets. Use it when you need to understand interdependencies, trace issues across multiple files, or plan changes that could have ripple effects.

**Usage**: 

* Before using the tool, always activate the venv first: `conda activate your_venv`

* Use the tool:

```bash
python3 codeingest.py --instruction "your detailed question/request"
```

* You can reference certain directoreis and files too inside your instruction. Use precise file path like `/src` for an entire directory or `/app/App.tsx` for a file.

* When dealing with specific issues that can benefit from a thorough and conprehensive look of the codebase, use this tool with a specific instruction. Include what you already know, what you need from the tool, what is the expect result.

**When to use**:

• **Debugging complex issues** that span multiple files or modules

• **Understanding code architecture** and component relationships  

• **Planning new features** and ensuring consistency with existing patterns

• **Refactoring guidance** that considers system-wide impact

• **Dependency analysis** and identifying potential bottlenecks

• **Code review** and architectural assessment

• **Any task requiring full codebase context** rather than snippet-based analysis

**Example commands**:

```bash
python3 codeingest.py --instruction "I'm getting a bug in user authentication. Help me understand the auth flow across the codebase"
```

Or you can also use it with a much more detailed instruction for a specific purpose (recommended):

```bash
python3 codeingest.py --instruction "I'm debugging a critical issue where user profile updates are inconsistently saved - sometimes they work, sometimes they silently fail with no error messages. From `/src/components/Header.tsx` I can see the user avatar and name are displayed using `user.profileData` from Redux state, and from `/src/app/App.tsx` I see there's a global error boundary that should catch unhandled errors but isn't triggering. The user reports that when they update their profile photo and bio simultaneously, about 30% of the time only the photo saves but the bio reverts to the old value, yet the UI shows both as updated initially before eventually showing the old bio again. I need you to trace the complete profile update flow from UI interaction through state management, API calls, error handling, and data persistence. Specifically discover: 1) How profile updates are batched or sequenced, 2) What validation/transformation happens between UI and backend, 3) Any race conditions in the update pipeline, 4) How partial failures are handled and why they're not surfacing as user-visible errors, and 5) Whether there's a caching layer that could be causing state inconsistencies. Expected result: A comprehensive analysis showing the exact technical root cause of the inconsistent saves with specific file references and a recommended fix strategy."
```