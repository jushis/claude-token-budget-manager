
# Claude Token Budget Manager & Context Trimmer

An open-source utility designed to optimize large codebases for LLM context windows, specifically tailored for Anthropic's Claude models. 

## Features
* **Token Efficiency**: Recursively strips non-essential files, empty spaces, and temporary directories.
* **Smart Filtering**: Automatically ignores heavy folders like `node_modules`, `.git`, `venv`, and binary media assets.
* **Single Payload Production**: Combines all text-based source files into a formatted `ai_ready_context.txt` file, making it seamless to copy-paste into Claude.

## Installation & Usage

```bash
git clone https://github.com/jushis
cd claude-token-budget-manager
python trimmer.py /path/to/your/project
```

## Ecosystem Impact Track Note
This repository serves as critical infrastructure for indie developers and micro-teams working under tight Anthropic API token budgets. By compressing source code structures, it maximizes the reasoning capabilities of Claude Sonnet/Opus without wasting prompt capacity on build artifacts.
