"""
Docstring for tuxman.__main__
"""

import os
import os.path

from core import module1
from core import sudo


CWD = os.getcwd()
SCRIPT_LOCATION = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(SCRIPT_LOCATION, "config.json")
RESOURCES_PATH = os.path.join(SCRIPT_LOCATION, "resources")


def main():
    sudo.elevate_privileges()
    print("Hello from my_package!")
    # Import and use modules from the core package
    module1.some_function()
    print("Current working directory:", os.getcwd())
    print("Script location:", os.path.dirname(__file__))
    os.chdir(os.path.dirname(__file__))
    print("Changed working directory to script location:", os.getcwd())


if __name__ == "__main__":
    main()
