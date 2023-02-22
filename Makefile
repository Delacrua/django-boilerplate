migrations:
	cd src && python manage.py makemigrations

migrate:
	cd src && python manage.py migrate

runserver:
	cd src && python manage.py runserver

run-fmt:
	cd src && isort .
	cd src && black .
run-lint:
	flake8 src


local-build:
	docker compose -f docker-compose.local.yml build
local-up:
	docker compose -f docker-compose.local.yml up
local-up-d:
	docker compose -f docker-compose.local.yml up -d
local-down:
	docker compose -f docker-compose.local.yml down
local-run-test:
	docker compose -f docker-compose.local.yml run web sh -c 'pytest'


dev-build:
	docker compose -f docker-compose.dev.yml build
dev-up:
	docker compose -f docker-compose.dev.yml up
dev-up-d:
	docker compose -f docker-compose.dev.yml up -d
dev-down:
	docker compose -f docker-compose.dev.yml down
dev-run-test:
	docker compose -f docker-compose.dev.yml run web sh -c 'pytest'


release-build:
	docker compose -f docker-compose.release.yml build
release-up:
	docker compose -f docker-compose.release.yml up
release-up-d:
	docker compose -f docker-compose.release.yml up -d
release-down:
	docker compose -f docker-compose.release.yml down