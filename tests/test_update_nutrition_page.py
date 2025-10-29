import json
import pytest
from colorama import Fore, Style, init

from core.activities import click_on
from core.locators import Nutrition
from features.nutrition_page import validate_nutrition_title, validate_nutrition_increment, validate_protein_update, \
    validate_carbs_update, validate_fat_update
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





# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Nutrition_page\nutrition_page_test_date.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    protein_test_data = json.load(f)["protein_update_test"]

@pytest.mark.run_feature
def test_update_protein_nutrition_page(driver):
    go_to_nutrition_page(driver)
    # Open edit protein page


    failed_cases = []
    click_on(driver, Nutrition.edit_protein_page)
    for protein in protein_test_data:
        protein_data = protein["protein"]
        expected = protein["expected"]
        tc_id = protein["tc_id"]

        # Call your existing validation function
        actual = validate_protein_update(driver, protein_data)

        try:
            # Assertion: compare actual result with expected
            assert actual == expected
            print(f"✅[PASS] {tc_id}: Protein '{protein_data}' validated successfully.")

        except AssertionError:
            print(f"❌[FAIL] {tc_id}: Protein '{protein_data}' validation failed. Expected={expected}, Actual={actual}")
            failed_cases.append(tc_id)  # Track failed cases but continue testing

    # At the end, fail the pytest test if any case failed
    if failed_cases:
        pytest.fail(f"Some protein validation test cases failed: {failed_cases}")




# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Nutrition_page\nutrition_page_test_date.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    fat_test_data = json.load(f)["fat_update_test"]
@pytest.mark.run_feature
def test_update_fat_nutrition_page(driver):
    go_to_nutrition_page(driver)
    # Open edit protein page


    failed_cases = []
    click_on(driver, Nutrition.edit_fats_page)
    for fat in fat_test_data:
        fat_data = fat["fat"]
        expected = fat["expected"]
        tc_id = fat["tc_id"]

        # Call your existing validation function
        actual = validate_fat_update(driver, fat_data)

        try:
            # Assertion: compare actual result with expected
            assert actual == expected
            print(f"✅[PASS] {tc_id}: Protein '{fat_data}' validated successfully.")

        except AssertionError:
            print(f"❌[FAIL] {tc_id}: Protein '{fat_data}' validation failed. Expected={expected}, Actual={actual}")
            failed_cases.append(tc_id)  # Track failed cases but continue testing

    # At the end, fail the pytest test if any case failed
    if failed_cases:
        pytest.fail(f"Some protein validation test cases failed: {failed_cases}")






# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Nutrition_page\nutrition_page_test_date.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    carbs_test_data = json.load(f)["carbs_update_test"]
@pytest.mark.run_feature
def test_update_carbs_nutrition_page(driver):
    go_to_nutrition_page(driver)



    failed_cases = []
    click_on(driver, Nutrition.edit_carbs_page)
    for carbs in carbs_test_data:
        carbs_data = carbs["carbs"]
        expected = carbs["expected"]
        tc_id = carbs["tc_id"]

        # Call your existing validation function
        actual = validate_carbs_update(driver, carbs_data)

        try:
            # Assertion: compare actual result with expected
            assert actual == expected
            print(f"✅[PASS] {tc_id}: Carbs '{carbs_data}' validated successfully.")

        except AssertionError:
            print(f"❌[FAIL] {tc_id}: Carbs '{carbs_data}' validation failed. Expected={expected}, Actual={actual}")
            failed_cases.append(tc_id)  # Track failed cases but continue testing

    # At the end, fail the pytest test if any case failed
    if failed_cases:
        pytest.fail(f"Some protein validation test cases failed: {failed_cases}")











