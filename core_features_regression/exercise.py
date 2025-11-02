import time
from datetime import datetime
from core.activities import click_on, match_element, fill_input_field
from core.driver_setup import setup_driver
from core.locators import *
from premium_features.exercise.go_to_target_page import go_to_run, go_to_weight_lifting, go_to_manual, go_to_describe

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






def check_run_preset_intensity_duration(driver) :


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

    current_time = datetime.now().strftime("%I:%M %p").upper()
    print(current_time)
    print(current_time)
    expected_values = [current_time, "RUN", "368"]
    return all(val in actual for val in expected_values)  # Returns True or False


def check_run_manual_duration_intensity(driver):

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

    current_time = datetime.now().strftime("%I:%M %p").upper()
    print(current_time)

    print(current_time)
    expected_values = ["RUN", "202"]
    return all(val in actual for val in expected_values)  # returns True/False





def check_weight_preset_intensity_duration(driver) :


    # Go to the target page
    go_to_weight_lifting(driver)

    #1.Select intensity
    click_on(driver,intensity_set_duration.medium_intensity)
    #2.Select duration
    click_on(driver,intensity_set_duration.duration_30min)
    #3.CLick on add button
    click_on(driver, intensity_set_duration.add_button)
    time.sleep(1)

    #4.check value from the activity list
    actual=match_element(driver,Home_page.testing_title_Weight_exercise).upper()
    print(actual)
    current_time = datetime.now().strftime("%I:%M %p").upper()
    print(current_time)
    expected_values = ["WEIGHT", "180"]
    return all(val in actual for val in expected_values)  # Returns True or False




def check_weight_manual_duration_intensity(driver):

    #Go to the target page
    go_to_weight_lifting(driver)

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
    actual=match_element(driver,Home_page.testing_title_Weight_exercise).upper()
    print(actual)

    current_time = datetime.now().strftime("%I:%M %p").upper()
    print(current_time)
    expected_values = ["WEIGHT", "175"]
    return all(val in actual for val in expected_values)  # returns True/False



def check_manual_calories(driver):
    #1.Add manual calories
    go_to_manual(driver)

    #2.input in the calories input field
    fill_input_field(driver,manual_calories.manual_calories_input_field,"300")

    #3. Click on the add button
    click_on(driver,manual_calories.manual_calories_add_button)

    actual=match_element(driver,manual_calories.testing_title_manual_calories).upper()
    print(actual)
    expected_values=["MANUAL","300"]
    return all(val in actual for val in expected_values)  # returns True/False


def check_describe_exercise(driver):
    #1.Add manual calories
    go_to_describe(driver)

    #2.input in the calories input field
    fill_input_field(driver,describe_exercise.describe_input_field,"20 min walk")

    #3. Click on the add button
    click_on(driver,describe_exercise.describe_exercise_add_button)

    time.sleep(2)

    actual=match_element(driver,describe_exercise.testing_title_describe_exercise).upper()
    print(actual)
    expected_values=["WALKING","80"]
    return all(val in actual for val in expected_values)  # returns True/False



def check_amount_today_burn(driver) :

    #1. read the value of the today's burn initially
    initial_value_today_burn=match_element(driver,Home_page.today_burn_section)
    ini_calories = initial_value_today_burn.split("\n")[1]
    print("Initial value of the Today's burn : ",ini_calories)
    #2. Log any exercise
    check_manual_calories(driver)
    # Split by newline and take the middle part


    #3. read the updated calories in the today's burn
    updated_value_today_burn=match_element(driver,Home_page.today_burn_section)
    updated_calories=updated_value_today_burn.split("\n")[1]
    print("Updated value of the today's burn: ",updated_calories)

    difference=(int(updated_calories)-int(ini_calories))

    print("Difference between calories is : ",difference)

    return  difference





def main():
    driver=setup_driver()
    #go_to_run(driver)
    #check_preset_intensity_duration(driver)
    #check_manual_duration_intensity(driver)
    check_amount_today_burn(driver)

if __name__ == "__main__":
    main()
