from core.activities import click_on
from core_features.scan_food import scan_food_functionality_check
from core.locators import *

import pytest


@pytest.mark.run_feature
def test_core_features(driver):
    # Run the validation
    result = scan_food_functionality_check(driver)

    # Assert for pytest
    assert result is True, "Food title not found in activity logs"




