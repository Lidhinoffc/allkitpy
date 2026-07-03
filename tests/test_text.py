import allpy


def test_upper():

    assert allpy.text.upper("hello") == "HELLO"


def test_lower():

    assert allpy.text.lower("HELLO") == "hello"


def test_title():

    assert allpy.text.title("hello world") == "Hello World"


def test_capitalize():

    assert allpy.text.capitalize("hello") == "Hello"


def test_word_count():

    assert allpy.text.word_count("one two three") == 3