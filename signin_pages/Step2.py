from core.activities import fill_input_field, click_on
from core.locators import *
from core.necessary_packages import *

def validation_of_height_weight(driver):
    wait = WebDriverWait(driver, 120)

    # Current script folder
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Correct folder and file name (with space)
    JSON_PATH = os.path.join(BASE_DIR, "..", "Test Data", "step_2_test_data.json")

    print("Looking for JSON at:", JSON_PATH)

    with open(JSON_PATH, "r",) as f:
        height_Weight_data = json.load(f)

    # Iterate over all test cases
    for data in  height_Weight_data["height_&_weight"]:
        feet = data["feet"]
        inch = data["inch"]
        weight=data["weight"]
        tc_id = data["tc_id"]
        expected = data["expected"]

        # Fill fields using locators
        fill_input_field(driver, Step_2.input_filed, feet,index=0)  # day
        fill_input_field(driver, Step_2.input_filed, inch,index=1)  # month
        fill_input_field(driver, Step_2.input_filed, weight,index=2)  # year

        #Click on the next button
        click_on(driver,Step_2.next_button)

        print(f"📄 {tc_id}: Entered feet={feet}, inch={inch}, weight={weight} (expected={expected})")

        if expected is False :
            print("✅Passed")
        else :
            print ("❌Failed")









