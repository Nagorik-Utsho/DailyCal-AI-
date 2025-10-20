from core.activities import click_on
from core.locators import *


def all_features_page(driver):

    #Go to all the features page
    click_on(driver,Home_page.all_features_button)


def go_to_log_exercise(driver) :

    #Go to log exercise page

    all_features_page(driver)
    click_on(driver,Features.log_exercise)


def go_to_run(driver):
    print("Now in the GO to run file")
    go_to_log_exercise(driver)
    click_on(driver,log_exercise.run_exercise)


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


