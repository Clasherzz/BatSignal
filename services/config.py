import os
import json

APP_NAME = "battery_alert"

def get_config_path():
    local_appdata = os.getenv("LOCALAPPDATA")
    config_dir = os.path.join(local_appdata, APP_NAME)
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "settings.json")

def load_config():
    config_path = get_config_path()
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {
        "low_threshold": 20,
        "high_threshold": 80,
        "beep_duration": 1000,
        "repeat":"Yes"
    }

def save_config(config):
    config_path = get_config_path()
    with open(config_path, 'w') as f:
        json.dump(config, f)
