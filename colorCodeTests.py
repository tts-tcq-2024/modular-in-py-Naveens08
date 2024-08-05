from ColorCodeFunctions import get_color_from_pair_number, get_pair_number_from_color
from GetColorCodeRefManual import get_color_coding_ref_manual

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def test_get_color_coding_ref_manual():
    expected_manual = (
        "Color Coding Reference Manual\n"
        "Pair Number | Major Color | Minor Color\n"
        "------------|-------------|------------\n"
        "          1 | White       | Blue\n"
        "          2 | White       | Orange\n"
        "          3 | White       | Green\n"
        "          4 | White       | Brown\n"
        "          5 | White       | Slate\n"
        "          6 | Red         | Blue\n"
        "          7 | Red         | Orange\n"
        "          8 | Red         | Green\n"
        "          9 | Red         | Brown\n"
        "         10 | Red         | Slate\n"
        "         11 | Black       | Blue\n"
        "         12 | Black       | Orange\n"
        "         13 | Black       | Green\n"
        "         14 | Black       | Brown\n"
        "         15 | Black       | Slate\n"
        "         16 | Yellow      | Blue\n"
        "         17 | Yellow      | Orange\n"
        "         18 | Yellow      | Green\n"
        "         19 | Yellow      | Brown\n"
        "         20 | Yellow      | Slate\n"
        "         21 | Violet      | Blue\n"
        "         22 | Violet      | Orange\n"
        "         23 | Violet      | Green\n"
        "         24 | Violet      | Brown\n"
        "         25 | Violet      | Slate\n"
    )
    
    actual_manual = get_color_coding_ref_manual()
    assert (actual_manual == expected_manual)
