import fitz


def create(save, text="Hello from Allpy"):
    """
    Create a simple PDF.

    Parameters
    ----------
    save : str
        Output PDF filename.

    text : str
        Text written inside the PDF.
    """

    doc = fitz.open()

    page = doc.new_page()

    page.insert_text(
        (72, 72),
        text,
        fontsize=14
    )

    doc.save(save)

    doc.close()