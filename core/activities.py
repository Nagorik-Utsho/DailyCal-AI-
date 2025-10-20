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



def click_on(driver, locator_value,timeout=30):
    wait = WebDriverWait(driver, timeout)
    field = wait.until(EC.presence_of_element_located((locator_value)))
    time.sleep(0.5)
    field.click()



def match_element(driver, locator_value,timeout=30) :
    wait=WebDriverWait(driver,timeout)
    field=wait.until(EC.presence_of_element_located((locator_value)))
    text=field.get_attribute('content-desc').strip().lower()
    return text