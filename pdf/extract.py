import fitz


def extract_text(input_file):
    """
    Extract all text from a PDF.

    Parameters
    ----------
    input_file : str
        PDF filename.

    Returns
    -------
    str
        Complete text inside PDF.
    """

    doc = fitz.open(input_file)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text