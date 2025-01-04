import os
from typing import Dict, Optional


def load_env_file(env_file_path: str) -> Dict[str, str]:
    env_variables = {}

    # Read the file and populate the dictionary
    with open(env_file_path, "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line and "=" in line:  # Skip empty lines or invalid lines
                key, value = line.split("=", 1)  # Split by the first '='
                env_variables[key] = value
                
    return env_variables