from core.driver_setup import setup_driver
from premium_features.exercise.go_to_target_page import *
from premium_features.exercise.run import check_run_page
from premium_features.exercise.weight_lifting import check_weight_lifting_page


def check_log_exercise_feature(driver):
    # Run

    #check_run_page(driver)

    check_weight_lifting_page(driver)

