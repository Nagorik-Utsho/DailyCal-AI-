import json
import os

from core.activities import *
from core.locators import *
from core.driver_setup import *
from signin_pages.Step1 import validation_of_birthdate


def go_to_target_page(driver):
    """
    Navigate by clicking the Next button 3 times
    """
    print("Navigating to target page...")
    for i in range(3):
        click_on(driver, OnBoarding.next_button)



def select_gender(driver):
    print("Selecting gender")
    click_on(driver,Step_1.male)


def validate_birthdate(driver):
        validation_of_birthdate(driver)


def step_1_checking(driver):
    go_to_target_page(driver)
    select_gender(driver)
    validate_birthdate(driver)

# def main():
#     driver=setup_driver()
#     step_1_checking(driver)
#
#
#
# if __name__ == "__main__":
#         main()