from dataclasses import dataclass
from pathlib import Path
import yaml
import os


@dataclass
class Config:
    STEAM_API_ALL_GAMES: str
    STEAM_API_GET_GAME: str


def load_config() -> "Config":
    # 1. Start at the current file's directory
    current_dir = Path(__file__).resolve().parent

    # 2. Go up the known number of levels (e.g., .parent.parent is 2 levels up)
    # This example assumes config.py is 2 levels below the root. Adjust as needed.
    project_root = current_dir.parent

    # 3. Construct the path to the config file
    config_path = project_root / "config.yml"

    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found at expected path: {config_path}"
        )

    # 4. Load the configuration
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return Config(**data)


config = load_config()
