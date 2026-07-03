import allpy
import os
import tempfile


def test_create_pdf():

    tmp = tempfile.gettempdir()

    filename = os.path.join(
        tmp,
        "sample.pdf"
    )

    allpy.pdf.create(
        filename,
        text="Hello"
    )

    assert os.path.exists(filename)