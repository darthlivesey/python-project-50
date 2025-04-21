from gendiff.scripts.generate_plain_view import generate_plain_view
from tests.test_data.test_values import (
    long_sorted_output,
    plain_long_result,
    plain_short_result,
    short_sorted_output,
)


def test_generate_plain_view():
    assert generate_plain_view(short_sorted_output) == plain_short_result
    assert generate_plain_view(long_sorted_output) == plain_long_result