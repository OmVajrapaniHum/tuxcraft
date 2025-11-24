"""Setup script for my_package."""

from setuptools import setup, find_packages

setup(
    name="tuxcraft",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tuxcraft = tuxcraft.__main__:main",
        ],
    },
)
