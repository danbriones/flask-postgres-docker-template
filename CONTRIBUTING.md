# Contributing to Flask Docker Stack

This project is optimized for an **AI-First Workflow**, specifically tailored for **GitHub Copilot Free** users. Please follow these guidelines to maintain high development velocity and token efficiency.

---

## 🤖 Working with AI (Copilot/Claude)

To keep development efficient and stay within [GitHub Copilot Free limits](https://github.com/settings/copilot/features):

### 1. Use the Instruction File
Before starting, ensure your editor is reading `.github/copilot-instructions.md`. This file contains the project's "memory" regarding:
- **Tech Stack:** Flask, Postgres, Docker.
- **UI Framework:** Bootstrap 5.
- **Database:** UUIDs for Primary Keys.
- **Standards:** Python type hinting and Google-style docstrings.

### 2. Context-Aware Prompting
Always use the `#` symbol in Copilot Chat to provide specific file context.
- **Correct:** "Add a field to #models.py"
- **Incorrect:** "Add a field to my database model."

### 3. Prefer Ghost Text over Chat
Since [Code Completions](https://github.com/settings/copilot/features) do not count toward your monthly chat limit, try to "nudge" the AI by writing comments or function headers and letting it provide the gray "ghost text" suggestions.

---

## 🛠 Development Workflow

### Shortcuts (The Makefile)
Avoid asking the AI for terminal commands. Use the provided `Makefile`:
- `make run`: Start the dev environment.
- `make migrate msg="your change"`: Generate a migration.
- `make upgrade`: Sync the database.
- `make test`: Run the pytest suite.

### Database Changes
1. Update the model in `app.py`.
2. Run `make migrate msg="description"`.
3. Run `make upgrade`.
4. Verify changes in the `web` container.

---

## 🧪 Testing
All new features should include a test case in `tests/test_basic.py`. You can run an isolated test environment (mimicking CI/CD) using:
```bash
make test-isolated