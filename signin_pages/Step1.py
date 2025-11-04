from core.activities import fill_input_field, click_on, match_element
from core.locators import *
from core.necessary_packages import *

def validation_of_birthdate(driver , day,month,year):

        # Fill fields using locators
        fill_input_field(driver, Step_1.input_filed, day,index=0)  # day
        fill_input_field(driver, Step_1.input_filed, month,index=1)  # month
        fill_input_field(driver, Step_1.input_filed, year,index=2)  # year
        #Click on the next button
        click_on(driver,Step_1.next_button)

        # Check if app navigated to step_2
        try:
            match_element(driver,Step_2.step_no,2)
            # User navigated → test failed
            print(f"❌ Test case FAILED for day : {day},month: {month},year: {year} (User moved to Step 2 )")

            # Recover to starting page

            try:
                    click_on(driver, Step_2.back_navigation)
            except Exception as nav_error:
                    print(f"⚠️ Failed to navigate back: {nav_error}")

            return True

        except Exception:
            return False




def go_to_step_2(driver,day,month,year):

    print("Going to step 2")
    # Fill fields using locators
    fill_input_field(driver, Step_1.input_filed, day, index=0)  # day
    fill_input_field(driver, Step_1.input_filed, month, index=1)  # month
    fill_input_field(driver, Step_1.input_filed, year, index=2)  # year
    # Click on the next button
    click_on(driver, Step_1.next_button)













