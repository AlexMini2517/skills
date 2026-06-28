from pathlib import Path
from urllib.request import urlopen
import json
import shutil

SOURCE_DIR = "docs/pages/versions/v54.0.0/sdk"
BASE_DIR = Path(__file__).resolve().parent
DEST_DIR = BASE_DIR / "packages"

def walk(path: str):
    with urlopen(f"https://api.github.com/repos/expo/expo/contents/{path}?ref=main", timeout=30) as r:
        items = json.load(r)

    for item in items:
        item_path = item["path"]
        out_path = DEST_DIR / Path(item_path).relative_to(SOURCE_DIR)

        if item["type"] == "dir":
            walk(item_path)
        elif item["type"] == "file":
            download_url = item.get("download_url")
            if not download_url:
                raise RuntimeError(f"Nessun download_url per {item_path}")
            print(f"Downloading {item_path} into {out_path.resolve()}")
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with urlopen(download_url, timeout=60) as r:
                out_path.write_bytes(r.read())

if DEST_DIR.exists():
    print(f"Rimuovo {DEST_DIR.resolve()} ...")
    shutil.rmtree(DEST_DIR)

DEST_DIR.mkdir()
print(f"Salvo in: {DEST_DIR.resolve()}")
walk(SOURCE_DIR)
print(f"\nFatto. File salvati in: {DEST_DIR.resolve()}")
