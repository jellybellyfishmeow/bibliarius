install:
	poetry install --remove-untracked

setup:
	pip install "poetry>=1.1.12"
	make install

format:
	poetry run black bibliarius/
	poetry run black tests/

lint:
	poetry run black --check bibliarius/
	poetry run mypy bibliarius/
	poetry run pylint bibliarius/
	poetry run black --check tests/

test:
	poetry run pytest

ci: install lint test
