install:
	pip install "poetry>=1.1.12"
	poetry install --remove-untracked

setup: start-db
	make install
	poetry run python scripts/setup_db.py

format:
	poetry run black bibliarius/
	poetry run black tests/
	poetry run black scripts/

lint:
	poetry run black --check bibliarius/
	poetry run mypy bibliarius/
	poetry run pylint bibliarius/
	poetry run black --check tests/
	poetry run black --check scripts/
	poetry run pylint scripts/

test:
	poetry run pytest

ci: install lint test

start-db:
	docker run --rm --name bibliarius-postgres \
 		-p 5432:5432 \
 		-e POSTGRES_USER=pblubbs \
		-e POSTGRES_PASSWORD=muppetverseofmadness \
		-e POSTGRES_DB=bibliarius \
		-d postgres:14-alpine

stop-db:
	docker stop bibliarius-postgres
