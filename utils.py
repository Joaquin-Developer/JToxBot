import configparser as ConfigParser
from typing import Any


CONFIG = None
CONFIG_FILE = "core/config.cfg"


def get_config():
    """obtenemos objeto config"""
    global CONFIG

    if not CONFIG:
        CONFIG = ConfigParser.ConfigParser(interpolation=None)
        CONFIG.read(CONFIG_FILE)

    return CONFIG


def get_from_config(section, key, tipo=None) -> Any:
    """Obtenemos cfg desde la config"""
    config = get_config()

    if tipo == "boolean":
        return config.getboolean(section, key)
    elif tipo == "int":
        return config.getint(section, key)

    return config.get(section, key)


if __name__ == "__main__":
    pass
