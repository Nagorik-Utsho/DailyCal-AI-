import re
import time

from core.activities import scroll_in_scrollview, screen_swipe_gesture, swipe_up_mobile, fill_input_field, click_on, \
    match_element
from core.driver_setup import setup_driver
from core.locators import Nutrition, Home_page
from premium_features.exercise.go_to_target_page import go_to_nutrition_page

def validate_nutrition_title(driver, value):
    try:
        scroll_in_scrollview(driver)
        fill_input_field(driver, Nutrition.food_title, value)
        time.sleep(0.5)
        driver.hide_keyboard()
        click_on(driver, Nutrition.update_button)
        time.sleep(0.5)

        # Match content from the home page
        home_page = match_element(driver, Home_page.activity_logs_title)
        print(f"Home page title: {home_page}")

        # Check if expected text is present
        if "activity log" in home_page.lower():  # safer lowercase comparison
            go_to_nutrition_page(driver)
            return True
        else:

            return False
    except Exception as e:
        print(f"⚠️ Error validating '{value}'")
        return False  # return False if anything fails




def validate_nutrition_increment(driver, increment):
    # Get initial calories
    desc = match_element(driver, Nutrition.read_calories)
    print(f"Initial: {desc}")

    # Extract number
    match = re.search(r'(\d+)', desc)
    if match:
        calories = int(match.group(1))
        calories_expected = calories + (calories * increment)  # If each click adds the same calories
        print(f"Calories Expected: {calories_expected}")
    else:
        print(f"⚠️ Could not extract calories from: {desc}")
        return False

    # Click increment button n times
    for _ in range(increment):
        click_on(driver, Nutrition.increment_button)

    # Read updated calories
    desc_after = match_element(driver, Nutrition.read_calories)
    print(f"After increment: {desc_after}")

    match_after = re.search(r'(\d+)', desc_after)
    if match_after:
        calories_after_update = int(match_after.group(1))
        print(f"Actual Calories: {calories_after_update}")
    else:
        print(f"⚠️ Could not extract calories from: {desc_after}")
        return False

    # Validation
    if calories_expected == calories_after_update:
        print("✅ Calories increment validation passed")
        return True
    else:
        print("❌ Calories increment validation failed")
        return False



def validate_number_of_decrement(driver) :
    # Get initial calories
    increment = 4
    decrement = 2
    desc = match_element(driver, Nutrition.read_calories)
    print(f"Initial: {desc}")

    # Extract number
    match = re.search(r'(\d+)', desc)
    if match:
        calories = int(match.group(1))
        calories_incremented_expected = calories + (calories * decrement)  # If each click adds the same calories
        print(f"Calories Expected: { calories_incremented_expected}")
    else:
        print(f"⚠️ Could not extract calories from: {desc}")
        return False
    scroll_in_scrollview(driver)
    # Click increment button n times
    for _ in range(increment):
        click_on(driver, Nutrition.increment_button)








    # Read updated calories
    desc_after = match_element(driver, Nutrition.read_calories)
    print(f"After increment: {desc_after}")

    match_after = re.search(r'(\d+)', desc_after)
    if match_after:
        calories_after_update = int(match_after.group(1))
        print(f"Actual Calories: {calories_after_update}")
    else:
        print(f"⚠️ Could not extract calories from: {desc_after}")

    #Click on the Update button

    click_on(driver,Nutrition.update_button)





    go_to_nutrition_page(driver)


    #Decrement

    for _ in range(2) :
         click_on(driver,Nutrition.decrement_button)



    # Read updated calories
    desc_after = match_element(driver, Nutrition.read_calories)
    print(f"After increment: {desc_after}")

    match_after = re.search(r'(\d+)', desc_after)
    if match_after:
        calories_after_update = int(match_after.group(1))
        print(f"Actual Calories: {calories_after_update}")
    else:
        print(f"⚠️ Could not extract calories from: {desc_after}")





def validate_protein_update(driver, protein_data):
    try:
        # Clear previous value if any

        fill_input_field(driver, Nutrition.input_field_protein, protein_data)
        click_on(driver, Nutrition.protein_page_done_button)

        # Try to find the success message within 5 seconds
        try:
            title_check = match_element(driver, Nutrition.message_for_valid_food, 5)
            if "nutrition" in title_check.lower():
                print(f"[PASS] Protein '{protein_data}' validated successfully.")
                # Open edit protein page
                click_on(driver, Nutrition.edit_protein_page)
                return True
            else:
                print(f"[FAIL] Protein '{protein_data}' rejected unexpectedly.")
                return False

        except Exception:
            # If success message not found, assume invalid input
            print(f"[INFO] No success message for protein '{protein_data}'. Invalid input.")
            # Stay on the edit protein page (field already cleared for next test)
            return False

    except Exception as e:
        print(f"[ERROR] Exception while validating protein '{protein_data}'")
        return False





def validate_fat_update(driver, fat_data):
    try:
        # Clear previous value if any

        fill_input_field(driver, Nutrition.input_field_fats, fat_data)
        click_on(driver, Nutrition.fat_page_done_button)

        # Try to find the success message within 5 seconds
        try:
            title_check = match_element(driver, Nutrition.message_for_valid_food, 5)
            if "nutrition" in title_check.lower():
                print(f"[PASS] Fats '{fat_data}' validated successfully.")
                # Open edit Fats page
                click_on(driver, Nutrition.edit_fats_page)
                return True
            else:
                print(f"[FAIL] Fats '{fat_data}' rejected unexpectedly.")
                return False

        except Exception:
            # If success message not found, assume invalid input
            print(f"[INFO] No success message for Fat '{fat_data}'. Invalid input.")
            # Stay on the edit Fats page (field already cleared for next test)
            return False

    except Exception as e:
        print(f"[ERROR] Exception while validating Fats '{fat_data}'")
        return False




def validate_carbs_update(driver, carbs_data):
    try:
        # Clear previous value if any

        fill_input_field(driver, Nutrition.input_field_carbs, carbs_data)
        click_on(driver, Nutrition.carbs_page_done_button)

        # Try to find the success message within 5 seconds
        try:
            title_check = match_element(driver, Nutrition.message_for_valid_food, 5)
            if "nutrition" in title_check.lower():
                print(f"[PASS] Carbs '{carbs_data}' validated successfully.")
                # Open edit Carbs page
                click_on(driver, Nutrition.edit_carbs_page)
                return True
            else:
                print(f"[FAIL] Carbs '{carbs_data}' rejected unexpectedly.")
                return False

        except Exception:
            # If success message not found, assume invalid input
            print(f"[INFO] No success message for Carbs '{carbs_data}'. Invalid input.")
            # Stay on the edit Carbs page (field already cleared for next test)
            return False

    except Exception as e:
        print(f"[ERROR] Exception while validating Carbs '{carbs_data}'")
        return False








def check_nutrition_page(driver):
    go_to_nutrition_page(driver)





def main():
    driver=setup_driver()
    check_nutrition_page(driver)





if __name__ == "__main__":
        main()