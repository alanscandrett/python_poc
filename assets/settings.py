import os, sys
import json
import logging
import logging.config
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# MISC
MISC_CONFIG = {
    "WARNING_STATE": 5
}

# Email
EMAIL = {
    "SMTP_SERVER": "smtp.gmail.com",
    "ACCOUNT": os.environ.get("EMAIL_ACCOUNT"),
    "PASS": os.environ.get("EMAIL_PASS"),
    "RECIPIENT": os.environ.get("EMAIL_RECIPIENT"),
    "TEMPLATE_WARNING": """\
        Subject: Sensor Warnings

        The following sensors are at a WARNING state:"""
}

# Devices API
API_SIGFOX = {
    "URL": "https://api.sigfox.com/v2/",
    "USER": os.environ.get("API_SIGFOX_USER"),
    "PASS": os.environ.get("API_SIGFOX_PASS"),
    "DEVICES_QUERY": {
        "ENDPOINT": "devices/?",
        "PARAMS": {
            "deep": "false",
            "authorizations": "false",
            "limit": "100",
            "offset": "0"
        }
    },
}

# ArcGIS Online
AGOL_NOVEGEN = {
    "URL": "https://novegen-ie.maps.arcgis.com/",
    "USER": os.environ.get("AGOL_NOVEGEN_USER"),
    "PASS": os.environ.get("AGOL_NOVEGEN_PASS"),
    "FEATURE_LAYER": None
}

def setupLogging(
    default_path=f'{sys.path[0]}/assets/logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
            print(config)
        logging.config.dictConfig(config)
    else:
        print(f"no logging config found at {path}, loading default.")
        logging.basicConfig(level=default_level)

