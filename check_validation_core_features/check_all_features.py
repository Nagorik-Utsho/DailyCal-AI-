from check_validation_core_features.check_log_exerciser import check_log_exercise_feature
from core.driver_setup import setup_driver
from features.update_current_weight_page import go_to_page
from features.update_goal_weight_page import *

from premium_features.scan_food.scan_food import check_scan_food


def main():
    driver=setup_driver()
    #check_log_exercise_feature(driver)
    #check_scan_food(driver)
    #check_update_goal_weight(driver)
    go_to_page(driver)



if __name__ == "__main__":
        main()