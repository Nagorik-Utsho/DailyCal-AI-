import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core.necessary_packages import *
def fill_input_field(driver, locator, value, index=0, timeout=30):
    """
    Clicks, clears, and sends keys to an input field at a given index.
    """
    wait = WebDriverWait(driver, timeout)
    fields = wait.until(EC.presence_of_all_elements_located(locator))
    if len(fields) <= index:
        raise Exception(f"Not enough input fields found (index {index})")
    field = fields[index]
    field.click()
    time.sleep(0.5)
    field.clear()
    field.send_keys(value)
    return field


import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def click_on(driver, locator_value, timeout=30, max_retries=3):
    """
    Clicks on an element safely, retrying if it becomes stale.

    Parameters:
        driver: Appium/Selenium driver
        locator_value: tuple like (By.XPATH, 'xpath_here')
        timeout: seconds to wait for element presence
        max_retries: number of retry attempts if element is stale
    """
    attempt = 0
    while attempt < max_retries:
        try:
            wait = WebDriverWait(driver, timeout)
            field = wait.until(EC.presence_of_element_located(locator_value))
            time.sleep(0.5)  # optional small pause before click
            field.click()
            return True
        except StaleElementReferenceException:
            attempt += 1
            print(f"[Warning] StaleElementReferenceException encountered. Retry {attempt}/{max_retries}")
            time.sleep(1)  # wait before retrying
        except TimeoutException:
            print(f"[Error] Element not found within {timeout} seconds: {locator_value}")
            raise
    # If still fails after retries
    raise StaleElementReferenceException(f"Failed to click on element after {max_retries} retries: {locator_value}")


def match_element(driver, locator_value,timeout=30) :
    wait=WebDriverWait(driver,timeout)
    field=wait.until(EC.presence_of_element_located((locator_value)))
    text=field.get_attribute('content-desc').strip().lower()
    return text


