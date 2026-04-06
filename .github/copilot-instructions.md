# Project Context: Flask + Postgres + Docker + Bootstrap

## Tech Stack
- **Backend:** Python 3.12+ using Flask (Strictly Flask-SQLAlchemy for ORM).
- **Database:** PostgreSQL. All migrations must use Flask-Migrate.
- **Frontend:** Simple Web UI using **Bootstrap 5** (via CDN for simplicity).
- **Environment:** Running inside Docker with `docker-compose`.

## UI/UX Standards (Bootstrap)
- **Grid System:** Use Bootstrap's container-row-column system for all layouts.
- **Components:** Prioritize standard Bootstrap components (Cards, Navbars, Modals).
- **Forms:** Use `form-control` and `form-label` classes for all input fields.
- **Styling:** Keep custom CSS to a minimum; override via a single `style.css` if necessary.

## Backend Coding Standards
- **Type Hinting:** Always include Python type hints for arguments and return types.
- **Security:** Use `os.getenv` for secrets. Never hardcode database credentials.
- **Models:** Use `UUID` as the primary key for all SQLAlchemy models.

## Docker Guidelines
- Use multi-stage builds in the `Dockerfile`.
- Always define a non-root user for the Flask application process.