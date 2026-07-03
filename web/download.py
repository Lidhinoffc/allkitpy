import requests


def download(url, save):
    """
    Download a file.
    """

    response = requests.get(url, stream=True)

    response.raise_for_status()

    with open(save, "wb") as file:

        for chunk in response.iter_content(8192):

            if chunk:
                file.write(chunk)

    return save