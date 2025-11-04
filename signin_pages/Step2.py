from core.activities import fill_input_field, click_on, match_element
from core.locators import *
from core.necessary_packages import *

def validation_of_height_weight(driver,feet,inch,weight):


        # Fill fields using locators
        fill_input_field(driver, Step_2.input_filed, feet,index=0)  # day
        fill_input_field(driver, Step_2.input_filed, inch,index=1)  # month
        fill_input_field(driver, Step_2.input_filed, weight,index=2)  # year





        # Check if app navigated to step_2
        try:
            match_element(driver, Step_3.step_no, 2)
            # User navigated → test failed
            print(f"❌ Test case FAILED for feet : {feet},inch: {inch},weight: {weight} (User moved to Step 2 )")

            # Recover to starting page

                # Recover to starting page only if not the last valid case
            try:
                click_on(driver, Step_3.back_navigation)
            except Exception as nav_error:
                    print(f"⚠️ Failed to navigate back: {nav_error}")
            return True

        except Exception:
            return False



def go_to_step_3(driver, feet, inch, weight):

    print("Go to step 3")
    # Fill fields using locators
    fill_input_field(driver, Step_2.input_filed, feet, index=0)  # day
    fill_input_field(driver, Step_2.input_filed, inch, index=1)  # month
    fill_input_field(driver, Step_2.input_filed, weight, index=2)  # year

    # Click on the next button
    click_on(driver, Step_2.next_button)



