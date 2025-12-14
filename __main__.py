"""
Docstring for tuxman.__main__
"""

from core import module1
import os
import os.path

# from core import sudo
from core import sudo


def main():
    sudo.elevate_privileges()
    print(f"UID: {os.getuid()}")
    print("Hello from my_package!")
    # Import and use modules from the core package
    module1.some_function()
    print("Current working directory:", os.getcwd())


if __name__ == "__main__":
    main()
