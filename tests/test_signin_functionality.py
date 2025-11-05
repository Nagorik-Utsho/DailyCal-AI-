import time

from signin_pages.Step1 import validation_of_birthdate, go_to_step_2
from signin_pages.Step2 import validation_of_height_weight, go_to_step_3
from signin_pages.Step3 import *
from signin_pages.Step4 import *
from signin_pages.Step5 import *
from signin_pages.Step6 import *
from signin_pages.create_account_page import social_login


def go_to_step1(driver):
    # 1. Go to step 1 page
    print("Navigating to target page...")
    for i in range(3):
        click_on(driver, OnBoarding.next_button)

    # 2.Select gender
    click_on(driver, Step_1.male)




# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Signin_pages\step_1_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    birthdate_data = json.load(f)
@pytest.mark.signin
def test_step1(driver):

    go_to_step1(driver)



    #3.Validate the birthdays

    for data in birthdate_data["birthday_check"]:
        day = data["day"]
        month = data["month"]
        year = data["year"]
        tc_id = data["tc_id"]
        expected = data["expected"]



        actual_result=validation_of_birthdate(driver,day,month, year)

        print(f"📄 {tc_id}: Entered day={day}, month={month}, year={year} (expected={expected})")

        if expected is False:
            print("✅Passed")
        else:
            print("❌Failed")# Compare actual vs expected
        if actual_result == expected:
            print(f"✅ TC {tc_id} PASSED | Input: {day}-{month}-{year} | Expected={expected} | Actual={actual_result}")
        else:
            print(f"❌ TC {tc_id} FAILED | Input: {day}-{month}-{year} | Expected={expected} | Actual={actual_result}")

        # Assertion for pytest report
        assert actual_result == expected, (
            f"❌ TC {tc_id} FAILED: Input ({day}-{month}-{year}) | "
            f"Expected={expected}, but got {actual_result}"
        )

def go_to_step2(driver):
    '''Here step 1 is commented ,
     because while we uncomment this code section the app state does not reset and it holds on the valid value'''
    # go_to_step1(driver)


    for data in birthdate_data["valid"]:
        day = data["day"]
        month = data["month"]
        year = data["year"]
        tc_id = data["tc_id"]
        expected = data["expected"]

        go_to_step_2(driver,day,month, year)









# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Signin_pages\step_2_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    height_Weight_data = json.load(f)

def test_validate_step2(driver):

    go_to_step2(driver)
    time.sleep(3)

    print("Started executing Step 2 ")


    for  data in height_Weight_data["height_&_weight"]:
        feet = data["feet"]
        inch = data["inch"]
        weight = data["weight"]
        tc_id = data["tc_id"]
        expected = data["expected"]



        actual_result=validation_of_height_weight(driver,feet,inch,weight)

        print(f"📄 {tc_id}: Entered feet={feet}, inch={inch}, weight={weight} (expected={expected})")

        if expected is False:
            print("✅Passed")
        else:
            print("❌Failed")# Compare actual vs expected
        if actual_result == expected:
            print(f"✅ TC {tc_id} PASSED | Input: {feet}-{inch}-{weight} | Expected={expected} | Actual={actual_result}")
        else:
            print(f"❌ TC {tc_id} FAILED | Input: {feet}-{inch}-{weight} | Expected={expected} | Actual={actual_result}")

        # Assertion for pytest report
        assert actual_result == expected, (
            f"❌ TC {tc_id} FAILED: Input ( {feet}-{inch}-{weight}) | "
            f"Expected={expected}, but got {actual_result}"
        )






def go_to_step3(driver):
    #go_to_step2(driver)

    for  data in height_Weight_data["valid"]:
        feet = data["feet"]
        inch = data["inch"]
        weight = data["weight"]
        tc_id = data["tc_id"]
        expected = data["expected"]

        go_to_step_3(driver, feet, inch, weight)








# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Signin_pages\step_3_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    Weight_data = json.load(f)


def test_validate_step3(driver):

    #2. Cross step 1 and Step 2
    go_to_step3(driver)


    print("Started executing Step 3 ")
    step_3=match_element(driver, Step_3.step_no)
    print("Now in step 3 : ",step_3)


    #Select the goal weight
    click_on(driver,Step_3.gain_weight)


    # Iterate over all test cases
    for data in Weight_data["weight_check"]:

        weight = data["weight"]
        tc_id = data["tc_id"]
        expected = data["expected"]



        actual_result=validation_of_weight(driver,weight)

        print(f"📄 {tc_id}: Entered  weight={weight} (expected={expected})")

        if expected is False:
            print("✅Passed")
        else:
            print("❌Failed")# Compare actual vs expected
        if actual_result == expected:
            print(f"✅ TC {tc_id} PASSED | Input:{weight} | Expected={expected} | Actual={actual_result}")
        else:
            print(f"❌ TC {tc_id} FAILED | Input: {weight} | Expected={expected} | Actual={actual_result}")

        # Assertion for pytest report
        assert actual_result == expected, (
            f"❌ TC {tc_id} FAILED: Input ( {weight}) | "
            f"Expected={expected}, but got {actual_result}"
        )









