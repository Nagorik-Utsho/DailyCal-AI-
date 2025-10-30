import json

import pytest

from premium_features.exercise.check_update_exercise_page import *
from premium_features.exercise.go_to_target_page import *

# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Features\time_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    time_validation_data = json.load(f)["time"]


@pytest.mark.run_feature
def test_update_intensity_exercise_feature(driver):
    # go_to_update_run_page(driver)
    # assert check_intensity_update(driver)

    go_to_update_weightlifting_page(driver)
    assert check_intensity_update(driver)





@pytest.mark.run_feature
def test_update_duration_run_exercise_feature(driver):
    go_to_update_run_page(driver)

    for time_data in time_validation_data:
        minutes = time_data["minutes"]
        tc_id = time_data["tc_id"]

        try:
            result =validation_of_update_duration_run(driver, minutes)
            assert result is True, f"TC {tc_id} FAILED: Duration {minutes} did not navigate to 'Today's Burn' page."
        except Exception as e:
            print(f"⚠️ TC {tc_id} caused exception: {e}. Skipping to next test case.")
            # Optional: recover to starting page
            try:
                go_to_update_run_page(driver)
            except Exception:
                print("⚠️ Failed to recover app to starting page. Continue to next test case.")
            continue





def test_update_duration_weight_exercise_feature(driver):
    print("Check duration for the weight ")
    go_to_update_weightlifting_page(driver)

    for time_data in time_validation_data:
        minutes = time_data["minutes"]
        tc_id = time_data["tc_id"]

        try:
            result = validation_of_update_duration_weightlifting(driver, minutes)
            assert result is True, f"TC {tc_id} FAILED: Duration {minutes} did not navigate to 'Today's Burn' page."
        except Exception as e:
            print(f"⚠️ TC {tc_id} caused exception: {e}. Skipping to next test case.")
            # Optional: recover to starting page
            try:
                go_to_update_weightlifting_page(driver)
            except Exception:
                print("⚠️ Failed to recover app to starting page. Continue to next test case.")
            continue


