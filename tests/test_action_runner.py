"""
Unit tests for the ActionRunner class.
"""

import pytest
from src.action_runner import ActionRunner


class TestActionRunner:
    """Test cases for ActionRunner class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = ActionRunner()

    def test_initialization(self):
        """Test ActionRunner initialization."""
        assert self.runner.name == "Python GitHub Action Template"
        assert self.runner.version == "1.0.0"

    def test_run_with_valid_inputs(self):
        """Test run method with valid inputs."""
        result = self.runner.run("test_input", "test_input2")

        assert "output1" in result
        assert "output2" in result
        assert result["output1"] == "Processed: TEST_INPUT"
        assert result["output2"] == "Secondary: test_input2"

    def test_run_with_empty_input2(self):
        """Test run method with empty input2."""
        result = self.runner.run("test_input", "")

        assert result["output1"] == "Processed: TEST_INPUT"
        assert result["output2"] == "No secondary input provided"

    def test_run_with_whitespace_input1(self):
        """Test run method with whitespace in input1."""
        result = self.runner.run("  test_input  ", "test_input2")

        assert result["output1"] == "Processed: TEST_INPUT"

    def test_validate_inputs_with_empty_input1(self):
        """Test input validation with empty input1."""
        with pytest.raises(ValueError, match="input1 cannot be empty"):
            self.runner._validate_inputs("", "test_input2")

    def test_validate_inputs_with_whitespace_input1(self):
        """Test input validation with whitespace-only input1."""
        with pytest.raises(ValueError, match="input1 cannot be empty"):
            self.runner._validate_inputs("   ", "test_input2")

    def test_process_input1(self):
        """Test input1 processing."""
        result = self.runner._process_input1("hello world")
        assert result == "HELLO WORLD"

    def test_process_input2(self):
        """Test input2 processing."""
        result = self.runner._process_input2("HELLO WORLD")
        assert result == "hello world"

    def test_process_input2_empty(self):
        """Test input2 processing with empty string."""
        result = self.runner._process_input2("")
        assert result == ""

    def test_generate_output1(self):
        """Test output1 generation."""
        result = self.runner._generate_output1("TEST")
        assert result == "Processed: TEST"

    def test_generate_output2_with_input(self):
        """Test output2 generation with input."""
        result = self.runner._generate_output2("test")
        assert result == "Secondary: test"

    def test_generate_output2_without_input(self):
        """Test output2 generation without input."""
        result = self.runner._generate_output2("")
        assert result == "No secondary input provided"
