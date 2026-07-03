from urllib.parse import (
    urlparse,
    urljoin
)


def parse(url):
    """
    Parse URL.
    """

    return urlparse(url)


def join(base, path):
    """
    Join URLs.
    """

    return urljoin(base, path)