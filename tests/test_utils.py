from project_b_utils import (
    reverse_string,
    capitalize_words,
    get_current_date
)


def test_reverse_string():
    assert reverse_string("Hello") == "olleH"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_current_date():
    assert len(get_current_date()) == 10

