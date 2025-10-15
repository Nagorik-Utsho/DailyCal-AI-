
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





def check_options_combinations(driver):
        all_passed = True  # track overall result

        for diet in specific_diet_options:
            try:
                print(f"🟢 Clicking on diet option: {diet}")
                click_on(driver, diet)
            except Exception as e:
                print(f"⚠️ Failed to click on option {diet}: {e}")
                all_passed = False
                continue  # move to next work_out

            for accomplish in accomplishment_options:
                try:
                    print(f"🟢 Clicking on accomplish option: {accomplish}")
                    click_on(driver, accomplish)
                    click_on(driver, common_button.next_button)
                except Exception as e:
                    print(f"⚠️ Failed to click on option {accomplish}: {e}")
                    all_passed = False
                    continue  # move to new option

                # Try to match Step 5 within 5 seconds
                try:
                    title_final= match_element(driver, All_information.all_done, 5)
                    print(f"✅ Test case passed for combination: {diet} + {accomplish} (Final Page appeared)")
                    click_on(driver, common_button.back_navigation)  # go back to try next combination
                except Exception:
                    # If Step 5 not found, test failed
                    print(
                        f"❌ Test case failed for combination: {diet} + {accomplish} (Final Page did not appear)")
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

    except Exception:
                # If Step 5 not found, test failed
                print(
                    f"❌ Test case failed for combination")




