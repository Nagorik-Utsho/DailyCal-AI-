import time

from core.activities import click_on, match_element
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




# def check_water_settings_page (driver):
#     go_to_water_settings_page(driver)