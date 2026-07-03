from pathlib import Path


def exists(path):
    """
    Check if path exists.
    """
    return Path(path).exists()


def absolute(path):
    """
    Return absolute path.
    """
    return str(Path(path).resolve())


def parent(path):
    """
    Return parent directory.
    """
    return str(Path(path).parent)


def filename(path):
    """
    Return filename.
    """
    return Path(path).name


def extension(path):
    """
    Return file extension.
    """
    return Path(path).suffix