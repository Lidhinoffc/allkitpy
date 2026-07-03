import json


def load(filename):
    """
    Load JSON file.
    """

    with open(filename, "r", encoding="utf-8") as file:

        return json.load(file)


def save(data, filename):
    """
    Save JSON file.
    """

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4
        )