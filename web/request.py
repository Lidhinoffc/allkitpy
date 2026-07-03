import requests


def get(url, **kwargs):
    """
    HTTP GET request.
    """

    response = requests.get(url, **kwargs)

    response.raise_for_status()

    return response


def post(url, data=None, json=None, **kwargs):
    """
    HTTP POST request.
    """

    response = requests.post(
        url,
        data=data,
        json=json,
        **kwargs
    )

    response.raise_for_status()

    return response