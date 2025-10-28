import json
import pytest
from colorama import Fore, Style, init

from core.locators import Nutrition
from features.nutrition_page import validate_nutrition_title, validate_nutrition_increment
from premium_features.exercise.go_to_target_page import go_to_nutrition_page

init(autoreset=True)  # For colored output

# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Nutrition_page\nutrition_page_test_date.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    food_title_test_data = json.load(f)["food_name_field_test"]

@pytest.mark.run_feature
def test_update_nutrition_page(driver):
    go_to_nutrition_page(driver)

    failed_cases = []  # Collect failed test cases

    for data in food_title_test_data:
        title = data["text"]
        expected = data["expected"]
        tc_id = data["tc_id"]

        actual = validate_nutrition_title(driver, title)

        if actual == expected:
            print(f"{Fore.GREEN}✅ Test case {tc_id} passed: '{title}' matches expected '{expected}'")
        else:
            print(f"{Fore.RED}❌ Test case {tc_id} failed: '{title}' expected '{expected}', got '{actual}'")

            # Fail once at the end if there are any failed cases
        if failed_cases:
            failed_message = "\n".join(failed_cases)
            pytest.fail(f"\nSome test cases failed:\n{failed_message}")


import pytest
from colorama import Fore, Style, init

init(autoreset=True)


@pytest.mark.run_feature
def test_increment_food_amount_nutrition_page(driver):
    go_to_nutrition_page(driver)

    number_of_increment = 5

    # Run validation function
    validation_result = validate_nutrition_increment(driver, number_of_increment)

    # Assertion with colored pass/fail message
    if validation_result:
        print(
            f"{Fore.GREEN}✅ Test case passed: Calories increment validation successful for {number_of_increment} increments")
    else:
        print(
            f"{Fore.RED}❌ Test case failed: Calories increment validation failed for {number_of_increment} increments")

    # Pytest assert
    assert validation_result, f"Calories increment validation failed for {number_of_increment} increments"



@pytest.mark.run_feature
def test_decrement_food_amount_nutrition_page(driver) :

    number_of_decerement=2