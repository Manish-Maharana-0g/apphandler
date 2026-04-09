from setuptools import setup, find_packages

setup(
    name="apphandler",
    version="1.0.0",
    author="Manish",
    description="App installation utilities for Python apps",
    packages=find_packages(exclude=["venv*", ".venv", ".venv.*"]),
    install_requires=[
        "winshell",
        "pywin32",
    ],
    platforms=["win32"],
)