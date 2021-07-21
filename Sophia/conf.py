import os


import sys
from envparse import env
from Sophia import LOGGER
from Sophia.utils.logger import log

DEFAULTS = {
    "LOAD_MODULES": True,
    "DEBUG_MODE": True,
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_DB_FSM": 1,
    "MONGODB_URI": "localhost",
    "MONGO_DB": "Sophia",
    "API_PORT": 8080,
    "JOIN_CONFIRM_DURATION": "30m",
}

CONFIG_PATH = "data/bot_conf.yaml"
if os.name == "nt":
    log.debug("Detected Windows, changing config path...")
    CONFIG_PATH = os.getcwd() + "\\data\\bot_conf.yaml"

if os.path.isfile(CONFIG_PATH):
    log.info(CONFIG_PATH)
    for item in (
        data := yaml.load(open("data/bot_conf.yaml", "r"), Loader=yaml.CLoader)
    ):
        DEFAULTS[item.upper()] = data[item]
else:
    log.info("Using env vars")



def get_str_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.str(name, default=default)) and not required:
        LOGGER.warn("No str key: " + name)
        return None
    elif not data:
        LOGGER.critical("No str key: " + name)
        sys.exit(2)
    else:
        return data

def get_int_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.int(name, default=default)) and not required:
        LOGGER.warn("No int key: " + name)
        return None
    elif not data:
        LOGGER.critical("No int key: " + name)
        sys.exit(2)
    else:
        return data
