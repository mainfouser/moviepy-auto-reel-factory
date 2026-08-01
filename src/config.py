"""
MARF Configuration Loader
Loads config/settings.json
"""

from __future__ import annotations

import json
from pathlib import Path


# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent

# Config file
CONFIG_FILE = ROOT_DIR / "config" / "settings.json"


def load_config() -> dict:
    """
    Load JSON configuration file.
    """

    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_FILE}"
        )

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# Global config object
CONFIG = load_config()


# Project
PROJECT = CONFIG.get("project", {})

# Video
VIDEO = CONFIG.get("video", {})

# RSS
RSS = CONFIG.get("rss", {})

# AI
AI = CONFIG.get("ai", {})

# TTS
TTS = CONFIG.get("tts", {})

# Assets
ASSETS = CONFIG.get("assets", {})

# Output
OUTPUT = CONFIG.get("output", {})

# Google Drive
GOOGLE_DRIVE = CONFIG.get("google_drive", {})

# Facebook
FACEBOOK = CONFIG.get("facebook", {})

# YouTube
YOUTUBE = CONFIG.get("youtube", {})

# Scheduler
SCHEDULER = CONFIG.get("scheduler", {})


def get(section: str, default=None):
    """
    Get any config section.
    """
    return CONFIG.get(section, default)


def reload():
    """
    Reload config without restarting app.
    """
    global CONFIG

    CONFIG = load_config()

    return CONFIG
