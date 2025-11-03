import json
import random
import pytest
import logging

from colorama import Fore, Style
from features.water_settings_page import *
from premium_features.exercise.go_to_target_page import go_to_water_settings_page

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Water_settings\water_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    water_amount_data = json.load(f)["water_check"]


def log_test_result(tc_id, ml, actual, expected):
    """Helper function to log test results."""
    if actual == expected:
        logger.info(f"{Fore.GREEN}✅ {tc_id}: PASSED (Test data={ml}, Actual={actual}){Style.RESET_ALL}")
        return True
    else:
        logger.error(f"{Fore.RED}❌ {tc_id}: FAILED (Test data={ml}, Expected={expected}, Actual={actual}){Style.RESET_ALL}")
        return False


@pytest.mark.run_feature
def test_water_setting_functionality(driver):
    """Validate multiple water input values from JSON."""
    all_results = []
    reset_water_level(driver)
    for amount in water_amount_data:
        ml = amount["ml"]
        expected = amount["expected"]
        tc_id = amount["tc_id"]

        go_to_water_settings_page(driver)

        try:
            actual= validate_water_settings(driver, ml)
            result = log_test_result(tc_id, ml, actual, expected)
            all_results.append(result)
        except Exception as e:
            logger.error(f"{Fore.RED}❌ {tc_id}: ERROR ({e}){Style.RESET_ALL}")
            all_results.append(False)

    assert all(all_results), "Some water input test cases failed. Check logs for details."


@pytest.mark.run_feature
def test_water_increment_functionality(driver):
    """Test increment functionality for water values."""
    reset_water_level(driver)
    random_water_data = random.sample(water_amount_data, 2)
    ml_01 = random_water_data[0]["ml"]
    ml_02 = random_water_data[1]["ml"]

    #go_to_water_settings_page(driver)

    logger.info(f"Testing water increment: first={ml_01}, second={ml_02}")

    actual = water_increment_check(driver, ml_01, ml_02)
    expected = str(int(ml_01) + int(ml_02))

    if actual == expected:
        logger.info(f"{Fore.GREEN}✅ PASS: Actual ({actual}) matches Expected ({expected}){Style.RESET_ALL}")
    else:
        logger.error(f"{Fore.RED}❌ FAIL: Actual ({actual}) does not match Expected ({expected}){Style.RESET_ALL}")

    assert actual == expected


@pytest.mark.run_feature
def test_water_decrement_functionality(driver):
    """Test decrement functionality for water values."""
    reset_water_level(driver)
    random_water_data = random.sample(water_amount_data, 2)
    ml_01 = random_water_data[0]["ml"]
    ml_02 = random_water_data[1]["ml"]
    ml_03 = "200"

    #go_to_water_settings_page(driver)

    logger.info(f"Testing water decrement: first={ml_01}, second={ml_02}, third={ml_03}")

    actual = water_decrement_check(driver, ml_01, ml_02, ml_03)
    expected = str(int(ml_01) + int(ml_02) - int(ml_03))

    if actual == expected:
        logger.info(f"{Fore.GREEN}✅ PASS: Actual ({actual}) matches Expected ({expected}){Style.RESET_ALL}")
    else:
        logger.error(f"{Fore.RED}❌ FAIL: Actual ({actual}) does not match Expected ({expected}){Style.RESET_ALL}")

    assert actual == expected
