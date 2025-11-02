import json
import pytest
import logging
from colorama import Fore, Style

from features.update_current_weight_page import validate_weight_input_field, check_current_weight_page
from premium_features.exercise.go_to_target_page import go_to_update_current_weight_page
from core.activities import click_on
from core.locators import Current_weight

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Features\update_weight.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    goal_weight_validation_data = json.load(f)["update_weight"]

@pytest.mark.run_feature
def test_update_current_weight_functionality(driver):
    """
    Regression test for updating goal weight with multiple test cases.
    Goes to Update Goal Weight page once, iterates through all test data,
    and continues execution even if one fails (soft assertion style).
    """

    # Step 1: Go to Update Goal Weight page once
    go_to_update_current_weight_page(driver)

    failures = []  # Collect all failures

    # Helper function for logging each test case
    def verify_weight(tc_id, weight, expected):
        try:
            # Fill input and validate
            validate_weight_input_field(driver, weight)

            # Check the current weight page
            actual = check_current_weight_page(driver)

            # Navigate back if needed
            if actual:
                click_on(driver, Current_weight.update_goal_weight_button)

            if actual == expected:
                logger.info(f"✅ {tc_id}: PASSED (weight={weight})")
                print(f"{Fore.GREEN}✅ {tc_id}: PASSED (weight={weight}){Style.RESET_ALL}")
                return True
            else:
                msg = f"{tc_id}: FAILED (weight={weight}, expected={expected}, actual={actual})"
                logger.error(f"❌ {msg}")
                print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")
                failures.append(msg)
                return False

        except Exception as e:
            msg = f"{tc_id}: ERROR ({e})"
            logger.error(f"❌ {msg}")
            print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")
            failures.append(msg)
            return False

    # Iterate over all test data
    for data in goal_weight_validation_data:
        verify_weight(data["tc_id"], data["weight"], data["expected"])

    # Final soft assertion
    assert not failures, "Some weight update test cases failed:\n" + "\n".join(failures)
