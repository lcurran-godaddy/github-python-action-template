# Python GitHub Action Template

A comprehensive template for creating Python-based GitHub Actions with proper structure, testing, and documentation.

## Features

- 🐍 **Python-based**: Written in Python 3.11+ with type hints
- 🧪 **Tested**: Comprehensive unit tests with pytest
- 📦 **Well-structured**: Modular design with clear separation of concerns
- 🔧 **Configurable**: Easy to customize inputs and outputs
- 📚 **Documented**: Complete documentation and examples
- 🛠️ **Development-ready**: Includes linting, formatting, and CI/CD setup

## Quick Start

### 1. Clone and Customize

```bash
git clone <your-repo-url>
cd github-python-action-template
```

### 2. Update the Action

1. **Modify `action.yml`**: Update the action name, description, and inputs/outputs
2. **Customize `src/action_runner.py`**: Implement your business logic
3. **Update `requirements.txt`**: Add your dependencies
4. **Modify tests**: Update tests to match your logic

### 3. Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run linting
flake8 src/ tests/
black src/ tests/
mypy src/
```

### 4. Use in Workflows

```yaml
name: Example Workflow
on: [push, pull_request]

jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Python Action
        uses: ./
        with:
          input1: "Hello World"
          input2: "Optional input"
        id: action-step
        
      - name: Use outputs
        run: |
          echo "Output 1: ${{ steps.action-step.outputs.output1 }}"
          echo "Output 2: ${{ steps.action-step.outputs.output2 }}"
```

## Project Structure

```
github-python-action-template/
├── action.yml              # Action metadata and configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .github/               # GitHub-specific files
│   └── workflows/         # CI/CD workflows
├── src/                   # Source code
│   ├── __init__.py
│   ├── main.py           # Main entry point
│   ├── action_runner.py  # Core business logic
│   └── utils.py          # Utility functions
└── tests/                # Test files
    ├── __init__.py
    ├── test_action_runner.py
    └── test_utils.py
```

## Configuration

### Inputs

| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `input1` | Yes | `default_value` | First input parameter |
| `input2` | No | `""` | Second input parameter (optional) |

### Outputs

| Output | Description |
|--------|-------------|
| `output1` | First output value |
| `output2` | Second output value |

## Development

### Prerequisites

- Python 3.11+
- pip
- pytest (for testing)

### Setup Development Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd github-python-action-template

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_action_runner.py

# Run tests with verbose output
pytest -v
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

### Local Testing

To test the action locally without GitHub Actions:

```bash
# Set environment variables to simulate GitHub Actions
export INPUT_INPUT1="test_value"
export INPUT_INPUT2="optional_value"
export GITHUB_OUTPUT="/tmp/github_output"

# Run the action
python -m src.main
```

## Customization Guide

### Adding New Inputs

1. **Update `action.yml`**:
   ```yaml
   inputs:
     new_input:
       description: 'Description of new input'
       required: false
       default: 'default_value'
   ```

2. **Update `src/main.py`**:
   ```python
   new_input = get_input("new_input", required=False, default="default_value")
   ```

3. **Update `src/action_runner.py`**:
   ```python
   def run(self, input1: str, input2: str = "", new_input: str = "") -> Dict[str, Any]:
       # Use new_input in your logic
   ```

### Adding New Outputs

1. **Update `action.yml`**:
   ```yaml
   outputs:
     new_output:
       description: 'Description of new output'
   ```

2. **Update `src/main.py`**:
   ```python
   set_output("new_output", result.get("new_output", ""))
   ```

3. **Update `src/action_runner.py`**:
   ```python
   return {
       "output1": output1,
       "output2": output2,
       "new_output": new_output
   }
   ```

### Implementing Custom Logic

The main business logic should be implemented in `src/action_runner.py`. The `ActionRunner` class provides a clean interface for:

- Input validation
- Data processing
- Output generation
- Error handling

## Best Practices

### Error Handling

- Always validate inputs
- Use descriptive error messages
- Handle exceptions gracefully
- Log important events

### Logging

Use the provided logging functions:

```python
from src.utils import log_info, log_warning, log_error

log_info("Processing started")
log_warning("Input validation warning")
log_error("Critical error occurred")
```

### Testing

- Write tests for all public methods
- Test edge cases and error conditions
- Use mocking for external dependencies
- Maintain good test coverage

### Security

- Never log sensitive information
- Validate all inputs
- Use environment variables for secrets
- Follow the principle of least privilege

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This template is provided under the MIT License. See the LICENSE file for details.

## Support

For issues and questions:

1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## Changelog

### Version 1.0.0
- Initial release
- Basic action structure
- Comprehensive testing
- Documentation 