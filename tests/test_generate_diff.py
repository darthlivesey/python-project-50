from gendiff.scripts.generate_diff import (
    converter,
    generate_difference,
    main,
    sort_output,
)
from tests.test_data.test_values import (
    first_long_file,
    first_short_file,
    gendiff_long_result,
    gendiff_short_result,
    long_sorted_output,
    plain_long_result,
    plain_short_result,
    second_long_file,
    second_short_file,
    short_sorted_output,
    stylish_long_result,
    stylish_short_result,
)


def test_main():
    assert main(first_long_file, second_long_file,
                 "stylish") == stylish_long_result
    assert main(first_short_file, second_short_file,
                 "stylish") == stylish_short_result
    assert main(first_long_file, second_long_file,
                 "plain") == plain_long_result
    assert main(first_short_file, second_short_file,
                 "plain") == plain_short_result


def test_generate_difference():
    assert generate_difference(first_short_file,
                                second_short_file) == gendiff_short_result
    assert generate_difference(first_long_file,
                                second_long_file) == gendiff_long_result


def test_sort_output():
    assert sort_output(gendiff_short_result) == short_sorted_output
    assert sort_output(gendiff_long_result) == long_sorted_output


def test_converter():
    assert converter({"id": {"value": 45}}) == [
        ['   ', 'id:', [['   ', 'value:', '45']]]]


