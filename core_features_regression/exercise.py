import time
from datetime import datetime
from core.activities import click_on, match_element, fill_input_field
from core.driver_setup import setup_driver
from core.locators import *
from premium_features.exercise.go_to_target_page import go_to_run

"'""Global Intensity && Duration XPATH declaration"""


intensity_set=[
    intensity_set_duration.low_intensity,
    intensity_set_duration.medium_intensity,
    intensity_set_duration.high_intensity
]

duration_set = [

    intensity_set_duration.duration_15min,
    intensity_set_duration.duration_30min,
    intensity_set_duration.duration_60min,
    intensity_set_duration.duration_90min

]

current_time = datetime.now().strftime("%I:%M %p").upper()

print(current_time)


def check_preset_intensity_duration(driver) :


    # Go to the target page
    go_to_run(driver)

    #1.Select intensity
    click_on(driver,intensity_set_duration.medium_intensity)
    #2.Select duration
    click_on(driver,intensity_set_duration.duration_30min)
    #3.CLick on add button
    click_on(driver, intensity_set_duration.add_button)
    time.sleep(1)

    #4.check value from the activity list
    actual=match_element(driver,Home_page.testing_title_run_exercise).upper()
    print(actual)

    expected_values = [current_time, "RUN", "368"]
    return all(val in actual for val in expected_values)  # Returns True or False


def check_manual_duration_intensity(driver):

    #Go to the target page
    go_to_run(driver)

    # 1.Select intensity
    click_on(driver, intensity_set_duration.low_intensity)

    #2.Input manual duration
    fill_input_field(driver, intensity_set_duration.duration_text_field, "50")
    time.sleep(.3)
    driver.hide_keyboard()
    # 3.CLick on add button
    click_on(driver, intensity_set_duration.add_button)
    time.sleep(1)


    #4.check value from the activity list
    actual=match_element(driver,Home_page.testing_title_run_exercise).upper()
    print(actual)


    expected_values = [current_time, "RUN", "202"]
    return all(val in actual for val in expected_values)  # returns True/False


def main():
    driver=setup_driver()
    go_to_run(driver)
    #check_preset_intensity_duration(driver)
    check_manual_duration_intensity(driver)


if __name__ == "__main__":
    main()
