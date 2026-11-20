#!/usr/bin/env python3
"""Entry point for news-image-20261120.

Copies the rendered front page (entry.png, sitting beside this file)
into the output directory make.fun grades.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
TARGET_NAME = "entry.png"


def run() -> Path:
    destination_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / TARGET_NAME
    shutil.copyfile(SOURCE, destination)
    return destination


if __name__ == "__main__":
    print(f"copied entry.png to {run()}")
