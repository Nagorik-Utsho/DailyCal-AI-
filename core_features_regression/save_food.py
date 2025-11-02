import time

from core.activities import click_on, match_element
from core.driver_setup import setup_driver
from core.locators import Home_page, Save_food
from premium_features.exercise.go_to_target_page import go_to_saved_food


def check_save_food_functionality(driver):

    #1. Click on the target food
    click_on(driver,Home_page.testing_title_read)

    #2. Click on the save button
    click_on(driver,Save_food.saved_icon)
    time.sleep(.3)

    #3. Click on the back navigation
    driver.back()

    #4. Go to  the features page
    go_to_saved_food(driver)

    #4. Capture the title
    actual = match_element(driver,Save_food.testing_food_title).upper()

    print(actual)

    return actual



def main():
    driver=setup_driver()

    check_save_food_functionality(driver)

if __name__ == "__main__":
    main()
