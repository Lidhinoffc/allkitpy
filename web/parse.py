from bs4 import BeautifulSoup


def html(content):
    """
    Parse HTML.
    """

    return BeautifulSoup(
        content,
        "html.parser"
    )


def title(content):
    """
    Return page title.
    """

    soup = html(content)

    if soup.title:

        return soup.title.text.strip()

    return None


def links(content):
    """
    Return all hyperlinks.
    """

    soup = html(content)

    return [
        tag.get("href")
        for tag in soup.find_all("a")
        if tag.get("href")
    ]