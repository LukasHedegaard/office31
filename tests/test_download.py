from office31 import download_and_extract_office31
from pathlib import Path
import shutil


def test_download_and_extract_office31():
    path = Path(__file__).parent.parent / "data"
    if path.exists():
        shutil.rmtree(path)
    assert not path.exists()

    download_and_extract_office31(path)

    assert path.exists()
