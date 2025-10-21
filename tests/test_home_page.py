import pytest

from features.home_page import is_element_visible, get_locator_by_title, load_home_page_test_data


@pytest.mark.parametrize("test_case", load_home_page_test_data())
def test_home_page_features(driver, test_case):
    title = test_case["title"]
    expected = test_case["expected"]
    tc_id = test_case["tc_id"]

    locator = get_locator_by_title(title)
    actual = is_element_visible(driver, locator)

    assert actual == expected, f"Test case {tc_id} failed: Expected {expected} but got {actual} for '{title}'"
