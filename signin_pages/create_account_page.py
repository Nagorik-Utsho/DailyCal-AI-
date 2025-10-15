import time

from core.activities import click_on, match_element
from core.locators import Create_An_Account, Successfull_account


def social_login(driver):
    print("Verifying the account create through social Log in ")
    click_on(driver,Create_An_Account.social_log_in)
    click_on(driver,Create_An_Account.click_on_gmail)
    time.sleep(3)

    actual_title=match_element(driver,Successfull_account.congratulation_message)

    if actual_title == "Congratulation" :
        print("✅ Account creation successful" )
        print("User signin completed")
    else :
        print("Failed to create a new account using the social log in")

    print("Click on Let's get started to go home page ")
    click_on(driver,Successfull_account.start_button)


def create_account(driver):
    social_login(driver)
