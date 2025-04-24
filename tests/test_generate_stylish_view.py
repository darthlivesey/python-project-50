from gendiff.scripts.generate_stylish_view import generate_stylish_view
from tests.test_data.test_values import (
    LONG_SORTED_OUTPUT,
    SHORT_SORTED_OUTPUT,
    STYLISH_LONG_RESULT,
    STYLISH_SHORT_RESULT,
)


def test_generate_stylish_view_short():
    assert generate_stylish_view(SHORT_SORTED_OUTPUT) == STYLISH_SHORT_RESULT


def test_generate_stylish_view_long():
    assert generate_stylish_view(LONG_SORTED_OUTPUT) == STYLISH_LONG_RESULT