"""
Docstring for tuxman.core.sudo
"""

import os
import sys


def elevate_privileges():
    """Elevate privileges using sudo if not running as root."""
    if os.getuid() != 0:
        cmd = ("sudo", sys.executable, *sys.argv)
        os.execvp("sudo", cmd)
