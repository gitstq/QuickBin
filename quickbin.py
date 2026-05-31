#!/usr/bin/env python3
"""
QuickBin - A lightweight CLI tool for sharing code snippets instantly.

QuickBin allows developers to quickly upload code snippets and get shareable links.
It supports syntax highlighting, expiration settings, and local history management.
"""

import os
import sys
import json
import time
import hashlib
import base64
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, List
from urllib.parse import urlencode

import click
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich import box


console = Console()

# Default configuration
DEFAULT_CONFIG = {
    "default_expiration": "7d",
    "default_language": "text",
    "auto_copy": True,
    "history_limit": 100,
    "api_endpoint": "https://api.github.com/gists",
}

CONFIG_DIR = Path.home() / ".config" / "quickbin"
CONFIG_FILE = CONFIG_DIR / "config.json"
HISTORY_FILE = CONFIG_DIR / "history.json"


class QuickBinConfig:
    """Manages QuickBin configuration."""

    def __init__(self):
        self.config = self.load_config()

    def load_config(self) -> Dict:
        """Load configuration from file or create default."""
        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    return {**DEFAULT_CONFIG, **json.load(f)}
            except (json.JSONDecodeError, IOError):
                pass
        return DEFAULT_CONFIG.copy()

    def save_config(self):
        """Save configuration to file."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2)

    def get(self, key: str, default=None):
        """Get configuration value."""
        return self.config.get(key, default)

    def set(self, key: str, value):
        """Set configuration value."""
        self.config[key] = value
        self.save_config()


class QuickBinHistory:
    """Manages snippet history."""

    def __init__(self):
        self.history_file = HISTORY_FILE
        self.entries = self.load_history()

    def load_history(self) -> List[Dict]:
        """Load history from file."""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return []

    def save_history(self):
        """Save history to file."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.entries, f, indent=2)

    def add(self, url: str, description: str, language: str):
        """Add entry to history."""
        entry = {
            "url": url,
            "description": description,
            "language": language,
            "created_at": datetime.now().isoformat(),
        }
        self.entries.insert(0, entry)
        # Limit history size
        config = QuickBinConfig()
        limit = config.get("history_limit", 100)
        self.entries = self.entries[:limit]
        self.save_history()

    def list(self, limit: int = 20) -> List[Dict]:
        """List history entries."""
        return self.entries[:limit]

    def clear(self):
        """Clear all history."""
        self.entries = []
        self.save_history()


class QuickBinUploader:
    """Handles snippet uploads."""

    def __init__(self, github_token: Optional[str] = None):
        self.github_token = github_token or os.environ.get("GITHUB_TOKEN")
        self.headers = {}
        if self.github_token:
            self.headers["Authorization"] = f"token {self.github_token}"
        self.headers["Accept"] = "application/vnd.github.v3+json"

    def upload_to_gist(self, content: str, description: str, filename: str, public: bool = False) -> Dict:
        """Upload snippet to GitHub Gist."""
        data = {
            "description": description,
            "public": public,
            "files": {
                filename: {
                    "content": content
                }
            }
        }

        try:
            response = requests.post(
                "https://api.github.com/gists",
                headers=self.headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise click.ClickException(f"Failed to upload: {e}")

    def upload_to_0x0(self, content: str, filename: str) -> str:
        """Upload to 0x0.st as fallback."""
        try:
            files = {'file': (filename, content)}
            response = requests.post(
                "https://0x0.st",
                files=files,
                timeout=30
            )
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            raise click.ClickException(f"Failed to upload to fallback: {e}")


def parse_expiration(exp: str) -> Optional[str]:
    """Parse expiration string to datetime."""
    if not exp:
        return None

    units = {
        'm': 'minutes',
        'h': 'hours',
        'd': 'days',
        'w': 'weeks',
    }

    try:
        value = int(exp[:-1])
        unit = exp[-1].lower()
        if unit not in units:
            raise ValueError
        return exp
    except (ValueError, IndexError):
        return None


def get_language_from_filename(filename: str) -> str:
    """Detect language from filename extension."""
    ext_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.jsx': 'jsx',
        '.tsx': 'tsx',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.h': 'c',
        '.go': 'go',
        '.rs': 'rust',
        '.rb': 'ruby',
        '.php': 'php',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.scala': 'scala',
        '.r': 'r',
        '.m': 'objectivec',
        '.sh': 'bash',
        '.bash': 'bash',
        '.zsh': 'zsh',
        '.fish': 'fish',
        '.ps1': 'powershell',
        '.sql': 'sql',
        '.html': 'html',
        '.htm': 'html',
        '.css': 'css',
        '.scss': 'scss',
        '.sass': 'sass',
        '.less': 'less',
        '.xml': 'xml',
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.toml': 'toml',
        '.ini': 'ini',
        '.cfg': 'ini',
        '.conf': 'ini',
        '.md': 'markdown',
        '.markdown': 'markdown',
        '.rst': 'rst',
        '.tex': 'latex',
        '.vim': 'vim',
        '.lua': 'lua',
        '.pl': 'perl',
        '.pm': 'perl',
        '.t': 'perl',
        '.erl': 'erlang',
        '.hrl': 'erlang',
        '.ex': 'elixir',
        '.exs': 'elixir',
        '.clj': 'clojure',
        '.cljs': 'clojure',
        '.hs': 'haskell',
        '.lhs': 'haskell',
        '.ml': 'ocaml',
        '.mli': 'ocaml',
        '.fs': 'fsharp',
        '.fsx': 'fsharp',
        '.fsi': 'fsharp',
        '.dart': 'dart',
        '.jl': 'julia',
        '.groovy': 'groovy',
        '.gradle': 'groovy',
        '.dockerfile': 'dockerfile',
        '.makefile': 'makefile',
        '.cmake': 'cmake',
    }

    ext = Path(filename).suffix.lower()
    return ext_map.get(ext, 'text')


