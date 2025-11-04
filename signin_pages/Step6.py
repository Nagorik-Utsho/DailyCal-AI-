
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
            print(f"🟢 Clicking on diet option: {diet}")
            click_on(driver, diet)
            click_on(driver, common_button.next_button)
        except Exception as e:
            print(f"⚠️ Failed to click on option {diet}: {e}")
            all_passed = False
            continue  # continue with the next option

            # Try to match Final page
        try:
                final_page = match_element(driver,All_information.all_done, 5)
                # If Final page is found, test failed
                print(f"❌ Test case failed for {diet} (User moved to Final page )")
                click_on(driver, common_button.back_navigation)
                all_passed = False
        except Exception:
                # If element not found, it’s actually the pass case

                print(f"✅ Test case passed for {diet} (User stayed on same page)")

    return all_passed






def check_accomplishment_options(driver):


    all_passed = True  # track overall result

    for accomplishment in accomplishment_options:
        try:
            print(f"🟢 Clicking on accomplishment option: {accomplishment}")
            click_on(driver, accomplishment)
            click_on(driver, common_button.next_button)
        except Exception as e:
            print(f"⚠️ Failed to click on option {accomplishment}: {e}")
            all_passed = False
            continue  # continue with the next option

            # Try to match Final page
        try:
                final_page = match_element(driver, All_information.all_done, 5)
                # If Step final page is found, test failed
                print(f"❌ Test case failed for {accomplishment} (User moved to Final page)")
                click_on(driver, common_button.back_navigation)
                all_passed = False
        except Exception:
                # If element not found, it’s actually the pass case

                print(f"✅ Test case passed for {accomplishment} (User stayed on same page)")

    return all_passed





def check_options_combinations_step_6(driver):
    all_passed = True  # track overall result

    for diet in specific_diet_options:
        for accomplish in accomplishment_options:
            try:
                print(f"🟢 Selecting combination: {diet} + {accomplish}")

                # Select diet option
                click_on(driver, diet)

                # Select accomplishment option
                click_on(driver, accomplish)

                # Click next to test if the combination navigates correctly
                click_on(driver, common_button.next_button)

                # Check if final page appeared (valid behavior)
                try:
                    match_element(driver, All_information.all_done, 3)
                    print(f"✅ Combination correct: {diet} + {accomplish} (Final page appeared)")
                except Exception:
                    print(f"❌ Combination failed: {diet} + {accomplish} (Final page did not appear)")
                    all_passed = False

                # Go back to Step 6 for next combination
                click_on(driver, common_button.back_navigation)

            except Exception as e:
                print(f"⚠️ Error with combination {diet} + {accomplish}: {e}")
                all_passed = False

    return all_passed



def check_one_time_step_6(driver):
    all_passed = True  # track overall result


    try:

        click_on(driver, Step_6.vegan)
    except Exception as e:
            print(f"⚠️ Failed to click on option ")


    try:
        click_on(driver, Step_6.option_4)
        click_on(driver, common_button.next_button)
    except Exception as e:
                print(f"⚠️ Failed to click on option")


    try:
        final_page = match_element(driver, All_information.all_done, 5)
        print("✅ Step 6 passed ")

    except Exception:
                # If Step 5 not found, test failed
                print(
                    f"❌ Test case failed for combination")


    try:
        click_on(driver,common_button.next_button)
        print("✅ Going for the Create An Account Page")

    except Exception:
                # If Step 5 not found, test failed
                print("Next button not found")






