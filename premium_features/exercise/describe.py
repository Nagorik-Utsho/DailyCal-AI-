from core.activities import *
from core.locators import intensity_set_duration, Home_page, describe_exercise
from core.necessary_packages import *
from premium_features.exercise.go_to_target_page import go_to_manual, go_to_describe


def validate_describe_calories(driver):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_PATH = os.path.join(BASE_DIR, "..", "..", "Test Data", "Features", "describe_exercise_data.json")

    print("Looking for JSON at:", JSON_PATH)
    if not os.path.exists(JSON_PATH):
        raise FileNotFoundError(f"JSON file not found: {JSON_PATH}")

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        describe_exercise_data = json.load(f)
    for test_case in describe_exercise_data["describe_exercise"]:
        prompt = test_case["input"]
        expected = test_case["expected"]
        tc_id = test_case["tc_id"]

        if prompt is None:
            print(f"⚠️ Skipping test case {tc_id} because input is None")
            go_to_describe(driver)
            continue

        print(f"\n--- Test Case: {tc_id} ---")
        print(f"Input: '{prompt}' | Expected valid = {expected}")

        try:
            fill_input_field(driver, describe_exercise.describe_text_field, prompt)
            driver.hide_keyboard()
            click_on(driver, describe_exercise.add_button)
        except Exception as e:
            print(f"⚠️ Error entering value {prompt}: {e}")
            go_to_describe(driver)
            continue

        ...

        # Step 4: Check if app navigated to Home page
        try:
            match_element(driver, Home_page.activity_logs_title, 3)
            # User navigated → test failed
            print(f"❌ Test case FAILED for {prompt} (User moved to Home page)")

            # Recover to starting page
            try:
                go_to_describe(driver)
            except Exception as nav_error:
                print(f"⚠️ Failed to navigate back: {nav_error}")

        except Exception:
            # User stayed → test passed
            print(f"✅ Test case PASSED for {prompt} (User stayed on the same page)")


def check_describe_calories_entry(driver):
    go_to_describe(driver)
    validate_describe_calories(driver)
