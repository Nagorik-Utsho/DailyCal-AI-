
from core.activities import click_on, fill_input_field, match_element
from premium_features.exercise.go_to_target_page import go_to_scan_food
from core.locators import *

def scan_food_functionality_check(driver):

    # 1. Go to home page
    go_to_scan_food(driver)

    # 2. Check picture from the gallery
    click_on(driver, scan_food.gallery_icon)

    # 3. Click on album
    click_on(driver, scan_food.albums)

    # 4. Go to favorite section
    click_on(driver, scan_food.favourite_group)

    # 5. Choose the image from the favorite
    click_on(driver, scan_food.choose_image_picture)

    # 6. Click on analysis
    click_on(driver, scan_food.analysis_button)

    time.sleep(10)

    # 7. Input the title
    fill_input_field(driver, Nutrition.food_title, "Test - 1")

    # 8. Hide keyboard if open
    try:
        driver.hide_keyboard()
    except Exception:
        pass

    # 9. Click done
    click_on(driver, Nutrition.done_button)
    time.sleep(5)

    # 10. Check if the activity log contains the title
    try:
        activity_list_food_title = match_element(driver, Home_page.testing_title_read, timeout=5)
        print("✅ The title is:", activity_list_food_title)
        return True
    except TimeoutException:
        print("❌ Title not found in activity logs")
        return False












