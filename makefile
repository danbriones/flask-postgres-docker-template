# Variables
COMPOSE=docker compose
WEB_SERVICE=web

.PHONY: run stop build migrate upgrade shell clean

# Start the environment
run:
	$(COMPOSE) up

# Build and start
build:
	$(COMPOSE) up --build

# Stop the environment
stop:
	$(COMPOSE) down

# Initialize migrations (Run once at start of project)
init-db:
	$(COMPOSE) exec $(WEB_SERVICE) flask db init

# Generate a migration script (Usage: make migrate msg="add user bio")
migrate:
	$(COMPOSE) exec $(WEB_SERVICE) flask db migrate -m "$(msg)"

# Apply migrations to the database
upgrade:
	$(COMPOSE) exec $(WEB_SERVICE) flask db upgrade

# Open a shell inside the Flask container
shell:
	$(COMPOSE) exec $(WEB_SERVICE) /bin/bash

# Remove dangling docker images and volumes
clean:
	$(COMPOSE) down -v
	docker system prune -f

test:
	$(COMPOSE) exec $(WEB_SERVICE) pytest tests/

test-isolated:
	docker compose -f docker-compose.test.yml up --abort-on-container-exit --exit-code-from test_web
	docker compose -f docker-compose.test.yml down