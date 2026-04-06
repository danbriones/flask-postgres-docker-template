This README.md serves as the "source of truth" for your project. By keeping this file updated, you ensure that any AI tool (Copilot, Claude, or ChatGPT) can immediately understand your architecture, saving you from repetitive prompting and wasting your monthly free message limits.

README.md
Markdown
# Flask + Postgres + Docker Stack

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)

A streamlined development environment for a Python-based web application, optimized for use with GitHub Copilot and VS Code.

**Repository**: [https://github.com/danbriones/flask-postgres-docker-template](https://github.com/danbriones/flask-postgres-docker-template)

## 🚀 Quick Start

1. **Build and Start:**

   ```bash
   docker compose up --build

Initialize Database:

Bash
docker compose exec web flask db init
docker compose exec web flask db migrate -m "Initial migration"
docker compose exec web flask db upgrade
Access the App:

Web UI: http://localhost:5000

Postgres: localhost:5432

🛠 Tech Stack
Backend: Python 3.12, Flask

Database: PostgreSQL 16

ORM: Flask-SQLAlchemy (using UUIDs for Primary Keys)

Migrations: Flask-Migrate (Alembic)

Frontend: Bootstrap 5 (via CDN)

Orchestration: Docker Compose

📂 Project Structure
.github/copilot-instructions.md: Custom instructions to keep AI coding aligned with project standards.

app.py: Flask application entry point and database models.

templates/: Jinja2 HTML templates using Bootstrap.

Dockerfile: Multi-stage build for a secure, lightweight image.

docker-compose.yml: Orchestration for the web and db services.

🤖 AI Assistance & Efficiency
This project is configured to work efficiently with the GitHub Copilot Free tier.

Custom Instructions
To maintain the coding style (UUIDs, Bootstrap, Type Hinting) without wasting chat tokens:

Ensure .github/copilot-instructions.md is present in the root.

If using VS Code, check "Chat: Use Claude Md File" in settings to allow Copilot to read project-wide rules.

Database Migrations
Always run migrations through the Docker container to ensure the Postgres schema stays in sync:

Bash
docker compose exec web flask db migrate -m "description_of_change"
docker compose exec web flask db upgrade
🔒 Security & Environment
Non-Root User: The Docker container runs as flaskuser.

Environment Variables: All secrets (DB credentials, Secret Keys) are managed via .env or Docker environment blocks. Never hardcode credentials in app.py.


---

### One Final Tip for your Copilot Limit
Since you have **12 days** until your [Free responses reset](https://github.com/settings/copilot/features), I recommend using **Inline Chat** (`Cmd+I` or `Ctrl+I`) for small code fixes instead of the big Chat Sidebar. It often uses fewer resources and keeps your workflow faster!

**Would you like me to create a `.gitignore` file to ensure you don't accidentally commit your Docker volumes or `__pycache__` folders?**