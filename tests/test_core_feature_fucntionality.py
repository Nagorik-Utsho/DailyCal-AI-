import time

from core.activities import click_on
from core_features_regression.exercise import *
from core_features_regression.save_food import check_save_food_functionality
from core_features_regression.scan_food import scan_food_functionality_check
from core.locators import *

import pytest


@pytest.mark.run_feature
def test_core_features(driver):


    #1. Scan food functionality check
    result_scan_food = scan_food_functionality_check(driver)
    assert result_scan_food is True, "Food title not found in activity logs"
    print("Scan food functionality Tested")

    #2.Check the saved food functionality
    result_saved_food = check_save_food_functionality(driver)

    # Assertion
    assert "TEST - 1" in result_saved_food, "❌ Test failed: 'TEST - 1' not found in saved food"
    print("✅ Test passed: 'TEST - 1' is present in saved food")




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


    #time.sleep(2)
    # 5. Manual calories input functionality
    result = check_manual_calories(driver)
    if result:
        print("✅ Manual calories functionality is  Tested ")
    else:
        print("❌ Test failed: Manual calories value   did not match expected values ")
    assert result, "Test failed: Manual calories input activity did not match expected values"

    time.sleep(2)
    # 6. Describe exercise functionality check
    result = check_describe_exercise(driver)
    if result:
        print("✅ Describe exercise  is  Tested ")
    else:
        print("❌ Test failed: Describe exercise value   did not match expected values ")
    assert result, "Test failed: Describe exercise activity did not match expected values"


    time.sleep(2)

    #7. Today's burn section at the home page  update calories update check

    result=check_amount_today_burn(driver)

    if result == 300 :
        print("✅ Value updated at  the home page successfully ")

    else :
        print("❌ Test failed: Today's value   did not match expected values ")

    assert result, "Test failed: Expected updated value  did not match "







