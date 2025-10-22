import json
import pytest
from colorama import Fore, Style

from features.update_goal_weight_page import validate_weight_input_field, check_current_weight_page
from premium_features.exercise.go_to_target_page import go_to_update_goal_weight_page
from core.activities import click_on
from core.locators import Current_weight

# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Features\update_weight.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    goal_weight_validation_data = json.load(f)["update_goal_weight"]


@pytest.mark.run_feature
def test_update_goal_weight_functionality(driver):
    """
    Go to Update Goal Weight page once and validate multiple test data.
    Continues running even if one fails.
    """

    # Step 1: Go to Update Goal Weight page once
    go_to_update_goal_weight_page(driver)

    all_results = []  # Track results to fail test at the end if needed

    # Step 2: Loop over all test data
    for data in goal_weight_validation_data:
        weight = data["weight"]
        expected = data["expected"]
        tc_id = data["tc_id"]

        try:
            # Step 3: Fill input field and save
            validate_weight_input_field(driver, weight)

            # Step 4: Check the page or result
            actual = check_current_weight_page(driver)

            # If it navigates to current weight page, go back
            if actual:
                click_on(driver, Current_weight.update_goal_weight_button)

            # Step 5: Assertion
            if actual == expected:
                print(f"{Fore.GREEN}✅ {tc_id}: PASSED (weight={weight}){Style.RESET_ALL}")
                all_results.append(True)
            else:
                print(f"{Fore.RED}❌ {tc_id}: FAILED (weight={weight}, expected={expected}, actual={actual}){Style.RESET_ALL}")
                all_results.append(False)

        except Exception as e:
            print(f"{Fore.RED}❌ {tc_id}: ERROR ({e}){Style.RESET_ALL}")
            all_results.append(False)

    # Final assertion: mark test failed if any data set failed
    assert all(all_results), "Some test data failed. Check logs above for details."