@click.group()
@click.version_option(version="1.0.0", prog_name="quickbin")
@click.pass_context
def cli(ctx):
    """QuickBin - Share code snippets instantly from your terminal."""
    ctx.ensure_object(dict)
    ctx.obj['config'] = QuickBinConfig()
    ctx.obj['history'] = QuickBinHistory()


@cli.command()
@click.argument('source', required=False)
@click.option('-f', '--file', 'input_file', type=click.File('r'), help='File to upload')
@click.option('-d', '--description', default='QuickBin snippet', help='Snippet description')
@click.option('-l', '--language', help='Programming language for syntax highlighting')
@click.option('-e', '--expire', help='Expiration time (e.g., 1h, 1d, 7d)')
@click.option('-p', '--public', is_flag=True, help='Make snippet public')
@click.option('-c', '--copy', is_flag=True, help='Copy URL to clipboard')
@click.option('--no-copy', is_flag=True, help='Do not copy URL to clipboard')
@click.pass_context
def upload(ctx, source, input_file, description, language, expire, public, copy, no_copy):
    """Upload a code snippet.

    SOURCE can be:
    - A file path
    - "-" to read from stdin
    - Omitted to use --file option
    """
    config = ctx.obj['config']
    history = ctx.obj['history']

    # Determine content source
    if source == '-':
        content = click.get_text_stream('stdin').read()
        filename = 'snippet.txt'
    elif input_file:
        content = input_file.read()
        filename = Path(input_file.name).name
    elif source:
        try:
            with open(source, 'r', encoding='utf-8') as f:
                content = f.read()
            filename = Path(source).name
        except FileNotFoundError:
            raise click.ClickException(f"File not found: {source}")
        except IOError as e:
            raise click.ClickException(f"Cannot read file: {e}")
    else:
        raise click.ClickException("Please provide a file path, use -f/--file, or use '-' for stdin")

    # Detect language
    if not language:
        language = get_language_from_filename(filename)

    # Upload
    uploader = QuickBinUploader()

    with console.status("[bold green]Uploading snippet..."):
        try:
            result = uploader.upload_to_gist(
                content=content,
                description=description,
                filename=filename,
                public=public
            )
            url = result['html_url']
        except click.ClickException:
            # Fallback to 0x0.st
            url = uploader.upload_to_0x0(content, filename)

    # Display result
    console.print()
    console.print(Panel(
        f"[bold green]✓[/bold green] Snippet uploaded successfully!\n\n"
        f"[bold]URL:[/bold] [link={url}]{url}[/link]\n"
        f"[bold]Language:[/bold] {language}",
        title="QuickBin",
        border_style="green"
    ))

    # Copy to clipboard
    should_copy = copy or (config.get('auto_copy', True) and not no_copy)
    if should_copy:
        try:
            import pyperclip
            pyperclip.copy(url)
            console.print("[dim]📋 URL copied to clipboard[/dim]")
        except ImportError:
            pass

    # Add to history
    history.add(url, description, language)


