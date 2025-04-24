from gendiff.scripts.generate_json_view import generate_json_view
from tests.test_data.test_values import (
    LONG_JSON_OUTPUT,
    LONG_SORTED_OUTPUT,
    SHORT_JSON_OUTPUT,
    SHORT_SORTED_OUTPUT,
)


def test_generate_json_view_short():
    assert generate_json_view(SHORT_SORTED_OUTPUT) == SHORT_JSON_OUTPUT


def test_generate_json_view_long():
    assert generate_json_view(LONG_SORTED_OUTPUT) == LONG_JSON_OUTPUT