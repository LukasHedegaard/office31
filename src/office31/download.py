# Source: https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url

import requests
from pathlib import Path
import shutil


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={"id": id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {"id": id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 200000

    print("Downloading")
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def download_and_extract_office31(target_path):

    tmp_path = Path("./tmp.tar.gz").absolute()
    download_file_from_google_drive(
        id="0B4IapRTv9pJ1WGZVd1VDMmhwdlE", destination=str(tmp_path),
    )

    target_path.mkdir(parents=True, exist_ok=True)

    print("Unpacking")
    shutil.unpack_archive(str(tmp_path), target_path)

    print("Cleaning up")
    tmp_path.unlink()

    print("Done")
