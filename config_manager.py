"""
Configuration loader for CadentialAI
Handles secure loading of API keys and settings
"""

import os
import shutil
import yaml
from pathlib import Path
from typing import Dict, Any, Optional

class ConfigManager:
    """Manages configuration loading with fallback to environment variables."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.project_root = Path(__file__).parent
        self.config_path = Path(config_path) if config_path else self.project_root / "config.yaml"
        self.template_path = self.project_root / "config.template.yaml"
        self._config = None
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file with environment variable fallbacks."""
        if self._config is not None:
            return self._config
        
        # Try to load from config.yaml
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._config = yaml.safe_load(f)
        else:
            # Create from template if config doesn't exist
            self._create_config_from_template()
            print(f"⚠️  Created {self.config_path} from template. Please add your API keys!")
            self._config = {}
        
        # Fallback to environment variables
        self._load_env_fallbacks()
        
        return self._config
    
    def _create_config_from_template(self):
        """Create config.yaml from template if it doesn't exist."""
        if self.template_path.exists():
            import shutil
            shutil.copy2(self.template_path, self.config_path)
            print(f"📋 Config template copied to {self.config_path}")
    
    def _load_env_fallbacks(self):
        """Load configuration from environment variables as fallback."""
        env_mappings = {
            # API Keys
            'OPENAI_API_KEY': ['OPENAI', 'API_KEY'],
            'AZURE_OPENAI_API_KEY': ['AZURE_OPENAI', 'API_KEY'],
            'AZURE_OPENAI_ENDPOINT': ['AZURE_OPENAI', 'API_BASE'],
            'AZURE_SPEECH_KEY': ['AZURE_SPEECH', 'API_KEY'],
            'AZURE_SPEECH_REGION': ['AZURE_SPEECH', 'REGION'],
            
            # Personal Settings
            'USER_NAME': ['USER_SETTINGS', 'NAME'],
            'PREFERRED_VOICE': ['USER_SETTINGS', 'VOICE'],
            'WORKSPACE_PATH': ['USER_SETTINGS', 'WORKSPACE'],
            
            # Application Settings
            'DEBUG_MODE': ['APP_SETTINGS', 'DEBUG'],
            'LOG_LEVEL': ['APP_SETTINGS', 'LOG_LEVEL'],
            'AUTO_SAVE': ['APP_SETTINGS', 'AUTO_SAVE'],
            
            # UFO Settings
            'UFO_VISUAL_MODE': ['UFO_CONFIG', 'VISUAL_MODE'],
            'UFO_MODEL': ['UFO_CONFIG', 'MODEL'],
            
            # Example: Add new variables here
            # 'MY_NEW_VAR': ['SECTION_NAME', 'VARIABLE_NAME'],
            # 'API_TIMEOUT': ['APP_SETTINGS', 'TIMEOUT'],
            # 'MAX_RETRIES': ['APP_SETTINGS', 'MAX_RETRIES'],
        }
        
        # Ensure self._config is initialized as a dictionary
        if self._config is None:
            self._config = {}

        for env_var, config_path in env_mappings.items():
            value = os.getenv(env_var)
            if value:
                # Create nested structure if needed
                current = self._config
                for key in config_path[:-1]:
                    if isinstance(current, dict) and key not in current:
                        current[key] = {}
                    current = current[key]
                current[config_path[-1]] = value
    
    def get_openai_config(self) -> Dict[str, str]:
        """Get OpenAI configuration."""
        config = self.load_config()
        openai_config = config.get('OPENAI', {})
        
        if not openai_config.get('API_KEY'):
            raise ValueError("OpenAI API key not found in config.yaml or environment variables")
        
        return openai_config
    
    def get_azure_openai_config(self) -> Dict[str, str]:
        """Get Azure OpenAI configuration."""
        config = self.load_config()
        azure_config = config.get('AZURE_OPENAI', {})
        
        if not azure_config.get('API_KEY'):
            raise ValueError("Azure OpenAI API key not found in config.yaml or environment variables")
        
        return azure_config
    
    def get_speech_config(self) -> Dict[str, str]:
        """Get Azure Speech configuration."""
        config = self.load_config()
        return config.get('AZURE_SPEECH', {})
    
    def get_user_settings(self) -> Dict[str, Any]:
        """Get CadentialAI user settings."""
        config = self.load_config()
        return config.get('CADENTIAL_AI', {})

# Global config manager instance
config_manager = ConfigManager()

def get_config() -> Dict[str, Any]:
    """Get the global configuration."""
    return config_manager.load_config()

def get_openai_key() -> str:
    """Get OpenAI API key."""
    return config_manager.get_openai_config()['API_KEY']

def get_azure_openai_key() -> str:
    """Get Azure OpenAI API key."""
    return config_manager.get_azure_openai_config()['API_KEY']

# Global instance for easy import
config_manager = ConfigManager()
