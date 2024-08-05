from constantColorValues import MAJOR_COLORS, MINOR_COLORS
from ColorCodeFunctions import get_color_from_pair_number

def get_color_coding_ref_manual():
    manual = "Color Coding Reference Manual\n"
    manual += "Pair Number | Major Color | Minor Color\n"
    manual += "------------|-------------|------------\n"
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        manual += f'{pair_number:11} | {major_color:12} | {minor_color}\n'
    return manual
