import os


def get(name, default=None):
    """
    Get environment variable.
    """
    return os.getenv(name, default)


def set(name, value):
    """
    Set environment variable.
    """
    os.environ[name] = str(value)


def all():
    """
    Return all environment variables.
    """
    return dict(os.environ)