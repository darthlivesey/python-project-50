from gendiff.scripts.generate_stylish_view import generate_stylish_view
from tests.test_data.test_values import (
    long_sorted_output,
    short_sorted_output,
    stylish_long_result,
    stylish_short_result,
)


def test_generate_stylish_view():
    assert generate_stylish_view(short_sorted_output) == stylish_short_result
    assert generate_stylish_view(long_sorted_output) == stylish_long_result

