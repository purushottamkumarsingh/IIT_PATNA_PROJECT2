import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

list_of_files = [
    "main.py",
    "ui.py",
    "data_handler.py",   # fixed spelling
    "cleaner.py",
    "table_viewer.py",
    "requirements.txt"   # fixed naming
]

for filepath in list_of_files:
    file = Path(filepath)

    # Create file if not exists or empty
    if not file.exists() or file.stat().st_size == 0:
        with open(file, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")
