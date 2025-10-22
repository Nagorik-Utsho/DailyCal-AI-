from selenium.webdriver.support.ui import WebDriverWait

from core.activities import fill_input_field, click_on, match_element
from core.locators import Update_goal_weight, Current_weight


def check_current_weight_page(driver):
    """
    Returns True if Current Weight page title is visible.
    Does NOT change page state.
    """
    try:
        match_element(driver, Current_weight.current_weight_page_title, 5)
        return True
    except Exception:
        return False


def validate_weight_input_field(driver, weight):
    """
    Fill the goal weight input field and click save.
    Wait until the page updates or any confirmation appears.
    """
    fill_input_field(driver, Update_goal_weight.update_goal_weight_input_field, weight)
    click_on(driver, Update_goal_weight.save_button)

    # Wait briefly to let page process the input
    WebDriverWait(driver, 5).until(lambda d: True)  # or replace with actual confirmation element
