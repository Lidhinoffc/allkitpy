import allpy


def test_parse_html():

    html = """

    <html>

    <title>Allpy</title>

    </html>

    """

    assert allpy.web.title(html) == "Allpy"