@cli.command()
@click.option('-n', '--limit', default=20, help='Number of entries to show')
@click.pass_context
def history(ctx, limit):
    """Show upload history."""
    history_mgr = ctx.obj['history']
    entries = history_mgr.list(limit)

    if not entries:
        console.print("[yellow]No history entries found.[/yellow]")
        return

    table = Table(
        title="QuickBin History",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta"
    )
    table.add_column("#", style="dim", width=4)
    table.add_column("Date", width=19)
    table.add_column("Language", width=12)
    table.add_column("Description", min_width=30)
    table.add_column("URL", min_width=40)

    for i, entry in enumerate(entries, 1):
        created = entry.get('created_at', 'Unknown')
        if created != 'Unknown':
            try:
                dt = datetime.fromisoformat(created)
                created = dt.strftime("%Y-%m-%d %H:%M")
            except ValueError:
                pass

        table.add_row(
            str(i),
            created,
            entry.get('language', 'text'),
            entry.get('description', 'No description')[:50],
            entry.get('url', '')
        )

    console.print(table)


@cli.command()
@click.confirmation_option(prompt='Are you sure you want to clear all history?')
@click.pass_context
def clear(ctx):
    """Clear upload history."""
    history_mgr = ctx.obj['history']
    history_mgr.clear()
    console.print("[green]✓ History cleared[/green]")


@cli.command()
@click.option('-k', '--key', help='Configuration key')
@click.option('-v', '--value', help='Configuration value')
@click.option('-l', '--list', 'list_config', is_flag=True, help='List all configuration')
@click.pass_context
def config(ctx, key, value, list_config):
    """Manage QuickBin configuration."""
    config_mgr = ctx.obj['config']

    if list_config:
        table = Table(title="QuickBin Configuration", box=box.ROUNDED)
        table.add_column("Key", style="cyan")
        table.add_column("Value")
        for k, v in config_mgr.config.items():
            table.add_row(k, str(v))
        console.print(table)
        return

    if key and value:
        # Convert value types
        if value.lower() in ('true', 'false'):
            value = value.lower() == 'true'
        elif value.isdigit():
            value = int(value)

        config_mgr.set(key, value)
        console.print(f"[green]✓ Set {key} = {value}[/green]")
    elif key:
        val = config_mgr.get(key)
        console.print(f"{key} = {val}")
    else:
        console.print("Use -k KEY -v VALUE to set, or --list to view all")


@cli.command()
@click.argument('url')
@click.pass_context
def view(ctx, url):
    """View a snippet from URL."""
    try:
        # Handle gist URLs
        if 'gist.github.com' in url:
            gist_id = url.split('/')[-1].split('#')[0]
            api_url = f"https://api.github.com/gists/{gist_id}"
            response = requests.get(api_url, timeout=30)
            response.raise_for_status()
            data = response.json()

            for filename, file_data in data['files'].items():
                content = file_data['content']
                language = file_data.get('language', 'text') or 'text'

                console.print(Panel(
                    Syntax(content, language.lower(), theme="monokai", line_numbers=True),
                    title=f"📄 {filename}",
                    border_style="blue"
                ))
        else:
            # Generic URL
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            content = response.text

            console.print(Panel(
                Syntax(content, "text", theme="monokai"),
                title="📄 Snippet",
                border_style="blue"
            ))
    except requests.exceptions.RequestException as e:
        raise click.ClickException(f"Failed to fetch snippet: {e}")


@cli.command()
def languages():
    """List supported languages for syntax highlighting."""
    langs = [
        "bash", "c", "clojure", "cpp", "csharp", "css", "dart", "dockerfile",
        "elixir", "erlang", "go", "groovy", "haskell", "html", "java",
        "javascript", "json", "julia", "kotlin", "latex", "lua", "markdown",
        "objectivec", "ocaml", "perl", "php", "powershell", "python", "r",
        "ruby", "rust", "scala", "scss", "sql", "swift", "text", "toml",
        "typescript", "vim", "xml", "yaml", "yaml", "zsh"
    ]

    console.print("[bold]Supported Languages:[/bold]")
    console.print(", ".join(sorted(set(langs))))


if __name__ == '__main__':
    cli()
