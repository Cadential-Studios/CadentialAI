"""Test configuration and fixtures for CadentialAI."""

import pytest
import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

@pytest.fixture
def sample_config():
    """Provide a sample configuration for testing."""
    return {
        "api_key": "test_key",
        "model": "gpt-4",
        "timeout": 30,
        "debug": True
    }

@pytest.fixture
def temp_dir(tmp_path):
    """Provide a temporary directory for tests."""
    return tmp_path
