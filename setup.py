#!/usr/bin/env python3
"""Setup script for QuickBin."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="quickbin-cli",
    version="1.0.0",
    author="QuickBin Team",
    author_email="hello@quickbin.dev",
    description="A lightweight CLI tool for sharing code snippets instantly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitstq/quickbin",
    py_modules=["quickbin"],
    install_requires=[
        "click>=8.0.0",
        "requests>=2.28.0",
        "rich>=13.0.0",
        "pyperclip>=1.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "quickbin=quickbin:cli",
            "qb=quickbin:cli",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Environment :: Console",
        "Natural Language :: English",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Chinese (Traditional)",
    ],
    python_requires=">=3.8",
    keywords="code snippet share paste bin gist cli developer tool",
    project_urls={
        "Bug Reports": "https://github.com/gitstq/quickbin/issues",
        "Source": "https://github.com/gitstq/quickbin",
        "Documentation": "https://github.com/gitstq/quickbin#readme",
    },
)