def go_to_step4(driver):
    #go_to_step3(driver)

    # Iterate over all test cases
    for data in Weight_data["valid"]:
        weight = data["weight"]
        tc_id = data["tc_id"]
        expected = data["expected"]
        print("\n✅ Step 3 finished successfully. Moving to Step 4 validation...")
        go_to_onetime_step4(driver, weight)




# Global list to collect soft assertion failures
step_failures = []

def test_validate_step4(driver):

    go_to_step4(driver)

    print("Start Executing Step 4")

    try:
        result_workout = check_workOut(driver)
        if not result_workout:
            step_failures.append("Step 4: Workout options test failed")
    except Exception as e:
        step_failures.append(f"Step 4: Workout options exception: {e}")

    try:
        result_blocking = check_blocking_progress(driver)
        if not result_blocking:
            step_failures.append("Step 4: Blocking progress options test failed")
    except Exception as e:
        step_failures.append(f"Step 4: Blocking progress exception: {e}")

    try:
        result_combination = check_options_combinations(driver)
        if not result_combination:
            step_failures.append("Step 4: Combinations test failed")
    except Exception as e:
        step_failures.append(f"Step 4: Combinations exception: {e}")

    print("Step 4 validations finished")
    time.sleep(3)






def go_to_step5(driver) :
   # go_to_step4(driver)
    print("\n✅ Step 4 finished. Moving to Step 5 validation...")
    time.sleep(2)

    try:
        go_to_onetime_step5(driver)
    except Exception as e:
        step_failures.append(f"Step 4: One-time check exception: {e}")




def test_validate_step5(driver):

    go_to_step5(driver)
    print("Start Executing Step 5")
    try:
        title_check(driver)
    except Exception as e:
        step_failures.append(f"Step 5: Title check exception: {e}")

    time.sleep(2)
    print("\n✅ Step 5 finished. Moving to Step 6 validation...")




def go_to_step6(driver):
    #go_to_step5(driver)
    click_on(driver, common_button.next_button)



def test_validation_step6(driver):
    print("Start Executing Step 6")
    go_to_step6(driver)

    try:
        result_diet = check_diet_options(driver)
        if not result_diet:
            step_failures.append("Step 6: Diet options test failed")
    except Exception as e:
        step_failures.append(f"Step 6: Diet options exception: {e}")

    try:
        result_accomplish = check_accomplishment_options(driver)
        if not result_accomplish:
            step_failures.append("Step 6: Accomplishment options test failed")
    except Exception as e:
        step_failures.append(f"Step 6: Accomplishment options exception: {e}")

    try:
        result_combination = check_options_combinations_step_6(driver)
        if not result_combination:
            step_failures.append("Step 6: Combination test failed")
    except Exception as e:
        step_failures.append(f"Step 6: Combination exception: {e}")

    print("Step 6 validations finished")

    # Final summary of all soft assertion failures
    if step_failures:
        print("\n⚠️ The following tests failed during execution:")
        for failure in step_failures:
            print("-", failure)
    else:
        print("\n✅ All steps passed successfully!")


def test_user_signin(driver):

   go_to_step1(driver)
   go_to_step2(driver)
   go_to_step3(driver)
   go_to_step4(driver)
   go_to_step5(driver)
   go_to_step6(driver)
   step_failures = []

   # 1️⃣ Step 6 final page
   try:
       go_to_finalPage(driver)
   except AssertionError as e:
       # Collect assertion failures without stopping the test
       step_failures.append(f"Final page validation failed: {e}")

   # 2️⃣ Social login
   try:
       social_login(driver)
   except AssertionError as e:
       step_failures.append(f"Social login validation failed: {e}")

   # 3️⃣ Final pytest assertion to report all failures
   if step_failures:
       print("\n⚠️ Some issues occurred during signup flow:")
       for failure in step_failures:
           print("-", failure)
       assert False, " | ".join(step_failures)
   else:
       print("\n✅ User signup flow completed successfully!")





   print("Reached at the final page")
