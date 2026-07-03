class AllpyError(Exception):
    """Base error for all Allpy modules."""
    pass


class FileError(AllpyError):
    """Errors related to file operations."""
    pass


class ImageError(AllpyError):
    """Errors related to image operations."""
    pass


class TextError(AllpyError):
    """Errors related to text operations."""
    pass

class AllpyError(Exception):
    """Base exception for Allpy."""


class ValidationError(AllpyError):
    """Invalid user input."""


class FileError(AllpyError):
    """File operation failed."""


class ImageError(AllpyError):
    """Image operation failed."""


class PDFError(AllpyError):
    """PDF operation failed."""


class AudioError(AllpyError):
    """Audio operation failed."""


class VideoError(AllpyError):
    """Video operation failed."""


class WebError(AllpyError):
    """Web operation failed."""


class AIError(AllpyError):
    """AI operation failed."""