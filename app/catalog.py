import json
from pathlib import Path


CATALOG_PATH = Path("data/shl_catalog.json")


def load_catalog():
    """
    Load SHL catalog and fix malformed entries.
    """

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # Fix malformed JSON entry
    text = text.replace(
        "Microsoft \n    365 (New)",
        "Microsoft 365 (New)"
    )

    return json.loads(text)


def get_catalog_size():
    return len(load_catalog())