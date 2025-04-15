install:
	uv sync

build:
	uv build

lint:
	uvx ruff check --config ruff.toml

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml