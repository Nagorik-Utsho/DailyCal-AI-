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





def validation_of_update_duration_run(driver, minutes):
    """
    Try updating the duration value.
    Returns True if 'Today's Burn' page appears within 5 seconds, otherwise False.
    """
    try:
        # Step 1: Select High intensity
        click_on(driver, intensity_set_duration.high_intensity)

        # Step 2: Enter duration and click update
        fill_input_field(driver, todays_burn.update_duration_input, minutes)
        driver.hide_keyboard()
        click_on(driver, intensity_set_duration.update_button)

        # Step 3: Check if navigation occurred within 5 seconds
        todays_burn_title = match_element(driver, todays_burn.todays_burn_page_title, timeout=5)

        if todays_burn_title:
            print(f"✅ [{minutes}] PASSED (page navigated within 5s)")
            click_on(driver, todays_burn.update_run)  # go back to main test page
            return True
        else:
            print(f"❌ [{minutes}] FAILED (page did not navigate within 5s)")
            return False

    except Exception as e:
        print(f"⚠️ Exception for '{minutes}': {e}")
        return False


def validation_of_update_duration_weightlifting(driver, minutes):
    """
    Try updating the duration value.
    Returns True if 'Today's Burn' page appears within 5 seconds, otherwise False.
    """
    try:
        # Step 1: Select High intensity
        click_on(driver, intensity_set_duration.high_intensity)

        # Step 2: Enter duration and click update
        fill_input_field(driver, todays_burn.update_duration_input, minutes)
        driver.hide_keyboard()
        click_on(driver, intensity_set_duration.update_button)

        # Step 3: Check if navigation occurred within 5 seconds
        todays_burn_title = match_element(driver, todays_burn.todays_burn_page_title, timeout=5)

        if todays_burn_title:
            print(f"✅ [{minutes}] PASSED (page navigated within 5s)")
            click_on(driver, todays_burn.update_weight_lifting)  # go back to main test page
            return True
        else:
            print(f"❌ [{minutes}] FAILED (page did not navigate within 5s)")
            return False

    except Exception as e:
        print(f"⚠️ Exception for '{minutes}': {e}")
        return False







def main():
    driver=setup_driver()
    go_to_update_run_page(driver)
    #check_intensity_update(driver)



if __name__ == "__main__":
        main()