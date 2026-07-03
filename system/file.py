from pathlib import Path


def create(filename):
    """
    Create an empty file.
    """
    Path(filename).touch(exist_ok=True)


def remove(filename):
    """
    Delete a file.
    """
    Path(filename).unlink(missing_ok=True)