import os
import json

CONFIG_FILE = os.path.expanduser("~/.notion_cli_config.json")


def write_token(token):
    """Saves the token to a config file."""
    with open(CONFIG_FILE, "w+") as f:
        json.dump({"token": token}, f)


def read_token():
    """Loads the token from the config file."""
    with open(CONFIG_FILE, "r") as f:
        return json.load(f).get("token")
