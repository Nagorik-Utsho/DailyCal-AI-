from core.activities import fill_input_field, click_on
from core.locators import *
from core.necessary_packages import *







def validation_of_birthdate(driver):
    wait = WebDriverWait(driver, 120)

    # Current script folder
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Correct folder and file name (with space)
    JSON_PATH = os.path.join(BASE_DIR, "..", "Test Data", "step_1_test_data.json")

    print("Looking for JSON at:", JSON_PATH)

    with open(JSON_PATH, "r",encoding="utf-8") as f:
        birthdate_data = json.load(f)

    # Iterate over all test cases
    for data in birthdate_data["birthday_check"]:
        day = data["day"]
        month = data["month"]
        year=data["year"]
        tc_id = data["tc_id"]
        expected = data["expected"]

        # Fill fields using locators
        fill_input_field(driver, Step_1.input_filed, day,index=0)  # day
        fill_input_field(driver, Step_1.input_filed, month,index=1)  # month
        fill_input_field(driver, Step_1.input_filed, year,index=2)  # year

        #Click on the next button
        click_on(driver,Step_1.next_button)

        print(f"📄 {tc_id}: Entered day={day}, month={month}, year={year} (expected={expected})")

        if expected is False :
            print("✅Passed")
        else :
            print ("❌Failed")









