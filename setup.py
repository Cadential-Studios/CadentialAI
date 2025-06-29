#!/usr/bin/env python3
"""Setup script for CadentialAI - Personal Windows AI Assistant."""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="cadentialai",
    version="1.0.0",
    author="CadentialAI Team",
    author_email="your-email@example.com",  # Replace with your email
    description="Personal Windows AI Assistant powered by UFO² framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/CadentialAI",  # Replace with your GitHub URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Desktop Environment",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.4",
            "pytest-cov>=4.1.0",
            "black>=23.12.1",
            "flake8>=7.0.0",
        ],
        "docs": [
            "mkdocs>=1.5.3",
            "mkdocs-material>=9.5.3",
            "mkdocstrings>=0.24.0",
        ],
    },    entry_points={
        "console_scripts": [
            "cadentialai=cadential_ai:main",
        ],
    },
    include_package_data=True,
    package_data={
        "cadentialai": [
            "config/*.yaml",
            "assets/*",
        ],
    },
    keywords="ai assistant windows automation ufo desktop productivity",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/CadentialAI/issues",
        "Source": "https://github.com/yourusername/CadentialAI",
        "Documentation": "https://github.com/yourusername/CadentialAI/docs",
    },
)
