from .request import get, post
from .download import download
from .parse import html, title, links
from .json_utils import load, save
from .url import parse, join
from .session import create


class Web:

    @staticmethod
    def get(*a, **k):
        return get(*a, **k)

    @staticmethod
    def post(*a, **k):
        return post(*a, **k)

    @staticmethod
    def download(*a, **k):
        return download(*a, **k)

    @staticmethod
    def html(*a, **k):
        return html(*a, **k)

    @staticmethod
    def title(*a, **k):
        return title(*a, **k)

    @staticmethod
    def links(*a, **k):
        return links(*a, **k)

    @staticmethod
    def load(*a, **k):
        return load(*a, **k)

    @staticmethod
    def save(*a, **k):
        return save(*a, **k)

    @staticmethod
    def parse(*a, **k):
        return parse(*a, **k)

    @staticmethod
    def join(*a, **k):
        return join(*a, **k)

    @staticmethod
    def create(*a, **k):
        return create(*a, **k)