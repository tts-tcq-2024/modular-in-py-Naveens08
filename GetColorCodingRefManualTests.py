from GetColorCodeRefManual import get_color_coding_ref_manual
from getColorCodingExpectedManual import get_expected_color_coding_manual

def test_get_color_coding_ref_manual():
    expected_manual = get_expected_color_coding_manual()
    actual_manual = get_color_coding_ref_manual()
    assert (actual_manual == expected_manual)
