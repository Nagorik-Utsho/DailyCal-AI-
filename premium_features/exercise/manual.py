from core.activities import *
from core.locators import intensity_set_duration, Home_page
from core.necessary_packages import *
from premium_features.exercise.go_to_target_page import go_to_manual


def validate_manual_calories(driver):

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        JSON_PATH = os.path.join(BASE_DIR, "..", "..", "Test Data", "Features", "calories_data.json")

        print("Looking for JSON at:", JSON_PATH)
        if not os.path.exists(JSON_PATH):
            raise FileNotFoundError(f"JSON file not found: {JSON_PATH}")

        with open(JSON_PATH, "r", encoding="utf-8") as f:
            calories_data = json.load(f)

        for calories in calories_data["calories"]:
            calory = calories["calories"]
            expected = calories["expected"]
            tc_id = calories["tc_id"]

            print(f"\n--- Test Case: {tc_id} ---")
            print(f"Input: '{calory}' | Expected valid = {expected}")


            # Enter value safely
            #Here we have used the duration class input field and add button

            try:
                fill_input_field(driver, intensity_set_duration.duration_text_field, calory)
                driver.hide_keyboard()
                click_on(driver, intensity_set_duration.add_button)
            except Exception as e:
                print(f"⚠️ Error entering value {calory}: {e}")
                go_to_manual(driver)  # recover to starting page
                continue  # skip to next test case

            print(f"📄 {tc_id}: Entered time={time}")

            # Check if app navigated to Home page
            try:
                match_element(driver, Home_page.activity_logs_title, 3)
                # User navigated → test failed
                print(f"❌ Test case FAILED for {time} (User moved to Home page)")

                # Recover to starting page
                try:
                    go_to_manual(driver)
                except Exception as nav_error:
                    print(f"⚠️ Failed to navigate back: {nav_error}")

            except Exception:
                # User stayed → test passed
                print(f"✅ Test case PASSED for {time} (User stayed on the same page)")




def check_manual_calories_entry(driver):
    go_to_manual(driver)
    validate_manual_calories(driver)