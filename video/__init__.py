from .convert import convert
from .merge import merge

from .edit import (
    trim,
    resize,
    rotate
)

from .extract import extract_audio

from .info import (
    duration,
    resolution,
    fps,
    metadata
)

from .split import split
from .frames import extract_frames
from .compress import compress
from .watermark import watermark

from .effects import (
    speed,
    reverse,
    mute
)

from .audio import add_audio
from .crop import crop
from .gif import gif


class Video:

    @staticmethod
    def convert(*a, **k):
        return convert(*a, **k)

    @staticmethod
    def merge(*a, **k):
        return merge(*a, **k)

    @staticmethod
    def trim(*a, **k):
        return trim(*a, **k)

    @staticmethod
    def resize(*a, **k):
        return resize(*a, **k)

    @staticmethod
    def rotate(*a, **k):
        return rotate(*a, **k)

    @staticmethod
    def extract_audio(*a, **k):
        return extract_audio(*a, **k)

    @staticmethod
    def duration(*a, **k):
        return duration(*a, **k)

    @staticmethod
    def resolution(*a, **k):
        return resolution(*a, **k)

    @staticmethod
    def fps(*a, **k):
        return fps(*a, **k)

    @staticmethod
    def metadata(*a, **k):
        return metadata(*a, **k)

    @staticmethod
    def split(*a, **k):
        return split(*a, **k)

    @staticmethod
    def extract_frames(*a, **k):
        return extract_frames(*a, **k)

    @staticmethod
    def compress(*a, **k):
        return compress(*a, **k)

    @staticmethod
    def watermark(*a, **k):
        return watermark(*a, **k)

    @staticmethod
    def speed(*a, **k):
        return speed(*a, **k)

    @staticmethod
    def reverse(*a, **k):
        return reverse(*a, **k)

    @staticmethod
    def mute(*a, **k):
        return mute(*a, **k)

    @staticmethod
    def add_audio(*a, **k):
        return add_audio(*a, **k)

    @staticmethod
    def crop(*a, **k):
        return crop(*a, **k)

    @staticmethod
    def gif(*a, **k):
        return gif(*a, **k)