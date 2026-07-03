from pathlib import Path
import shutil


def create(folder):
    """
    Create a directory.
    """
    Path(folder).mkdir(
        parents=True,
        exist_ok=True
    )


def remove(folder):
    """
    Delete a directory.
    """
    shutil.rmtree(
        folder,
        ignore_errors=True
    )


def list(folder="."):
    """
    List directory contents.
    """
    return [item.name for item in Path(folder).iterdir()]