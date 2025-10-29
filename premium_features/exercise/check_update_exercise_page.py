import json
import os
from re import match

from core.activities import click_on, fill_input_field, match_element
from core.driver_setup import setup_driver
from core.locators import intensity_set_duration, common_button, Home_page, todays_burn
from premium_features.exercise.go_to_target_page import go_to_run, go_to_update_run_page

"""Global Intensity && Duration XPATH declaration"""
intensity_set=[
    intensity_set_duration.low_intensity,
    intensity_set_duration.medium_intensity,
    intensity_set_duration.high_intensity
]

duration_set = [

    intensity_set_duration.duration_90min,
    intensity_set_duration.duration_15min,
    intensity_set_duration.duration_30min,
    intensity_set_duration.duration_60min,


]



def check_intensity_update(driver):
    """
    For each intensity in intensity_set:
        - select intensity
        - for each duration in duration_set:
            - select duration
            - click update
            - verify the 'Today's Burn' page title
            - if found: pass, then go back via update_run
            - if not found: fail
    """
    results = []  # collect (intensity, duration, result)

    for intensity_level in intensity_set:
        try:
            print(f"🟢 Clicking on Intensity option: {intensity_level}")
            click_on(driver, intensity_level)
        except Exception as e:
            print(f"⚠️ Failed to click on intensity option {intensity_level}: {e}")
            results.append((intensity_level, None, "FAILED - click intensity"))
            continue

        for duration in duration_set:
            try:
                print(f"🟢 Clicking on Duration option: {duration}")
                click_on(driver, duration)
                click_on(driver, intensity_set_duration.update_button)

                # Wait for the next page
                todays_burn_title = match_element(driver, todays_burn.todays_burn_page_title, timeout=5)
                print(todays_burn_title)
                if todays_burn_title:
                    print(f"✅ Test case PASSED for Intensity '{intensity_level}' and Duration '{duration}'")
                    results.append((intensity_level, duration, "PASSED"))

                    # Navigate back to update page
                    click_on(driver, todays_burn.update_run)
                else:
                    print(f"❌ Test case FAILED (title not found) for Duration '{duration}'")
                    results.append((intensity_level, duration, "FAILED - no title"))
            except Exception as e:
                print(f"❌ Exception during test for Duration '{duration}': {e}")
                results.append((intensity_level, duration, f"FAILED - exception: {e}"))

    # Optional summary
    print("\n==== Test Summary ====")
    for intensity, duration, result in results:
        print(f"Intensity: {intensity}, Duration: {duration}, Result: {result}")

    return results





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
            click_on(driver, intensity_set_duration.update_button)
        except Exception as e:
            print(f"⚠️ Error entering value {minutes}: {e}")
            go_to_run(driver)  # recover to starting page
            continue  # skip to next test case

        print(f"📄 {tc_id}: Entered time={time}")

        # Determine actual app behavior
        app_on_home = False
        # Check if app navigated to Home page
        try:
            match_element(driver, Home_page.activity_logs_title, 3)
            app_on_home = True
            # User navigated → test failed
            print(f"❌ Test case FAILED for {time} (User moved to Home page)")
            # Recover to starting page

        except Exception:
            # User stayed → test passed
            app_on_home = False
            print(f"✅ Test case PASSED for {time} (User stayed on the same page)")

        # Compare expected vs actual
        if expected:  # Value should be valid → app should go Home
            if app_on_home:
                print(f"✅ Test case PASSED for {tc_id} (valid value registered, went Home)")
            else:
                print(f"❌ Test case FAILED for {tc_id} (valid value not registered, stayed on Run)")
                all_passed = False
        else:  # Value should be invalid → app should stay on Run
            if app_on_home:
                print(f"❌ Test case FAILED for {tc_id} (invalid value allowed, went Home)")
                all_passed = False
            else:
                print(f"✅ Test case PASSED for {tc_id} (invalid value blocked, stayed on Run)")


        # Recover to Run page for next iteration if needed
        if app_on_home:
            try:
                go_to_run(driver)
                print("🔄 Returned to Run page for next test")
            except Exception as nav_error:
                print(f"⚠️ Failed to navigate back to Run page: {nav_error}")
                all_passed = False


    return all_passed




def main():
    driver=setup_driver()
    go_to_update_run_page(driver)
    check_intensity_update(driver)



if __name__ == "__main__":
        main()