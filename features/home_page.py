import os
import json
from selenium.webdriver.remote.webdriver import WebDriver

from core.activities import match_element
from core.driver_setup import setup_driver
from core.locators import Home_page
import re

def read_information_from_daily_progressbar(driver):
    actual = match_element(driver, Home_page.daily_progress_section)

    # Use regex to find the number that appears before "calories"
    match = re.search(r'(\d+)\s*calories', actual, re.IGNORECASE)
    if match:
        total_calories = match.group(1)
        print("Total calories:", total_calories)
        return total_calories
    else:
        print("Calories not found")



def read_calories_burn_from_activity_log_run(driver):
    actual=match_element(driver,Home_page.read_burn_calories_run)
    # Use regex to find the number that appears before "calories"
    match = re.search(r'(\d+)\s*calories', actual, re.IGNORECASE)
    if match:
        run_burned_calories = match.group(1)
        print("Burned calories : ", run_burned_calories)
        return run_burned_calories
    else:
        print("Calories not found")

def main():
    driver=setup_driver()
    #read_information_from_daily_progressbar(driver)
    read_calories_burn_from_activity_log(driver)


if __name__ == "__main__":
        main()