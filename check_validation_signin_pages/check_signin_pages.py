from check_validation_signin_pages.check_account_creation import check_create_account
from check_validation_signin_pages.check_step3 import step_3_checking
from check_validation_signin_pages.check_step4 import step_4_checking
from check_validation_signin_pages.check_step6 import step_6_checking
from check_validation_signin_pages.check_step1 import step_1_checking
from check_validation_signin_pages.check_step2 import step_2_checking
from check_validation_signin_pages.check_step5 import step_5_checking
from core.driver_setup import setup_driver


def main():
    driver=setup_driver()
    step_1_checking(driver)
    step_2_checking(driver)
    step_3_checking(driver)
    step_4_checking(driver)
    step_5_checking(driver)
    step_6_checking(driver)
    check_create_account(driver)



if __name__ == "__main__":
        main()