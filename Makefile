.PHONY: all
all: lint test

.PHONY: lint
lint: .venv
	poetry run mypy protocol_lib tests
	poetry run flake8 protocol_lib tests
	poetry run isort --check-only --profile black protocol_lib tests
	poetry run black --check --diff protocol_lib tests

.PHONY: fmt
fmt: .venv
	poetry run isort --profile black protocol_lib tests
	poetry run black protocol_lib tests

.PHONY: test
test: .venv
	poetry run pytest --verbose --capture=no

.PHONY: publish
publish: dist
	poetry publish

.PHONY: dist
dist: dist/protocol-lib-0.3.0.tar.gz dist/protocol_lib-0.3.0-py3-none-any.whl

dist/protocol-lib-0.3.0.tar.gz dist/protocol_lib-0.3.0-py3-none-any.whl: $(shell find protocol_lib -type f -name '*.py')
	poetry build

.venv: poetry.lock
	poetry install
	@touch -c .venv

poetry.lock: pyproject.toml
	poetry lock
	@touch -c poetry.lock
