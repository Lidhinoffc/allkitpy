from .format import (
    upper,
    uppercase,
    lower,
    lowercase,
    title,
    capitalize,
)

from .clean import remove_spaces, remove_extra_spaces, remove_numbers
from .analyze import word_count, char_count, sentence_count


class Text:
    @staticmethod
    def upper(*a):
        return upper(*a)

    @staticmethod
    def uppercase(*a):
        return uppercase(*a)

    @staticmethod
    def lower(*a):
        return lower(*a)

    @staticmethod
    def lowercase(*a):
        return lowercase(*a)

    @staticmethod
    def title(*a):
        return title(*a)

    @staticmethod
    def capitalize(*a):
        return capitalize(*a)

    @staticmethod
    def remove_spaces(*a):
        return remove_spaces(*a)

    @staticmethod
    def remove_extra_spaces(*a):
        return remove_extra_spaces(*a)

    @staticmethod
    def remove_numbers(*a):
        return remove_numbers(*a)

    @staticmethod
    def word_count(*a):
        return word_count(*a)

    @staticmethod
    def char_count(*a):
        return char_count(*a)

    @staticmethod
    def sentence_count(*a):
        return sentence_count(*a)