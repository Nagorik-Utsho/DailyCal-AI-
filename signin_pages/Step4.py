from core.activities import click_on, match_element
from core.locators import *


"""Global options XPATH declaration"""
work_out_options = [
    Step_4.sedentary,
    Step_4.light_active,
    Step_4.moderately_active,
    Step_4.very_active,
    Step_4.super_active
]
blocking_progress_options=[
    Step_4.lack_of_consistency,
    Step_4.lack_of_support,
    Step_4.busy_schedule,
    Step_4.lack_of_meal_inspiration,
    Step_4.unhealthy_eating_habits,

]

def check_workOut(driver):


    all_passed = True  # track overall result

    for work_out in work_out_options:
        try:
            print(f"🟢 Clicking on workout option: {work_out}")
            click_on(driver, work_out)
            click_on(driver, common_button.next_button)
        except Exception as e:
            print(f"⚠️ Failed to click on option {work_out}: {e}")
            all_passed = False
            continue  # continue with the next option

            # Try to match Step 5
        try:
                title_step_5 = match_element(driver, Step_5.step_no, 5)
                # If Step 5 is found, test failed
                print(f"❌ Test case failed for {work_out} (User moved to Step 5)")
                click_on(driver, common_button.back_navigation)
                all_passed = False
        except Exception:
                # If element not found, it’s actually the pass case

                print(f"✅ Test case passed for {work_out} (User stayed on same page)")

    return all_passed






def check_blocking_progress(driver):


    all_passed = True  # track overall result

    for blocking_progress in blocking_progress_options:
        try:
            print(f"🟢 Clicking on workout option: {blocking_progress}")
            click_on(driver, blocking_progress)
            click_on(driver, common_button.next_button)
        except Exception as e:
            print(f"⚠️ Failed to click on option {blocking_progress}: {e}")
            all_passed = False
            continue  # continue with the next option

            # Try to match Step 5
        try:
                title_step_5 = match_element(driver, Step_5.step_no, 5)
                # If Step 5 is found, test failed
                print(f"❌ Test case failed for {blocking_progress} (User moved to Step 5)")
                click_on(driver, common_button.back_navigation)
                all_passed = False
        except Exception:
                # If element not found, it’s actually the pass case

                print(f"✅ Test case passed for {blocking_progress} (User stayed on same page)")

    return all_passed