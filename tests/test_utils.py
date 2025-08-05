"""
Unit tests for utility functions.
"""

import os
import pytest
from unittest.mock import patch, mock_open
from src.utils import (
    get_input,
    set_output,
    log_info,
    log_warning,
    log_error,
    get_github_context,
    is_github_actions,
)


class TestUtils:
    """Test cases for utility functions."""

    def test_get_input_with_required_input(self):
        """Test get_input with required input that exists."""
        with patch.dict(os.environ, {"INPUT_TEST_INPUT": "test_value"}):
            result = get_input("test_input", required=True)
            assert result == "test_value"

    def test_get_input_with_required_input_missing(self):
        """Test get_input with required input that is missing."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(
                ValueError, match="Required input 'test_input' is missing"
            ):
                get_input("test_input", required=True)

    def test_get_input_with_optional_input(self):
        """Test get_input with optional input."""
        with patch.dict(os.environ, {}, clear=True):
            result = get_input("test_input", required=False, default="default_value")
            assert result == "default_value"

    def test_get_input_case_insensitive(self):
        """Test get_input handles case conversion correctly."""
        with patch.dict(os.environ, {"INPUT_TEST_INPUT": "test_value"}):
            result = get_input("Test_Input", required=True)
            assert result == "test_value"

    def test_set_output_with_github_output_file(self):
        """Test set_output with GITHUB_OUTPUT file."""
        mock_file = mock_open()
        with patch.dict(os.environ, {"GITHUB_OUTPUT": "/tmp/output"}):
            with patch("builtins.open", mock_file):
                set_output("test_output", "test_value")
                mock_file.assert_called_once_with("/tmp/output", "a")
                mock_file().write.assert_called_once_with("test_output=test_value\n")

    def test_set_output_without_github_output_file(self):
        """Test set_output without GITHUB_OUTPUT file (fallback)."""
        with patch.dict(os.environ, {}, clear=True):
            with patch("builtins.print") as mock_print:
                set_output("test_output", "test_value")
                mock_print.assert_called_once_with(
                    "::set-output name=test_output::test_value"
                )

    def test_log_info(self):
        """Test log_info function."""
        with patch("builtins.print") as mock_print:
            log_info("test message")
            mock_print.assert_called_once_with("::info::test message")

    def test_log_warning(self):
        """Test log_warning function."""
        with patch("builtins.print") as mock_print:
            log_warning("test warning")
            mock_print.assert_called_once_with("::warning::test warning")

    def test_log_error(self):
        """Test log_error function."""
        with patch("builtins.print") as mock_print:
            log_error("test error")
            mock_print.assert_called_once_with("::error::test error")

    def test_get_github_context(self):
        """Test get_github_context function."""
        test_env = {
            "GITHUB_EVENT_NAME": "push",
            "GITHUB_REPOSITORY": "owner/repo",
            "GITHUB_REF": "refs/heads/main",
            "GITHUB_SHA": "abc123",
            "GITHUB_WORKFLOW": "test-workflow",
            "GITHUB_RUN_ID": "123456",
            "GITHUB_RUN_NUMBER": "1",
            "GITHUB_ACTOR": "test-user",
            "GITHUB_WORKSPACE": "/workspace",
        }

        with patch.dict(os.environ, test_env):
            context = get_github_context()

            assert context["event_name"] == "push"
            assert context["repository"] == "owner/repo"
            assert context["ref"] == "refs/heads/main"
            assert context["sha"] == "abc123"
            assert context["workflow"] == "test-workflow"
            assert context["run_id"] == "123456"
            assert context["run_number"] == "1"
            assert context["actor"] == "test-user"
            assert context["workspace"] == "/workspace"

    def test_is_github_actions_true(self):
        """Test is_github_actions returns True when GITHUB_ACTIONS is set."""
        with patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}):
            assert is_github_actions() is True

    def test_is_github_actions_false(self):
        """Returns False when GITHUB_ACTIONS is not set."""
        with patch.dict(os.environ, {}, clear=True):
            assert is_github_actions() is False

    def test_is_github_actions_false_when_set_to_false(self):
        """Returns False when GITHUB_ACTIONS is set to 'false'."""
        with patch.dict(os.environ, {"GITHUB_ACTIONS": "false"}):
            assert is_github_actions() is False
