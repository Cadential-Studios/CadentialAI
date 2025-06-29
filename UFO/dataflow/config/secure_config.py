# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
import yaml
from pathlib import Path


def load_env_file(env_path: str) -> dict:
    """
    Load environment variables from a .env file.
    
    :param env_path: Path to the .env file
    :return: Dictionary of environment variables
    """
    env_vars = {}
    
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Remove quotes if present
                    if (value.startswith('"') and value.endswith('"')) or \
                       (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1]
                    
                    env_vars[key] = value
    
    return env_vars


def get_config_from_env(agent_prefix: str = "") -> dict:
    """
    Extract configuration from environment variables for a specific agent.
    
    :param agent_prefix: Prefix for agent-specific env vars (e.g., "PREFILL_AGENT_", "FILTER_AGENT_")
    :return: Configuration dictionary
    """
    config = {}
    
    # Define mapping from env var suffixes to config keys
    env_mappings = {
        "API_KEY": "API_KEY",
        "API_BASE": "API_BASE", 
        "API_TYPE": "API_TYPE",
        "API_MODEL": "API_MODEL",
        "API_VERSION": "API_VERSION",
        "API_DEPLOYMENT_ID": "API_DEPLOYMENT_ID",
        "VISUAL_MODE": "VISUAL_MODE",
        "AAD_TENANT_ID": "AAD_TENANT_ID",
        "AAD_API_SCOPE": "AAD_API_SCOPE",
        "AAD_API_SCOPE_BASE": "AAD_API_SCOPE_BASE"
    }
    
    # Check for agent-specific environment variables first
    if agent_prefix:
        for env_suffix, config_key in env_mappings.items():
            env_var = f"{agent_prefix}{env_suffix}"
            if env_var in os.environ:
                value = os.environ[env_var]
                
                # Convert string boolean values
                if env_suffix == "VISUAL_MODE":
                    value = value.lower() in ('true', '1', 'yes', 'on')
                
                config[config_key] = value
    
    # Fallback to generic environment variables (without agent prefix)
    for env_suffix, config_key in env_mappings.items():
        if config_key not in config:  # Only if not already set by agent-specific var
            generic_vars = [
                env_suffix,  # Direct mapping
                f"OPENAI_{env_suffix}",  # OpenAI prefix
                f"AZURE_{env_suffix}",  # Azure prefix
            ]
            
            for var_name in generic_vars:
                if var_name in os.environ:
                    value = os.environ[var_name]
                    
                    # Convert string boolean values
                    if env_suffix == "VISUAL_MODE":
                        value = value.lower() in ('true', '1', 'yes', 'on')
                    
                    config[config_key] = value
                    break
    
    return config


def load_secure_config(config_dir: str = "dataflow/config/") -> dict:
    """
    Load configuration with secure API key management.
    Priorities (highest to lowest):
    1. Environment variables 
    2. .env file in config directory
    3. .env file in parent directory
    4. YAML config files
    
    :param config_dir: Directory containing config files
    :return: Complete configuration dictionary
    """
    config_path = Path(config_dir)
    config = {}
    
    # Load from .env files (lower priority)
    env_files = [
        config_path / ".env",
        config_path.parent / ".env", 
        Path(".env")
    ]
    
    for env_file in env_files:
        if env_file.exists():
            env_vars = load_env_file(str(env_file))
            # Set env vars in os.environ so they can be picked up later
            for key, value in env_vars.items():
                if key not in os.environ:  # Don't override existing env vars
                    os.environ[key] = value
    
    # Load YAML config files if they exist
    yaml_files = [
        config_path / "config.yaml",
        config_path / "config_dev.yaml", 
        config_path / "config_prices.yaml"
    ]
    
    for yaml_file in yaml_files:
        if yaml_file.exists():
            try:
                with open(yaml_file, 'r', encoding='utf-8') as file:
                    yaml_data = yaml.safe_load(file)
                    if yaml_data:
                        config.update(yaml_data)
            except Exception as e:
                print(f"Warning: Could not load {yaml_file}: {e}")
    
    # Override with environment variables (highest priority)
    # Update agent configurations with environment variables
    agents = ["PREFILL_AGENT", "FILTER_AGENT", "HOST_AGENT", "APP_AGENT", "BACKUP_AGENT"]
    
    for agent in agents:
        if agent in config or any(key.startswith(f"{agent}_") for key in os.environ):
            env_config = get_config_from_env(f"{agent}_")
            
            if env_config:
                if agent not in config:
                    config[agent] = {}
                config[agent].update(env_config)
    
    # Add global parameters from environment
    global_params = {
        "MAX_TOKENS": "MAX_TOKENS",
        "MAX_RETRY": "MAX_RETRY", 
        "TEMPERATURE": "TEMPERATURE",
        "TOP_P": "TOP_P",
        "TIMEOUT": "TIMEOUT"
    }
    
    for env_key, config_key in global_params.items():
        if env_key in os.environ:
            try:
                value = os.environ[env_key]
                # Convert numeric values
                if env_key in ["MAX_TOKENS", "MAX_RETRY", "TIMEOUT"]:
                    value = int(value)
                elif env_key in ["TEMPERATURE", "TOP_P"]:
                    value = float(value)
                config[config_key] = value
            except ValueError:
                print(f"Warning: Invalid value for {env_key}: {os.environ[env_key]}")
    
    return config
