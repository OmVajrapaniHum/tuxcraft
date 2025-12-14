"""
Docstring for tuxman.setup
"""

from setuptools import setup, find_packages

setup(
    name="tuxman",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tuxman = __main__:main",
        ],
    },
)
