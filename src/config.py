import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_FILE = BASE_DIR / "config" / "settings.json"


def load_settings():
    """Load MARF settings from settings.json"""

    if not SETTINGS_FILE.exists():
        raise FileNotFoundError(
            f"Settings file not found: {SETTINGS_FILE}"
        )

    with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
