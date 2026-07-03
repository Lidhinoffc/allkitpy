import fitz


def compress(input_file, save):
    """
    Basic PDF optimization.
    """

    pdf = fitz.open(input_file)

    pdf.save(
        save,
        garbage=4,
        deflate=True,
        clean=True
    )

    pdf.close()