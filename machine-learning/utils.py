import requests


def download_file(url, local_path):
    # ref: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_path
