import json
import time

from core.activities import fill_input_field, click_on
from core.locators import Food_database
from premium_features.exercise.go_to_target_page import go_to_food_database, go_to_food_database_page


json_file_path = r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\Food_Database\food_data_base_data.json"
with open(json_file_path, "r",) as f:
    food_data_set = json.load(f)["food_database_check"]




def validate_food_database(driver):

    for food_data in food_data_set :
        food=food_data["text"]
        expected=food_data["expected"]
        tc_id=food_data["tc_id"]

        fill_input_field(driver,Food_database.food_data_input_field,food)
        click_on(driver,Food_database.food_data_generate_button)
        time.sleep(1)



def check_food_database(driver):
    go_to_food_database_page(driver)