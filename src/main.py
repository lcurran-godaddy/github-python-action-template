#!/usr/bin/env python3
"""
Main module for the Python GitHub Action Template.
This module contains the core logic for the GitHub Action.
"""

import os
import sys
from typing import Dict, Any, Optional
from .action_runner import ActionRunner
from .utils import get_input, set_output, log_info, log_warning, log_error


def main() -> None:
    """
    Main entry point for the GitHub Action.
    """
    try:
        # Initialize the action runner
        runner = ActionRunner()
        
        # Get inputs from GitHub Actions
        input1 = get_input("input1", required=True)
        input2 = get_input("input2", required=False, default="")
        
        log_info(f"Starting action with input1: {input1}, input2: {input2}")
        
        # Execute the main action logic
        result = runner.run(input1=input1, input2=input2)
        
        # Set outputs
        set_output("output1", result.get("output1", ""))
        set_output("output2", result.get("output2", ""))
        
        log_info("Action completed successfully")
        
    except Exception as e:
        log_error(f"Action failed with error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main() 