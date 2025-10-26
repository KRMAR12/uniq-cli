from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setup(
    name="uniq_cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click==8.3.0",
        "colorama==0.4.6",
        "setuptools==80.9.0",
    ],
    entry_points={
        "console_scripts": [
            "uniq_cli=uniq_cli.__main__:main",
        ],
    },
    long_description=README,
    long_description_content_type="text/markdown",
)
