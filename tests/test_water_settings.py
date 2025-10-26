import json
import random

import pytest
from colorama import Fore, Style

from features.update_goal_weight_page import validate_weight_input_field, check_current_weight_page
from features.water_settings_page import *
from premium_features.exercise.go_to_target_page import go_to_update_goal_weight_page, go_to_water_settings_page

# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Water_settings\water_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    water_amount_data = json.load(f)["water_check"]


@pytest.mark.run_feature
def test_water_setting_functionality(driver):
    """
    Go to Water setting  page  and validate multiple test data.
    Continues running even if one fails.
    """



    all_results = []  # Track results to fail test at the end if needed

    # Step 2: Loop over all test data
    for amount in water_amount_data:
        ml = amount["ml"]
        expected = amount["expected"]
        tc_id = amount["tc_id"]

        # Step 1: Go to water setting page
        go_to_water_settings_page(driver)


        try:
            # Step 3: Fill input field and save
            actual = validate_water_settings(driver,ml)



            # If it navigates to current weight page, go back

            # Step 5: Assertion
            if actual == expected:
                print(f"{Fore.GREEN}✅ {tc_id}: PASSED (Test data ={ml}){Style.RESET_ALL}")
                all_results.append(True)
            else:
                print(f"{Fore.RED}❌ {tc_id}: FAILED (Test data={ml}, expected={expected}, actual={actual}){Style.RESET_ALL}")
                all_results.append(False)

        except Exception as e:
            print(f"{Fore.RED}❌ {tc_id}: ERROR ({e}){Style.RESET_ALL}")
            all_results.append(False)

    # Final assertion: mark test failed if any data set failed
    assert all(all_results), "Some test data failed. Check logs above for details."


@pytest.mark.run_feature
def test_water_increment_functionality(driver):
    # Pick 2 random water amounts
    random_water_data = random.sample(water_amount_data, 2)
    ml_01 = random_water_data[0]["ml"]
    ml_02 = random_water_data[1]["ml"]

    print(f"Sending first water value: {ml_01}")
    print(f"Sending second water value: {ml_02}")

    actual = water_increment_check(driver, ml_01, ml_02)
    expected = str(int(ml_01) + int(ml_02))

    if actual == expected:
        print(f"✅ PASS: Actual value ({actual}) matches expected ({expected})")
    else:
        print(f"❌ FAIL: Actual value ({actual}) does not match expected ({expected})")

    assert actual == expected



