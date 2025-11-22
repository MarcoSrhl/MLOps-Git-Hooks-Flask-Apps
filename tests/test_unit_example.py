from app import count_words


def test_count_words_basic():
    assert count_words("hello world") == 2
    assert count_words("Flask app test") == 3


def test_count_words_empty_or_invalid():
    assert count_words("") == 0
    assert count_words(None) == 0
    assert count_words("   ") == 0
