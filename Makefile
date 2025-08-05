.PHONY: help install test lint format clean build

# Default target
help:
	@echo "Available commands:"
	@echo "  install    - Install dependencies"
	@echo "  test       - Run tests"
	@echo "  lint       - Run linting checks"
	@echo "  format     - Format code with black"
	@echo "  clean      - Clean build artifacts"
	@echo "  build      - Build the package"
	@echo "  all        - Run install, format, lint, and test"

# Install dependencies
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .[dev]

# Run tests
test:
	pytest tests/ -v --cov=src --cov-report=term-missing

# Run tests with coverage report
test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

# Run linting
lint:
	flake8 src/ tests/
	mypy src/

# Format code
format:
	black src/ tests/

# Check formatting
check-format:
	black --check src/ tests/

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Build package
build: clean
	python -m build

# Run all checks
all: install format lint test

# Local development setup
dev-setup: install
	@echo "Development environment setup complete!"
	@echo "Run 'make test' to run tests"
	@echo "Run 'make lint' to run linting"
	@echo "Run 'make format' to format code"

# Test action locally
test-action:
	INPUT_INPUT1="test_value" INPUT_INPUT2="optional_value" GITHUB_OUTPUT="/tmp/github_output" python -m src.main
	@echo "Action output:"
	@cat /tmp/github_output || echo "No output file generated" 