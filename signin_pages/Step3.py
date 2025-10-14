from core.activities import fill_input_field, click_on
from core.locators import *
from core.necessary_packages import *

def validation_of_weight(driver):
    wait = WebDriverWait(driver, 120)

    # Current script folder
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Correct folder and file name (with space)
    JSON_PATH = os.path.join(BASE_DIR, "..", "Test Data", "step_3_test_data.json")

    print("Looking for JSON at:", JSON_PATH)

    with open(JSON_PATH, "r",encoding="utf-8") as f:
        Weight_data = json.load(f)

    # Iterate over all test cases
    for data in  Weight_data["weight_check"]:

        weight=data["weight"]
        tc_id = data["tc_id"]
        expected = data["expected"]

        # Fill fields using locators
        fill_input_field(driver, Step_2.input_filed, weight,index=0)  # Weight


        #Click on the next button
        click_on(driver,Step_2.next_button)

        print(f"📄 {tc_id}: Entered  weight={weight} (expected={expected})")

        if expected is False :
            print("✅Passed")
        else :
            print ("❌Failed")









