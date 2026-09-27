from __future__ import annotations

import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

username = os.getenv("KAGGLE_USERNAME")
key = os.getenv("KAGGLE_KEY")
if not username or not key:
    raise RuntimeError(
        "Missing KAGGLE_USERNAME/KAGGLE_KEY in .env. "
        "Create a Kaggle API token first."
    )

out_dir = Path("data/raw/m5")
out_dir.mkdir(parents=True, exist_ok=True)

# The Kaggle CLI reads KAGGLE_USERNAME/KAGGLE_KEY from environment.
env = os.environ.copy()
env["KAGGLE_USERNAME"] = username
env["KAGGLE_KEY"] = key

cmd = [
    "kaggle",
    "competitions",
    "download",
    "-c",
    "m5-forecasting-accuracy",
    "-p",
    str(out_dir),
]

subprocess.run(cmd, env=env, check=True)
print(f"Downloaded M5 competition archive into {out_dir}")
print("Unzip the downloaded archive before ingestion.")
