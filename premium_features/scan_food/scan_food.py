import time
import json
from core.activities import click_on, match_element
from core.necessary_adb_commands import adb_tap_gallery
from premium_features.exercise.go_to_target_page import go_to_scan_food
from core.locators import scan_food, Nutrition

# -------------------------------
# Global Image Xpath mapping
# -------------------------------
IMAGE_SET = {
    1: scan_food.invalid_food_image,
    2: scan_food.valid_food_image,
    3: scan_food.blurry_food_image,
    4: scan_food.food_with_partial_object_image
}

# Path to JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Scan_food\image_data_set.json"

# -------------------------------
# Function to validate results


# -------------------------------
# Function to pick images from JSON
# -------------------------------
def pick_images(driver):
    """
    Pick each image from the gallery based on JSON dataset,
    map ID to locator, and validate results.
    """
    # Load JSON data
    with open(json_file_path, "r") as f:
        image_validation_data = json.load(f)["image_test_data"]

    for data in image_validation_data:
        image_id = data["image"]  # numeric
        expected = data["expected"]
        tc_id = data["tc_id"]
        message = data["description"].strip().lower()

        # Map image ID to locator
        locator = IMAGE_SET[image_id]

        print(f"Running test case: {tc_id}")

        # Open gallery
        click_on(driver, scan_food.gallery_icon, 60)
        click_on(driver, scan_food.collections_xpath, 60)
        click_on(driver, scan_food.favourites_xpath, 60)

        # Select image
        click_on(driver, locator, 60)

        # Click analysis
        click_on(driver, scan_food.analysis_button, 60)
        time.sleep(10)  # Replace with dynamic wait if possible

        # Validation
        if image_id == 1:
            check_message = match_element(driver, scan_food.message_for_invalid_food_image)
            check_message = check_message.strip().lower() if check_message else ""
            assert check_message == message, f"{tc_id} failed: Expected '{message}', got '{check_message}'"
        else:
            check_message = match_element(driver, Nutrition.message_for_valid_food)
            check_message = check_message.strip().lower() if check_message else ""
            assert message in check_message, f"{tc_id} failed: Expected '{message}' in '{check_message}'"

        # Go back for next test
        driver.back()
        click_on(driver, scan_food.retake_button)

            # For other images, you can do normal validation or continue


        # Go back to pick next image


# -------------------------------
# Main function to run scan food test
# -------------------------------
def check_scan_food(driver):
    # Navigate to scan food page
    go_to_scan_food(driver)
    time.sleep(0.4)

    # Run gallery image test using JSON dataset
    pick_images(driver)
