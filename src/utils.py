here
"""
MARF Utility Functions
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path


def ensure_directory(path: str | Path) -> Path:
    """
    Create directory if it does not exist.
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def load_json(file_path: str | Path) -> dict:
    """
    Load JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict, file_path: str | Path):
    """
    Save JSON file.
    """
    path = Path(file_path)
    ensure_directory(path.parent)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )


def timestamp() -> str:
    """
    Current timestamp.
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def sanitize_filename(filename: str) -> str:
    """
    Remove invalid filename characters.
    """
    filename = re.sub(r'[<>:"/\\|?*]', "", filename)
    filename = filename.strip()
    filename = filename.replace(" ", "_")

    return filename


def create_output_filename(title: str, extension: str = ".mp4") -> str:
    """
    Create safe output filename.
    """
    safe = sanitize_filename(title)

    return f"{timestamp()}_{safe}{extension}"


def delete_file(file_path: str | Path):
    """
    Delete file safely.
    """
    path = Path(file_path)

    if path.exists():
        path.unlink()


def file_exists(file_path: str | Path) -> bool:
    """
    Check if file exists.
    """
    return Path(file_path).exists()

