from core.activities import fill_input_field, click_on, match_element
from core.locators import *
from core.necessary_packages import *

def validation_of_weight(driver,weight):

        # Fill fields using locators
        fill_input_field(driver, Step_3.input_filed, weight,index=0)  # Weight
        #Click on the next button
        click_on(driver,Step_3.next_button)

        # Check if app navigated to step_2
        try:
                match_element(driver, Step_4.step_no, 2)
                # User navigated → test failed
                print(f"❌ Test case FAILED for weight: {weight} (User moved to Step 4 )")

                # Recover to starting page

                        # Recover to starting page only if not the last valid case
                try:
                                click_on(driver, Step_4.back_navigation)
                except Exception as nav_error:
                                print(f"⚠️ Failed to navigate back: {nav_error}")
                return True

        except Exception:
                return False



def go_to_onetime_step4(driver,weight):
        print("Going to step 4 ")
        #select Gender
        click_on(driver,Step_3.gain_weight)
        # Fill fields using locators
        fill_input_field(driver, Step_3.input_filed, weight,index=0)  # Weight
        #Click on the next button
        click_on(driver,Step_3.next_button)














