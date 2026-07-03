import platform


def system():
    return platform.system()


def release():
    return platform.release()


def version():
    return platform.version()


def machine():
    return platform.machine()


def processor():
    return platform.processor()


def python_version():
    return platform.python_version()