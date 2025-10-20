from core.driver_setup import setup_driver
from premium_features.exercise.go_to_target_page import *
from premium_features.exercise.run import check_run_page


def check_log_exercise_feature(driver):
    # Run
    go_to_run(driver)
    check_run_page(driver)

