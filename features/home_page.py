import os
import json
from selenium.webdriver.remote.webdriver import WebDriver

from core.activities import match_element
from core.locators import Home_page


def load_home_page_test_data():
    """Load test data from JSON."""
    # Set the full path to your JSON file
    json_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Home_page\home_page_test_data.json"

    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)["home_page_check"]



def is_element_visible(driver: WebDriver, locator, timeout=30) -> bool:
    """Return True if element is found within timeout, False otherwise."""
    try:
        element = match_element(driver, locator, timeout)
        return element is not None
    except Exception:
        return False


def get_locator_by_title(title: str):
    """Map JSON title to page object locator."""
    locator_map = {
        "daily progress": Home_page.daily_progress_section,
        "water settings": Home_page.water_section,
        "bmi": Home_page.current_weight_section,
        "today's burn": Home_page.today_burn_section,
        "activity logs": Home_page.activity_logs_title
    }
    if title not in locator_map:
        raise ValueError(f"Locator for '{title}' not defined in locator_map")
    return locator_map[title]
