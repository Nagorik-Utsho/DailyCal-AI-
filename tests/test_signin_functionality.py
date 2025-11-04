
from signin_pages.Step1 import validation_of_birthdate, go_to_step_2
from signin_pages.Step3 import validation_of_weight, go_to_step4
from signin_pages.Step4 import *
from signin_pages.Step5 import *
from signin_pages.Step6 import check_diet_options, check_accomplishment_options, check_options_combinations_step_6

# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Signin_pages\step_1_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    birthdate_data = json.load(f)
@pytest.mark.signin
def test_step1(driver):

    #1. Go to step 1 page
    print("Navigating to target page...")
    for i in range(3):
        click_on(driver, OnBoarding.next_button)

    #2.Select gender
    click_on(driver, Step_1.male)

    #3.Validate the birthdays

    # for data in birthdate_data["birthday_check"]:
    #     day = data["day"]
    #     month = data["month"]
    #     year = data["year"]
    #     tc_id = data["tc_id"]
    #     expected = data["expected"]
    #
    #
    #
    #     actual_result=validation_of_birthdate(driver,day,month, year)
    #
    #     print(f"📄 {tc_id}: Entered day={day}, month={month}, year={year} (expected={expected})")
    #
    #     if expected is False:
    #         print("✅Passed")
    #     else:
    #         print("❌Failed")# Compare actual vs expected
    #     if actual_result == expected:
    #         print(f"✅ TC {tc_id} PASSED | Input: {day}-{month}-{year} | Expected={expected} | Actual={actual_result}")
    #     else:
    #         print(f"❌ TC {tc_id} FAILED | Input: {day}-{month}-{year} | Expected={expected} | Actual={actual_result}")
    #
    #     # Assertion for pytest report
    #     assert actual_result == expected, (
    #         f"❌ TC {tc_id} FAILED: Input ({day}-{month}-{year}) | "
    #         f"Expected={expected}, but got {actual_result}"
    #     )


    for valid_value in birthdate_data["valid"]:
        day = valid_value["day"]
        month = valid_value["month"]
        year = valid_value["year"]
        tc_id = valid_value["tc_id"]
        expected = valid_value["expected"]

        go_to_step_2(driver,day,month,year)
        print("\n✅ Step 1 finished successfully. Moving to Step 2 validation...")
        validate_step2(driver)












# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Signin_pages\step_2_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    height_Weight_data = json.load(f)

def validate_step2(driver):

    print("Started executing Step 2 ")
    step_2=match_element(driver, Step_2.step_no)
    print("Now in step 2 : ",step_2)


    # for  data in height_Weight_data["height_&_weight"]:
    #     feet = data["feet"]
    #     inch = data["inch"]
    #     weight = data["weight"]
    #     tc_id = data["tc_id"]
    #     expected = data["expected"]
    #
    #
    #
    #     actual_result=validation_of_height_weight(driver,feet,inch,weight)
    #
    #     print(f"📄 {tc_id}: Entered feet={feet}, inch={inch}, weight={weight} (expected={expected})")
    #
    #     if expected is False:
    #         print("✅Passed")
    #     else:
    #         print("❌Failed")# Compare actual vs expected
    #     if actual_result == expected:
    #         print(f"✅ TC {tc_id} PASSED | Input: {feet}-{inch}-{weight} | Expected={expected} | Actual={actual_result}")
    #     else:
    #         print(f"❌ TC {tc_id} FAILED | Input: {feet}-{inch}-{weight} | Expected={expected} | Actual={actual_result}")
    #
    #     # Assertion for pytest report
    #     assert actual_result == expected, (
    #         f"❌ TC {tc_id} FAILED: Input ( {feet}-{inch}-{weight}) | "
    #         f"Expected={expected}, but got {actual_result}"
    #     )

    for data in height_Weight_data["valid"]:
        feet = data["feet"]
        inch = data["inch"]
        weight = data["weight"]
        tc_id = data["tc_id"]
        expected = data["expected"]

        go_to_step_2(driver,feet, inch,weight)
        print("\n✅ Step 2 finished successfully. Moving to Step 3 validation...")
        validate_step3(driver)









# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Signin_pages\step_3_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    Weight_data = json.load(f)


def validate_step3(driver):

    print("Started executing Step 3 ")
    step_3=match_element(driver, Step_3.step_no)
    print("Now in step 3 : ",step_3)


    #Select the goal weight
    click_on(driver,Step_3.gain_weight)

    #
    # # Iterate over all test cases
    # for data in Weight_data["weight_check"]:
    #
    #     weight = data["weight"]
    #     tc_id = data["tc_id"]
    #     expected = data["expected"]
    #
    #
    #
    #     actual_result=validation_of_weight(driver,weight)
    #
    #     print(f"📄 {tc_id}: Entered  weight={weight} (expected={expected})")
    #
    #     if expected is False:
    #         print("✅Passed")
    #     else:
    #         print("❌Failed")# Compare actual vs expected
    #     if actual_result == expected:
    #         print(f"✅ TC {tc_id} PASSED | Input:{weight} | Expected={expected} | Actual={actual_result}")
    #     else:
    #         print(f"❌ TC {tc_id} FAILED | Input: {weight} | Expected={expected} | Actual={actual_result}")
    #
    #     # Assertion for pytest report
    #     assert actual_result == expected, (
    #         f"❌ TC {tc_id} FAILED: Input ( {weight}) | "
    #         f"Expected={expected}, but got {actual_result}"
    #     )
    for data in Weight_data["valid"]:
            weight = data["weight"]
            tc_id = data["tc_id"]
            expected = data["expected"]
            go_to_step4(driver,weight)

            print("\n✅ Step 3 finished successfully. Moving to Step 4 validation...")
            validate_step4(driver)


# Global list to collect soft assertion failures
step_failures = []

def validate_step4(driver):
    print("Start Executing Step 4")

    try:
        result_workout = check_workOut(driver)
        if not result_workout:
            step_failures.append("Step 4: Workout options test failed")
    except Exception as e:
        step_failures.append(f"Step 4: Workout options exception: {e}")

    # try:
    #     result_blocking = check_blocking_progress(driver)
    #     if not result_blocking:
    #         step_failures.append("Step 4: Blocking progress options test failed")
    # except Exception as e:
    #     step_failures.append(f"Step 4: Blocking progress exception: {e}")

    try:
        result_combination = check_options_combinations(driver)
        if not result_combination:
            step_failures.append("Step 4: Combinations test failed")
    except Exception as e:
        step_failures.append(f"Step 4: Combinations exception: {e}")

    print("Step 4 validations finished")
    time.sleep(3)

    print("\n✅ Step 4 finished. Moving to Step 5 validation...")
    time.sleep(2)

    try:
        check_one_time_step_4(driver)
    except Exception as e:
        step_failures.append(f"Step 4: One-time check exception: {e}")

    validate_step5(driver)


def validate_step5(driver):
    print("Start Executing Step 5")
    try:
        title_check(driver)
    except Exception as e:
        step_failures.append(f"Step 5: Title check exception: {e}")

    time.sleep(2)
    print("\n✅ Step 5 finished. Moving to Step 6 validation...")
    validation_step6(driver)


def validation_step6(driver):
    print("Start Executing Step 6")

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
