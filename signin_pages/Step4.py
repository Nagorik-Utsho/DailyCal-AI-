
from core.activities import click_on, match_element
from core.driver_setup import setup_driver
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
    #Step_4.unhealthy_eating_habits,

]

def check_workOut(driver):


    all_passed = True  # track overall result

    for work_out in work_out_options:
        try:
            print(f"🟢 Clicking on workout option: {work_out}")
            click_on(driver, work_out)
            click_on(driver, Step_4.step_4_next_button)
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
            click_on(driver, Step_4.step_4_next_button)
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


def check_options_combinations(driver):
    all_passed = True  # track overall result

    for work_out in work_out_options:
        for blocking_progress in blocking_progress_options:
            try:
                print(f"🟢 Selecting combination: {work_out} + {blocking_progress}")

                # Select workout
                click_on(driver, work_out)

                # Select blocking progress
                click_on(driver, blocking_progress)

                # Click next to test if invalid navigation is allowed
                click_on(driver, Step_4.step_4_next_button)

                # Check if Step 5 appeared (invalid if it does)
                try:
                    match_element(driver, Step_5.step_no, 3)
                    print(f"✅ Combination correct: {work_out} + {blocking_progress} (Step 5 appeared)")
                    all_passed = False
                except Exception:
                    # Step 5 did not appear → correct behavior
                    print(f"❌ Invalid combination passed: {work_out} + {blocking_progress} (Stayed on Step 4)")

                # Go back to Step 4 for the next combination
                click_on(driver, common_button.back_navigation)

            except Exception as e:
                print(f"⚠️ Error with combination {work_out} + {blocking_progress}: {e}")
                all_passed = False

    return all_passed



def go_to_onetime_step5(driver):
    all_passed = True  # track overall result


    try:

        click_on(driver, Step_4.super_active)
    except Exception as e:
            print(f"⚠️ Failed to click on option ")


    try:
        click_on(driver, Step_4.lack_of_consistency)
        click_on(driver, Step_4.step_4_next_button)
    except Exception as e:
                print(f"⚠️ Failed to click on option")

            # Try to match Step 5 within 5 seconds
    try:
        title_step_5 = match_element(driver, Step_5.step_no, 5)


    except Exception:
                # If Step 5 not found, test failed
                print(
                    f"❌ Test case failed for combination")





def main():
    driver=setup_driver()
    check_options_combinations(driver)




if __name__ == "__main__":
        main()