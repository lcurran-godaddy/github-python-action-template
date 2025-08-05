"""
Utility functions for GitHub Actions integration.
"""

import os
import sys
from typing import Optional


def get_input(name: str, required: bool = False, default: str = "") -> str:
    """
    Get an input value from GitHub Actions.
    
    Args:
        name: Name of the input parameter
        required: Whether the input is required
        default: Default value if input is not provided
        
    Returns:
        The input value
        
    Raises:
        ValueError: If required input is missing
    """
    # GitHub Actions sets inputs as environment variables with INPUT_ prefix
    env_name = f"INPUT_{name.upper()}"
    value = os.environ.get(env_name, default)
    
    if required and not value:
        raise ValueError(f"Required input '{name}' is missing")
    
    return value


def set_output(name: str, value: str) -> None:
    """
    Set an output value for GitHub Actions.
    
    Args:
        name: Name of the output parameter
        value: Value to set
    """
    # GitHub Actions outputs are set by writing to a special file
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{name}={value}\n")
    else:
        # Fallback for local development
        print(f"::set-output name={name}::{value}")


def log_info(message: str) -> None:
    """
    Log an info message in GitHub Actions format.
    
    Args:
        message: Message to log
    """
    print(f"::info::{message}")


def log_warning(message: str) -> None:
    """
    Log a warning message in GitHub Actions format.
    
    Args:
        message: Message to log
    """
    print(f"::warning::{message}")


def log_error(message: str) -> None:
    """
    Log an error message in GitHub Actions format.
    
    Args:
        message: Message to log
    """
    print(f"::error::{message}")


def get_github_context() -> dict:
    """
    Get GitHub context information from environment variables.
    
    Returns:
        Dictionary containing GitHub context information
    """
    return {
        "event_name": os.environ.get("GITHUB_EVENT_NAME"),
        "event_path": os.environ.get("GITHUB_EVENT_PATH"),
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "ref": os.environ.get("GITHUB_REF"),
        "sha": os.environ.get("GITHUB_SHA"),
        "workflow": os.environ.get("GITHUB_WORKFLOW"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_number": os.environ.get("GITHUB_RUN_NUMBER"),
        "actor": os.environ.get("GITHUB_ACTOR"),
        "workspace": os.environ.get("GITHUB_WORKSPACE"),
    }


def is_github_actions() -> bool:
    """
    Check if the code is running in GitHub Actions.
    
    Returns:
        True if running in GitHub Actions, False otherwise
    """
    return os.environ.get("GITHUB_ACTIONS") == "true" 