import time

from core.activities import click_on
from core.locators import *
from core.necessary_adb_commands import adb_tap_element_bottom


def go_to_update_goal_weight_page(driver):
        click_on(driver,Home_page.current_weight_section)
        click_on(driver,Current_weight.update_goal_weight_button)


def go_to_update_current_weight_page(driver):
    click_on(driver, Home_page.current_weight_section)
    time.sleep(5)
    adb_tap_element_bottom(
        driver,
        '//android.view.View[@content-desc="Current Weight 70 kg\nRemember to update this at least once a week so we can adjust your plan to hit your goal.\nUpdate your weight"]'
    )

def go_to_water_settings_page(driver):
    click_on(driver,Water.go_to_water_settings_page)

def go_to_todays_burn_page(driver) :
    click_on(driver,todays_burn.go_to_todays_burn)


def all_features_page(driver):

    #Go to all the features page
    click_on(driver,Home_page.all_features_button)


def  go_to_food_database_page(driver):
    all_features_page(driver)
    click_on(driver,Features.food_database)

def go_to_log_exercise(driver) :

    #Go to log exercise page

    all_features_page(driver)
    click_on(driver,Features.log_exercise)


def go_to_run(driver):
    print("Now in the GO to run file")
    go_to_log_exercise(driver)
    click_on(driver,log_exercise.run_exercise)

def go_to_update_run_page(driver) :
    click_on(driver,Home_page.today_burn_section)
    click_on(driver,todays_burn.update_weight_lifting)

def go_to_update_weightlifting_page(driver) :
    click_on(driver, Home_page.today_burn_section)
    click_on(driver, todays_burn.update_weight_lifting)

def go_to_manual_calories_update_page(driver) :
    click_on(driver, Home_page.today_burn_section)
    click_on(driver,todays_burn.manual_burn_list)
    click_on(driver,todays_burn.update_manual_calories)


def go_to_al_generated_list(driver) :
    click_on(driver,Home_page.today_burn_section)
    click_on(driver,todays_burn.ai_generated_burn_list)

def go_to_weight_lifting(driver):
    go_to_log_exercise(driver)
    click_on(driver,log_exercise.weight_lifting_exercise)

def go_to_manual(driver):
    go_to_log_exercise(driver)
    click_on(driver,log_exercise.manual_exercise)


def go_to_describe(driver):
    go_to_log_exercise(driver)
    click_on(driver,log_exercise.describe_exercise)




def go_to_saved_food(driver):
    # Go to log exercise page

    all_features_page(driver)
    click_on(driver, Features.saved_foods)


def go_to_scan_food(driver):
    # Go to log exercise page

    all_features_page(driver)
    click_on(driver, Features.scan_food)


def go_to_food_database(driver):
        # Go to log exercise page

        all_features_page(driver)
        click_on(driver, Features.food_database)

def go_to_nutrition_page(driver):
    all_features_page(driver)
    click_on(driver, Features.saved_foods)
    click_on(driver,Nutrition.food_in_food_database)






