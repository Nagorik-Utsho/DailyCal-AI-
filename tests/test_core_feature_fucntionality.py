import time

from core.activities import click_on
from core_features_regression.exercise import *
from core_features_regression.scan_food import scan_food_functionality_check
from core.locators import *

import pytest


@pytest.mark.run_feature
def test_core_features(driver):

    #
    # #1. Scan food functionality check
    # result_scan_food = scan_food_functionality_check(driver)
    # assert result_scan_food is True, "Food title not found in activity logs"
    # print("Scan food functionality Tested")
    #
    #
    # 1️⃣ Run functionality check — Preset
    result = check_run_preset_intensity_duration(driver)
    if result:
        print("✅ Preset intensity & duration Tested (Run)")
    else:
        print("❌ Test failed: Preset intensity & duration activity did not match expected values (Run)")
    assert result, "Test failed: Preset intensity & duration activity did not match expected values"

    time.sleep(2)

    # 2️⃣ Run functionality check — Manual
    result = check_run_manual_duration_intensity(driver)
    if result:
        print("✅ Manual duration with intensity Tested (Run)")
    else:
        print("❌ Test failed: Manual duration activity did not match expected values (Run)")
    assert result, "Test failed: Manual duration activity did not match expected values"
    time.sleep(2)

    # 3️⃣ Weight lifting functionality — Preset
    result = check_weight_preset_intensity_duration(driver)
    if result:
        print("✅ Preset intensity & duration Tested for Weight Lifting")
    else:
        print("❌ Test failed: Preset intensity & duration activity did not match expected values (Weight Lifting)")
    assert result, "Test failed: Preset intensity & duration activity did not match expected values"


    time.sleep(2)
    # 4️⃣ Weight lifting functionality — Manual
    result = check_weight_manual_duration_intensity(driver)
    if result:
        print("✅ Manual duration with intensity Tested (Weight Lifting)")
    else:
        print("❌ Test failed: Manual duration activity did not match expected values (Weight Lifting)")
    assert result, "Test failed: Manual duration activity did not match expected values"








