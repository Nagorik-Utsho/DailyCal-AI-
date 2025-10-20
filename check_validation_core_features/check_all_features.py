from check_validation_core_features.check_log_exerciser import check_log_exercise_feature
from core.driver_setup import setup_driver


def main():
    driver=setup_driver()
    check_log_exercise_feature(driver)


if __name__ == "__main__":
        main()