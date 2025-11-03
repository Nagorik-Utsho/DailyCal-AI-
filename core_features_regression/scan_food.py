
from core.activities import click_on, fill_input_field, match_element
from core.driver_setup import setup_driver
from premium_features.exercise.go_to_target_page import go_to_scan_food
from core.locators import *
import re

def scan_food_functionality_check(driver):

    # 1. Go to home page
    go_to_scan_food(driver)

    # 2. Check picture from the gallery
    click_on(driver, scan_food.gallery_icon)

    # 3. Click on album
    click_on(driver, scan_food.collections_xpath)

    # 4. Go to favorite section
    click_on(driver, scan_food.favourites_xpath)

    # 5. Choose the image from the favorite
    click_on(driver, scan_food.valid_food_image)

    # 6. Click on analysis
    click_on(driver, scan_food.analysis_button)

    #7.increment the food number and read the calories
    click_on(driver,Nutrition.increment_button)

    calories = match_element(driver, Nutrition.total_calories)
    calories_number = re.findall(r'\d+', calories)
    if calories_number:
        calories = calories_number[0]
    else:
        calories = "0"
    print(f"Total calories: {calories}")


    time.sleep(10)

    # 8. Input the title
    fill_input_field(driver, Nutrition.food_title, "Test - 1")

    # 9. Hide keyboard if open
    try:
        driver.hide_keyboard()
    except Exception:
        pass

    # 10. Click done
    click_on(driver, Nutrition.done_button)
    time.sleep(5)

    # 11. Check if the activity log contains the title
    try:
        activity_list_food_title = match_element(driver, Home_page.testing_title_read, timeout=5)
        print("✅ The title is:", activity_list_food_title)
        return True , calories
    except TimeoutException:
        print("❌ Title not found in activity logs")
        return False






def main():
    driver=setup_driver()
    scan_food_functionality_check(driver)

if __name__ == '__main__' :
    main()





