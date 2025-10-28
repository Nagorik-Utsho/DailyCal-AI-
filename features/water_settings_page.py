import time

from core.activities import click_on, match_element
from core.driver_setup import setup_driver
from core.locators import Water
from premium_features.exercise.go_to_target_page import go_to_water_settings_page

def validate_increment(driver,ml) :

    click_on(driver,Water)



def validate_water_settings(driver, ml):


    click_on(driver,Water.serving_size_dropdown(ml))
    time.sleep(.5)
    #Click on the Increment Button
    click_on(driver,Water.water_increment)
    actual=match_element(driver,Water.read_water(ml))
    print(actual)
    time.sleep(.5)
    #click on decrement
    try:
        click_on(driver, Water.water_decrement,ml)
    except Exception as e :
        print("decrement button not found")
    return actual


def water_increment_check(driver, *ml_values):
    print("Verify the water increment is functional")

    # Compute expected total
    total_ml = str(sum(int(ml) for ml in ml_values))
    print(f"Expected total: {total_ml}")

    for ml in ml_values:
        # Step 1: Go to water settings page
        go_to_water_settings_page(driver)
        print(f"Sending water value: {ml}")

        # Step 2: Send value
        click_on(driver, Water.click_on_water_drop_down)
        click_on(driver, Water.serving_size_dropdown(ml))
        click_on(driver, Water.water_increment)
        time.sleep(1)  # optional: reduce if needed

    # Step 3: Read total value
    total_increment = match_element(driver, Water.read_water(total_ml))
    total_increment = total_increment.replace(" ml", "").strip()
    print(f"Actual total: {total_increment}")

    return total_increment




def water_decrement_check(driver, ml_01, ml_02, ml_03):
    print("Verify the water decrement is functional")
    ml_values=[ml_01,ml_02]
    dm_water = ml_03
    total_incre=str(int(ml_values[0]) + int(ml_values[1]))
    # Compute expected total
    total_ml = str(int(ml_values[0]) + int(ml_values[1]) - int(dm_water))
    print(f"Expected total in the Decrement function : {total_ml}")

    for  ml in ml_values:
        # Step 1: Go to water settings page
        go_to_water_settings_page(driver)
        print(f"Sending water value: {ml}")

        # Step 2: Send value
        click_on(driver, Water.click_on_water_drop_down)
        click_on(driver, Water.serving_size_dropdown(ml))
        click_on(driver, Water.water_increment)
        time.sleep(1)  # optional: reduce if needed


    total_increment = match_element(driver, Water.read_water(total_incre))
    print(f"Amount of total water incremented : ",total_increment)


    #now decrement
    go_to_water_settings_page(driver)
    click_on(driver, Water.click_on_water_drop_down)
    click_on(driver, Water.serving_size_dropdown(dm_water))
    click_on(driver, Water.water_decrement)

    # Step 4: Read total value
    total_decrement = match_element(driver, Water.read_water(total_ml))
    total_decrement = total_decrement.replace(" ml", "").strip()
    print(f" After decrement : {total_decrement}")

    return total_decrement







# def check_water_settings_page (driver):
#     #go_to_water_settings_page(driver)
#     water_decrement_check(driver)
#
#
# def main():
#     driver=setup_driver()
#     check_water_settings_page(driver)
#
#
# if __name__ == "__main__":
#         main()
