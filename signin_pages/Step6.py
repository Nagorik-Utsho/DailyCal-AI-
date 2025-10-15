
from core.activities import click_on, match_element
from core.locators import *


"""Global options XPATH declaration"""
specific_diet_options = [
    Step_6.classic,
    Step_6.pescatarian,
    Step_6.vegetarian,
    Step_6.vegan
]

accomplishment_options=[
    Step_6.option_1,
    Step_6.option_2,
    Step_6.option_3,
    Step_6.option_4

]

def check_diet_options(driver):


    all_passed = True  # track overall result

    for diet in specific_diet_options:
        try:
            print(f"🟢 Clicking on workout option: {diet}")
            click_on(driver, diet)
            click_on(driver, common_button.next_button)
        except Exception as e:
            print(f"⚠️ Failed to click on option {diet}: {e}")
            all_passed = False
            continue  # continue with the next option

            # Try to match Step 5
        try:
                final_page = match_element(driver,All_information.all_done, 5)
                # If Step 5 is found, test failed
                print(f"❌ Test case failed for {diet} (User moved to Step 5)")
                click_on(driver, common_button.back_navigation)
                all_passed = False
        except Exception:
                # If element not found, it’s actually the pass case

                print(f"✅ Test case passed for {diet} (User stayed on same page)")

    return all_passed






# def check_blocking_progress(driver):
#
#
#     all_passed = True  # track overall result
#
#     for blocking_progress in blocking_progress_options:
#         try:
#             print(f"🟢 Clicking on workout option: {blocking_progress}")
#             click_on(driver, blocking_progress)
#             click_on(driver, common_button.next_button)
#         except Exception as e:
#             print(f"⚠️ Failed to click on option {blocking_progress}: {e}")
#             all_passed = False
#             continue  # continue with the next option
#
#             # Try to match Step 5
#         try:
#                 title_step_5 = match_element(driver, Step_5.step_no, 5)
#                 # If Step 5 is found, test failed
#                 print(f"❌ Test case failed for {blocking_progress} (User moved to Step 5)")
#                 click_on(driver, common_button.back_navigation)
#                 all_passed = False
#         except Exception:
#                 # If element not found, it’s actually the pass case
#
#                 print(f"✅ Test case passed for {blocking_progress} (User stayed on same page)")
#
#     return all_passed
#
#
#
#
#
# def check_options_combinations(driver):
#         all_passed = True  # track overall result
#
#         for work_out in work_out_options:
#             try:
#                 print(f"🟢 Clicking on workout option: {work_out}")
#                 click_on(driver, work_out)
#             except Exception as e:
#                 print(f"⚠️ Failed to click on option {work_out}: {e}")
#                 all_passed = False
#                 continue  # move to next work_out
#
#             for blocking_progress in blocking_progress_options:
#                 try:
#                     print(f"🟢 Clicking on blocking progress option: {blocking_progress}")
#                     click_on(driver, blocking_progress)
#                     click_on(driver, common_button.next_button)
#                 except Exception as e:
#                     print(f"⚠️ Failed to click on option {blocking_progress}: {e}")
#                     all_passed = False
#                     continue  # move to next blocking_progress
#
#                 # Try to match Step 5 within 5 seconds
#                 try:
#                     title_step_5 = match_element(driver, Step_5.step_no, 5)
#                     # If Step 5 found, test passed
#                     print(f"✅ Test case passed for combination: {work_out} + {blocking_progress} (Step 5 appeared)")
#                     click_on(driver, common_button.back_navigation)  # go back to try next combination
#                 except Exception:
#                     # If Step 5 not found, test failed
#                     print(
#                         f"❌ Test case failed for combination: {work_out} + {blocking_progress} (Step 5 did not appear)")
#                     all_passed = False
#
#         return all_passed
#
#
# def check_one_time_step_4(driver):
#     all_passed = True  # track overall result
#
#
#     try:
#
#         click_on(driver, Step_4.super_active)
#     except Exception as e:
#             print(f"⚠️ Failed to click on option ")
#
#
#     try:
#         click_on(driver, Step_4.unhealthy_eating_habits)
#         click_on(driver, common_button.next_button)
#     except Exception as e:
#                 print(f"⚠️ Failed to click on option")
#
#             # Try to match Step 5 within 5 seconds
#     try:
#         title_step_5 = match_element(driver, Step_5.step_no, 5)
#
#     except Exception:
#                 # If Step 5 not found, test failed
#                 print(
#                     f"❌ Test case failed for combination")




