import os


def pid():
    """
    Current process ID.
    """
    return os.getpid()


def cwd():
    """
    Current working directory.
    """
    return os.getcwd()