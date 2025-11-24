"""Entry point module for my_package."""

from . import greet
from .core.example import greet2


def main():
    print("Hello from my_package!")
    print(greet())
    print(greet2("World"))


if __name__ == "__main__":
    main()
