
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



def go_to_finalPage(driver):
    """
    Navigate through Step 6 options and reach the final page.
    Uses soft assertions to continue on failures but still reports them.
    """
    step_failures = []  # collect issues

    # 1️⃣ Select Vegan option
    try:
        click_on(driver, Step_6.vegan)
        print("✅ Clicked Vegan option")
    except Exception as e:
        print(f"⚠️ Failed to click on Vegan option: {e}")
        step_failures.append("Step 6: Vegan option click failed")

    # 2️⃣ Select another option and click Next
    try:
        click_on(driver, Step_6.option_4)
        click_on(driver, common_button.next_button)
        print("✅ Selected option 4 and clicked Next")
    except Exception as e:
        print(f"⚠️ Failed to click on option 4 or Next: {e}")
        step_failures.append("Step 6: Option 4 / Next click failed")

    # 3️⃣ Validate final page is displayed
    try:
        final_page = match_element(driver, All_information.all_done, 5)
        print("✅ Final page loaded successfully")
    except Exception as e:
        print(f"❌ Final page not found: {e}")
        step_failures.append("Step 6: Final page validation failed")

    # 4️⃣ Click Next to go to Create Account page
    try:
        click_on(driver, common_button.next_button)
        print("✅ Navigated to Create An Account page")
    except Exception as e:
        print(f"⚠️ Next button not found on final page: {e}")
        step_failures.append("Step 6: Next button click failed")

    # 5️⃣ Assert at the end (soft assertion)
    if step_failures:
        print("\n⚠️ Step 6 encountered the following issues:")
        for failure in step_failures:
            print("-", failure)
        # Fail the pytest test case, but after collecting all errors
        assert False, " | ".join(step_failures)
    else:
        print("\n✅ Step 6 completed successfully without errors")







