from re import match

from core.activities import click_on
from core.driver_setup import setup_driver
from core.locators import intensity_set_duration, common_button, Home_page, todays_burn
from premium_features.exercise.go_to_target_page import go_to_run


def check_run_log (driver) :
    #1. go to log exercise page
    print( "Working good ")

    #2. Select intensity
    click_on(driver,intensity_set_duration.high_intensity)

    #3. Select duration
    click_on(driver, intensity_set_duration.duration_30min)

    #4. Click on the add button
    click_on(driver,intensity_set_duration.add_button)

    #5. Go to the burned
    click_on(driver,Home_page.today_burn_section)

    #6.match element
    actual=match(driver,todays_burn.check_for_regression_run_check)

    if "15" in actual :
        print("Test case Passed")
    else:
        print("Test case failed")




















def main():
    driver=setup_driver()
    go_to_run(driver)
    check_run_log(driver)


if __name__ == "__main__":
        main()