.PHONY: help clean sync install test lint format build dist ksyrebuild docs release
.DEFAULT_GOAL := help

PYTHON ?= uv run python

KSY_SOURCES := $(shell find dispersing/ksy_files -name '*.ksy')
COMPILED_KSY := $(subst ksy_files,kaitai_parsers,$(KSY_SOURCES:%.ksy=%.py))

dispersing/kaitai_parsers/%.py : dispersing/ksy_files/%.ksy
	kaitai-struct-compiler --target=python --python-package=dispersing.kaitai_parsers --read-pos --outdir=$(dir $@) $<

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

clean: ## Remove build, test, coverage and Python artifacts
	rm -fr build/ dist/ .venv/ .eggs/ htmlcov/
	rm -f .coverage
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

sync: ## Create the environment and install all dependencies with uv
	uv sync --dev

install: sync ## Install the package (editable) into a uv-managed environment

test: ## Run the test suite
	uv run pytest

lint: ## Lint the code with ruff
	uv run ruff check dispersing tests

format: ## Format the code with ruff
	uv run ruff format dispersing tests

build: ksyrebuild ## Build source and wheel distributions
	uv build

dist: build ## Alias for `build`

ksyrebuild: $(COMPILED_KSY) ## Regenerate Kaitai parsers from .ksy definitions

docs: ## Build the Sphinx documentation
	rm -f docs/dispersing.rst docs/modules.rst
	uv run sphinx-apidoc -o docs/ dispersing
	uv run sphinx-build -b html docs docs/_build/html

release: clean ksyrebuild ## Package and upload a release
	uv publish
