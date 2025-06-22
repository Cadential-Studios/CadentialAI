"""Basic tests for CadentialAI functionality."""

import unittest
import os
import sys

class TestBasicFunctionality(unittest.TestCase):
    """Test basic CadentialAI functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_config = {
            "api_key": "test_key",
            "model": "gpt-4",
            "timeout": 30
        }

    def test_config_loading(self):
        """Test configuration loading."""
        self.assertIsInstance(self.test_config, dict)
        self.assertIn("api_key", self.test_config)

    def test_project_structure(self):
        """Test that required project files exist."""
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        required_files = [
            "README.md",
            "requirements.txt",
            "LICENSE",
            ".gitignore"
        ]
        
        for file_name in required_files:
            file_path = os.path.join(project_root, file_name)
            self.assertTrue(os.path.exists(file_path), f"Required file {file_name} not found")

if __name__ == "__main__":
    unittest.main()
