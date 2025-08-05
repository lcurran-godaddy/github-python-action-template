"""
ActionRunner module containing the main business logic for the GitHub Action.
"""

from typing import Dict, Any, Optional
from .utils import log_info, log_warning, log_error


class ActionRunner:
    """
    Main class that handles the execution of the GitHub Action.
    """
    
    def __init__(self):
        """Initialize the ActionRunner."""
        self.name = "Python GitHub Action Template"
        self.version = "1.0.0"
    
    def run(self, input1: str, input2: str = "") -> Dict[str, Any]:
        """
        Execute the main action logic.
        
        Args:
            input1: Required input parameter
            input2: Optional input parameter
            
        Returns:
            Dictionary containing the output values
        """
        log_info(f"Running {self.name} v{self.version}")
        
        # Validate inputs
        self._validate_inputs(input1, input2)
        
        # Process the inputs
        processed_input1 = self._process_input1(input1)
        processed_input2 = self._process_input2(input2)
        
        # Generate outputs
        output1 = self._generate_output1(processed_input1)
        output2 = self._generate_output2(processed_input2)
        
        log_info("Action processing completed")
        
        return {
            "output1": output1,
            "output2": output2
        }
    
    def _validate_inputs(self, input1: str, input2: str) -> None:
        """
        Validate the input parameters.
        
        Args:
            input1: First input parameter
            input2: Second input parameter
            
        Raises:
            ValueError: If inputs are invalid
        """
        if not input1 or not input1.strip():
            raise ValueError("input1 cannot be empty")
        
        log_info("Input validation passed")
    
    def _process_input1(self, input1: str) -> str:
        """
        Process the first input parameter.
        
        Args:
            input1: Raw input value
            
        Returns:
            Processed input value
        """
        # Add your custom processing logic here
        processed = input1.strip().upper()
        log_info(f"Processed input1: {input1} -> {processed}")
        return processed
    
    def _process_input2(self, input2: str) -> str:
        """
        Process the second input parameter.
        
        Args:
            input2: Raw input value
            
        Returns:
            Processed input value
        """
        # Add your custom processing logic here
        processed = input2.strip().lower() if input2 else ""
        if processed:
            log_info(f"Processed input2: {input2} -> {processed}")
        return processed
    
    def _generate_output1(self, processed_input1: str) -> str:
        """
        Generate the first output based on processed input1.
        
        Args:
            processed_input1: Processed first input
            
        Returns:
            Generated output value
        """
        # Add your custom output generation logic here
        output = f"Processed: {processed_input1}"
        log_info(f"Generated output1: {output}")
        return output
    
    def _generate_output2(self, processed_input2: str) -> str:
        """
        Generate the second output based on processed input2.
        
        Args:
            processed_input2: Processed second input
            
        Returns:
            Generated output value
        """
        # Add your custom output generation logic here
        if processed_input2:
            output = f"Secondary: {processed_input2}"
        else:
            output = "No secondary input provided"
        
        log_info(f"Generated output2: {output}")
        return output 