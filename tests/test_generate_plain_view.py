from gendiff.scripts.generate_plain_view import generate_plain_view
from tests.test_data.test_values import (
    LONG_SORTED_OUTPUT,
    PLAIN_LONG_RESULT,
    PLAIN_SHORT_RESULT,
    SHORT_SORTED_OUTPUT,
)


def test_generate_plain_view_short():
    assert generate_plain_view(SHORT_SORTED_OUTPUT) == PLAIN_SHORT_RESULT


def test_generate_plain_view_long():
    assert generate_plain_view(LONG_SORTED_OUTPUT) == PLAIN_LONG_RESULT