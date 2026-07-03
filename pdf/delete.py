import fitz


def delete_pages(input_file, pages, save):
    """
    Delete pages.

    pages uses zero-based indexes.
    Example:
    [0,2]
    """

    pdf = fitz.open(input_file)

    for page in sorted(pages, reverse=True):
        pdf.delete_page(page)

    pdf.save(save)

    pdf.close()