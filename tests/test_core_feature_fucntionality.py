import time

from core.activities import click_on
from core_features_regression.exercise import  check_manual_duration_intensity, \
    check_preset_intensity_duration
from core_features_regression.scan_food import scan_food_functionality_check
from core.locators import *

import pytest


@pytest.mark.run_feature
def test_core_features(driver):
    # Run the validation
    result_scan_food = scan_food_functionality_check(driver)
    # Assert for pytest
    assert result_scan_food is True, "Food title not found in activity logs"
    print("Scan food functionality Tested")

    result = check_preset_intensity_duration(driver)
    assert result, "Test failed: Preset intensity & duration activity did not match expected values"
    print("Preset intensity & duration Tested")

    time.sleep(2)

    result = check_manual_duration_intensity(driver)
    assert result, "Test failed: Manual duration activity did not match expected values"
    print("Manual duration with intensity Tested")






