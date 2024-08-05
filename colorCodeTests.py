from ColorCodeFunctions import get_color_from_pair_number, get_pair_number_from_color
from printColorCodeManual import print_color_coding_manual

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def test_print_color_coding_manual():
    manual = get_color_coding_ref_manual()
    print(manual)
