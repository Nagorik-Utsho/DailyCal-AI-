from core.activities import fill_input_field, click_on, match_element
from core.locators import *
from core.necessary_packages import *
from premium_features.exercise.go_to_target_page import go_to_run

"""Global Intensity && Duration XPATH declaration"""
intensity_set=[
    intensity_set_duration.low_intensity,
    intensity_set_duration.medium_intensity,
    intensity_set_duration.high_intensity
]

duration_set = [

    intensity_set_duration.duration_15min,
    intensity_set_duration.duration_30min,
    intensity_set_duration.duration_60min,
    intensity_set_duration.duration_90min

]



def check_intensity(driver):
    all_passed = True  # track overall result

    for intensity_level in intensity_set:
        try:
            print(f"🟢 Clicking on Intensity option: {intensity_level}")
            click_on(driver, intensity_level)
            click_on(driver, intensity_set_duration.add_button)
        except Exception as e:
            print(f"⚠️ Failed to click on option {intensity_level}: {e}")
            all_passed = False
            continue  # continue with the next option

            # Try to match Step 5
        try:
            activity_logs = match_element(driver,Home_page.activity_logs_title, 5)
            # If activity log  title is  found, test failed
            print(f"❌ Test case failed for {intensity_level} (User moved to Step 5)")
            click_on(driver, common_button.back_navigation)
            all_passed = False
        except Exception:
            # If element not found, it’s actually the pass case

            print(f"✅ Test case passed for {intensity_level} (User stayed on same page)")

    return all_passed


def check_duration(driver):

    all_passed = True  # track overall result

    for duration in duration_set:
        try:
            print(f"🟢 Clicking on Intensity option: {duration}")
            click_on(driver, duration)
            click_on(driver, intensity_set_duration.add_button)
        except Exception as e:
            print(f"⚠️ Failed to click on option {duration}: {e}")
            all_passed = False
            continue  # continue with the next option

            # Try to match Step 5
        try:
            activity_logs = match_element(driver,Home_page.activity_logs_title, 5)
            # If activity log  title is  found, test failed
            print(f"❌ Test case failed for {duration} (User moved to Home page )")
            click_on(driver, common_button.back_navigation)
            all_passed = False
        except Exception:
            # If element not found, it’s actually the pass case

            print(f"✅ Test case passed for {duration} (User stayed on same page)")

    return all_passed


def validation_of_duration(driver):

    all_passed=True
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_PATH = os.path.join(BASE_DIR, "..", "..", "Test Data", "Features", "time_data.json")

    print("Looking for JSON at:", JSON_PATH)
    if not os.path.exists(JSON_PATH):
        raise FileNotFoundError(f"JSON file not found: {JSON_PATH}")

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        time_data = json.load(f)

    for time in time_data["time"]:
        minutes = time["minutes"]
        expected = time["expected"]
        tc_id = time["tc_id"]

        print(f"\n--- Test Case: {tc_id} ---")
        print(f"Input: '{minutes}' | Expected valid = {expected}")

        # Select intensity
        try:
            click_on(driver, intensity_set_duration.high_intensity)
        except Exception as e:
            print(f"⚠️ Failed to click on intensity: {e}")

        # Enter value safely
        try:
            fill_input_field(driver, intensity_set_duration.duration_text_field, minutes)
            driver.hide_keyboard()
            click_on(driver, intensity_set_duration.add_button)
        except Exception as e:
            print(f"⚠️ Error entering value {minutes}: {e}")
            go_to_run(driver)  # recover to starting page
            continue  # skip to next test case

        print(f"📄 {tc_id}: Entered time={time}")

        # Check if app navigated to Home page
        try:
            match_element(driver, Home_page.activity_logs_title, 3)
            # User navigated → test failed
            print(f"❌ Test case FAILED for {time} (User moved to Home page)")
            all_passed=False
            # Recover to starting page
            try:
                go_to_run(driver)
            except Exception as nav_error:
                print(f"⚠️ Failed to navigate back: {nav_error}")

        except Exception:
            # User stayed → test passed
            print(f"✅ Test case PASSED for {time} (User stayed on the same page)")


    return all_passed



def check_run_page(driver):
    go_to_run(driver)
    # Uncomment whichever validations you want to include
    #ntensity_result = check_intensity(driver)
    #duration_result = check_duration(driver)
    validation_result = validation_of_duration(driver)

    # Combine results (if any one fails, overall fails)
    overall_result = all([validation_result])

    print(f"✅ Overall result for Run feature: {overall_result}")
    return overall_result