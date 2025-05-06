from gendiff.scripts.generate_diff import (
    converter,
    generate_diff,
    generate_difference,
    sort_output,
)
from tests.test_data.test_values import (
    FIRST_LONG_FILE,
    FIRST_LONG_FILEPATH,
    FIRST_SHORT_FILE,
    FIRST_SHORT_FILEPATH,
    GENDIFF_LONG_RESULT,
    GENDIFF_SHORT_RESULT,
    LONG_SORTED_OUTPUT,
    PLAIN_LONG_RESULT,
    PLAIN_SHORT_RESULT,
    SECOND_LONG_FILE,
    SECOND_LONG_FILEPATH,
    SECOND_SHORT_FILE,
    SECOND_SHORT_FILEPATH,
    SHORT_SORTED_OUTPUT,
    STYLISH_LONG_RESULT,
    STYLISH_SHORT_RESULT,
)


def test_main_stylish_long():
    assert generate_diff(FIRST_LONG_FILEPATH, SECOND_LONG_FILEPATH,
                 "stylish") == STYLISH_LONG_RESULT
    

def test_main_stylish_short():
    assert generate_diff(FIRST_SHORT_FILEPATH, SECOND_SHORT_FILEPATH,
                 "stylish") == STYLISH_SHORT_RESULT
    

def test_main_plain_long():
    assert generate_diff(FIRST_LONG_FILEPATH, SECOND_LONG_FILEPATH,
                 "plain") == PLAIN_LONG_RESULT
    

def test_main_plain_short():
    assert generate_diff(FIRST_SHORT_FILEPATH, SECOND_SHORT_FILEPATH,
                 "plain") == PLAIN_SHORT_RESULT


def test_generate_difference_short():
    assert generate_difference(FIRST_SHORT_FILE,
                                SECOND_SHORT_FILE) == GENDIFF_SHORT_RESULT
    

def test_generate_difference_long():
    assert generate_difference(FIRST_LONG_FILE,
                                SECOND_LONG_FILE) == GENDIFF_LONG_RESULT


def test_sort_output_short():
    assert sort_output(GENDIFF_SHORT_RESULT) == SHORT_SORTED_OUTPUT


def test_sort_output_long():
    assert sort_output(GENDIFF_LONG_RESULT) == LONG_SORTED_OUTPUT


def test_converter():
    assert converter({"id": {"value": 45}}) == [
        ['   ', 'id:', [['   ', 'value:', '45']]]]


