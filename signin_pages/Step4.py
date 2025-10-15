from core.activities import click_on, match_element
from core.locators import *

def check_workOut(driver):
    work_outs = [
        Step_4.sedentary,
        Step_4.light_active,
        Step_4.moderately_active,
        Step_4.very_active,
        Step_4.super_active
    ]

    all_passed = True  # track overall result

    for work_out in work_outs:
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
                all_passed = False
        except Exception:
                # If element not found, it’s actually the pass case
                print(f"✅ Test case passed for {work_out} (User stayed on same page)")

    return all_passed
