import time

from core.activities import click_on, match_element
from core.locators import Create_An_Account, Successfull_account, common_button


def social_login(driver):
    """
    Performs social login (Gmail) and verifies account creation.
    Uses soft assertions to continue execution while tracking failures.
    """
    failures = []  # Collect any issues


    # 2️⃣ Click on Social Log In
    try:
        print("Verifying the account creation through social login")
        click_on(driver, Create_An_Account.social_log_in)
        click_on(driver, Create_An_Account.click_on_gmail)
        time.sleep(3)
    except Exception as e:
        print(f"⚠️ Failed to select social login or Gmail: {e}")
        failures.append("Social login / Gmail click failed")

    # 3️⃣ Verify account creation message
    try:
        actual_title = match_element(driver, Successfull_account.congratulation_message)
        if actual_title.strip() == "Congratulation":
            print("✅ Account creation successful")
            print("User signin completed")
        else:
            print(f"❌ Account creation message unexpected: {actual_title}")
            failures.append("Account creation message mismatch")
    except Exception as e:
        print(f"⚠️ Failed to verify account creation message: {e}")
        failures.append("Account creation message check failed")

    # 4️⃣ Click Let's Get Started button
    try:
        print("Clicking on Let's get started to go to home page")
        click_on(driver, Successfull_account.start_button)
    except Exception as e:
        print(f"⚠️ Failed to click on start button: {e}")
        failures.append("Click start button failed")

    # 5️⃣ Soft assertion at the end
    if failures:
        print("\n⚠️ Social login encountered the following issues:")
        for failure in failures:
            print("-", failure)
        assert False, " | ".join(failures)
    else:
        print("\n✅ Social login flow completed successfully")














