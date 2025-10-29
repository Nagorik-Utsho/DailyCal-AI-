from core.necessary_packages import *





class OnBoarding:
    next_button=(By.XPATH,'//android.view.View[@content-desc="Next"]')


class common_button:
    next_button = (By.XPATH, '//android.widget.Button[@content-desc="Next"]')
    back_navigation=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')



class Step_1:
    step_no=(By.XPATH,'//android.view.View[@content-desc="Step 1 of 6"]')
    female=(By.XPATH,'//android.widget.ImageView[@content-desc="female"]')
    male=(By.XPATH,'//android.widget.ImageView[@content-desc="male"]')
    Other=(By.XPATH,'//android.widget.ImageView[@content-desc="other"]')
    input_filed=(By.CLASS_NAME,'android.widget.EditText')
    next_button=(By.XPATH,'//android.widget.Button[@content-desc="Next"]')



class Step_2:
    step_no=(By.XPATH,'//android.view.View[@content-desc="Step 2 of 6"]')
    input_filed = (By.CLASS_NAME, 'android.widget.EditText')
    next_button = (By.XPATH, '//android.widget.Button[@content-desc="Next"]')
    back_navigation=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')



class Step_3:
    step_no=(By.XPATH,'//android.view.View[@content-desc="Step 3 of 6"]')
    lose_weight=(By.XPATH,'//android.view.View[@content-desc="Lose Weight"]')
    gain_weight=(By.XPATH,'//android.view.View[@content-desc="Gain Weight"]')
    maintain_weight=(By.XPATH,'//android.view.View[@content-desc="Maintain Weight"]')
    input_filed = (By.CLASS_NAME, 'android.widget.EditText')
    next_button=(By.XPATH,'//android.widget.Button[@content-desc="Next"]')
    back_navigation = (By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')

class Step_4:
    from selenium.webdriver.common.by import By

    sedentary = (By.XPATH, '//android.view.View[contains(@content-desc, "Sedentary")]/android.widget.RadioButton')
    light_active = (
    By.XPATH, '//android.view.View[contains(@content-desc, "Lightly Active")]/android.widget.RadioButton')
    moderately_active = (By.XPATH, '//android.view.View[contains(@content-desc, "Moderately Active")]/android.widget.RadioButton')
    very_active = (By.XPATH, '//android.view.View[contains(@content-desc, "Very Active")]/android.widget.RadioButton')
    super_active = (By.XPATH, '//android.view.View[contains(@content-desc, "Super Active")]/android.widget.RadioButton')

    #Progress Blocking
    lack_of_consistency=(By.XPATH,'//android.view.View[@content-desc="Lack of consistency"]')
    lack_of_support=(By.XPATH,'//android.view.View[@content-desc="Lack of support"]')
    busy_schedule=(By.XPATH,'//android.view.View[@content-desc="Busy schedule"]')
    lack_of_meal_inspiration=(By.XPATH,'//android.view.View[@content-desc="Lack of meal inspiration"]')
    unhealthy_eating_habits=(By.XPATH,'//android.view.View[@content-desc="Unhealthy eating habits"]')




class Step_5:
    step_no = (By.XPATH, '//android.view.View[@content-desc="Step 5 of 6"]')
    seekbar = (By.CLASS_NAME, 'android.widget.SeekBar')  # simple, find the first SeekBar




class Step_6:
    step_no = (By.XPATH, '//android.view.View[@content-desc="Step 6 of 6"]')

    #Specific Diet
    classic=(By.XPATH,'//android.view.View[@content-desc="Classic"]')
    pescatarian=(By.XPATH,'//android.view.View[@content-desc="Pescatarian"]')
    vegetarian=(By.XPATH,'//android.view.View[@content-desc="Vegetarian"]')
    vegan=(By.XPATH,'//android.view.View[@content-desc="Vegan"]')

    #Accomplish
    option_1=(By.XPATH,'//android.view.View[@content-desc="Eat and live healthier"]')
    option_2=(By.XPATH,'//android.view.View[@content-desc="Boost my energy and mood"]')
    option_3=(By.XPATH,'//android.view.View[@content-desc="Stay motivated & consistent"]')
    option_4=(By.XPATH,'//android.view.View[@content-desc="Feel better about my body"]')


class All_information:
    all_done=(By.XPATH,'//android.view.View[@content-desc="All Done"]')
    thank_you=(By.XPATH,'//android.view.View[@content-desc="Thank you for trusting us"]')
    back_navigation=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')

class Create_An_Account:
    social_log_in=(By.XPATH,'//android.widget.ImageView[@content-desc="Sign in with Google"]')
    continue_with_phone=(By.XPATH,'//android.widget.ImageView[@content-desc="continue with phone"]')
    click_on_gmail=(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.gms:id/account_display_name" and @text="Md. Samir Shahariar"]')

class Successfull_account:
   congratulation_message=(By.XPATH,'//android.view.View[@content-desc="Congratulation"]')
   start_button=(By.XPATH,'//android.widget.Button[@content-desc="Lets get started"]')

class Home_page:
    activity_logs_title=(By.XPATH,'//android.view.View[@content-desc="Activity logs"]')
    all_features_button=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
    date_check=(By.XPATH,'//android.view.View[@content-desc="Tue 21"]')
    daily_progress_section=(By.XPATH,'//android.view.View[contains(@content-desc,"DAILY PROGRESS")]')
    water_section=(By.XPATH,'//android.view.View[@content-desc="Water"]')
    current_weight_section=(By.XPATH,'//android.view.View[contains(@content-desc,"CURRENT WEIGHT")]')
    today_burn_section=(By.XPATH,'//android.view.View[contains(@content-desc,"BURNED")]')

class Water:
    water_section=(By.XPATH,'//android.view.View[@content-desc="Water"]')
    go_to_water_settings_page=(By.XPATH,'//android.widget.ScrollView/android.widget.ImageView[2]')
    water_increment=(By.XPATH,'//android.widget.ScrollView/android.widget.Button[2]')
    water_decrement=(By.XPATH,'//android.widget.ScrollView/android.widget.Button[1]')

    water_setting_page_title=(By.XPATH,'//android.view.View[contains(@content-desc,"Water settings")]')

    click_on_water_drop_down=(By.CLASS_NAME,'android.widget.Button')

    @staticmethod
    def read_water(ml):
        """
        Returns the XPATH for the indexed water element.

        :param ml: The text (e.g., '250 ml') to search for in content-desc
        :param index: The 1-based index of the element (default = 3)
        :return: Tuple (By.XPATH, xpath_string)
        """
        return (By.XPATH,f'(//android.view.View[contains(@content-desc,"{ml}")])')

    @staticmethod
    def serving_size_dropdown(ml):
        """
        Returns a dynamic locator for the water serving size dropdown.

        :param ml: The milliliter value (e.g., 250, 500)
        :return: Tuple (By.XPATH, xpath_string)
        """
        return (By.XPATH,f'//android.widget.Button[contains(@content-desc,"{ml}")]')


class Current_weight:
    current_weight_page_title=(By.XPATH,'//android.view.View[@content-desc="Your BMI"]')
    update_goal_weight_button=(By.XPATH,'//android.widget.Button[@content-desc="Update"]')
    update_current_weight_button=(By.XPATH,'//')


class Update_goal_weight:
    update_goal_weight_input_field=(By.CLASS_NAME,'android.widget.EditText')
    save_button=(By.XPATH,'//android.widget.Button[@content-desc="Save changes"]')

class Update_current_weight:
    update_current_weight_input_field = (By.CLASS_NAME,'android.widget.EditText')
    save_button = (By.XPATH,'//android.widget.Button[@content-desc="Save changes"]')

class Features:
    log_exercise=(By.XPATH,'//android.widget.ImageView[@content-desc="Log exercise"]')
    saved_foods=(By.XPATH,'//android.widget.ImageView[@content-desc="Saved foods"]')
    food_database=(By.XPATH,'//android.widget.ImageView[@content-desc="Food database"]')
    scan_food=(By.XPATH,'//android.widget.ImageView[@content-desc="Scan food"]')


class Food_database :
    food_database_page_title=(By.XPATH,'//android.view.View[@content-desc="Food database"]')
    food_data_input_field=(By.CLASS_NAME,'android.widget.EditText')
    food_data_generate_button=(By.XPATH,'//android.widget.ImageView[@content-desc="Generate Macros Using AI"]')

class log_exercise:
    run_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Run")]')
    weight_lifting_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Weight")]')
    manual_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Manual")]')
    describe_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Describe")]')


class intensity_set_duration:
    high_intensity=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"High")]')
    medium_intensity = (By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Medium")]')
    low_intensity = (By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Low")]')

    duration_15min = (By.XPATH, "//android.view.View[@content-desc='15 Mins']")
    duration_30min = (By.XPATH, "//android.view.View[@content-desc='30 Mins']")
    duration_60min = (By.XPATH, "//android.view.View[@content-desc='60 Mins']")
    duration_90min = (By.XPATH, "//android.view.View[@content-desc='90 Mins']")

    duration_text_field=(By.CLASS_NAME,'android.widget.EditText')

    add_button=(By.XPATH,'//android.widget.Button[@content-desc="Add"]')
    update_button=(By.XPATH,'//android.widget.Button[@content-desc="Update"]')


class describe_exercise:
    describe_text_field = (By.CLASS_NAME,'android.widget.EditText')

    add_button=(By.XPATH,'//android.widget.Button[@content-desc="Add Exercise"]')

class scan_food:
    camera_icon=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[2]')
    gallery_icon=(By.XPATH,'//android.widget.ImageView[@content-desc="Gallery"]')
    analysis_button=(By.XPATH,'//android.widget.Button[@content-desc="Analysis"]')
    retake_button=(By.XPATH,'//android.widget.Button[@content-desc="Retake"]')
    collections_xpath=(By.XPATH,'//android.widget.TextView[@text="Collections"]')
    favourites_xpath=(By.XPATH,'//android.widget.TextView[@text="Favourites"]')

    valid_food_image=(By.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]/android.view.View[2]/android.view.View')
    message_for_valid_food=(By.XPATH,'//android.widget.ImageView[@content-desc="Nutrition"]')

    invalid_food_image=(By.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View[4]/android.view.View[2]/android.view.View')
    message_for_invalid_food_image=(By.XPATH,'//android.view.View[@content-desc="No recognizable food detected in the image."]')

    back_navigation_invalid_food=(By.XPATH,'//android.widget.Button')
    blurry_food_image=(By.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.view.View')
    food_with_partial_object_image=(By.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.view.View[2]/android.view.View')




class Nutrition:
    message_for_valid_food = (By.XPATH, '//android.widget.ImageView[@content-desc="Nutrition"]')
    food_title = (By.CLASS_NAME, 'android.widget.EditText')
    increment_button=(By.XPATH,'//android.widget.ScrollView/android.view.View[4]')
    decrement_button=(By.XPATH,'//android.widget.ScrollView/android.view.View[2]')

    @staticmethod
    def read_value(value):
        read_value = (By.XPATH,f'//android.view.View[contains(@content-desc,"{value}")]')


    total_calories=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Calories")]')

    update_button=(By.XPATH,'//android.widget.Button[@content-desc="Update"]')

    done_button = (By.XPATH, '//android.widget.Button[@content-desc="Done"]')

    food_in_food_database=(By.XPATH,'//android.view.View[contains(@content-desc,"calories")]')

    read_calories=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"calories")]')

    edit_protein_page=(By.XPATH ,'//android.widget.ImageView[contains(@content-desc,"Protein")]')
    input_field_protein=(By.CLASS_NAME,'android.widget.EditText')
    protein_page_done_button=(By.XPATH,'//android.widget.Button[@content-desc="Done"]')

    edit_carbs_page=(By.XPATH , '//android.widget.ImageView[contains(@content-desc,"Carbs")]')
    input_field_carbs = (By.CLASS_NAME,'android.widget.EditText')
    carbs_page_done_button = (By.XPATH,'//android.widget.Button[@content-desc="Done"]')


    edit_fats_page=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Fats")]')
    input_field_fats=(By.CLASS_NAME,'android.widget.EditText')
    fat_page_done_button = (By.XPATH,'//android.widget.Button[@content-desc="Done"]')








class todays_burn:
    go_to_todays_burn = (By.XPATH, '//android.view.View[contains(@content-desc,"TODAY")]')

    back_navigation=(By.XPATH,'//android.widget.Button')

    todays_burn_page_title = (By.XPATH,'//android.view.View[contains(@content-desc,"Today")]')
    update_run = (By.XPATH, "//android.view.View[contains(@content-desc, 'Run')]")
    update_weight_lifting = (By.XPATH, '//android.view.View[contains(@content-desc,"Weight")]')
    exercise_burn_list=(By.XPATH,'//android.view.View[contains(@content-desc,"Exercise")')
    manual_burn_list=(By.XPATH,'//android.view.View[contains(@content-desc,"Manual")')
    al_generated_burn_list=(By.XPATH,'//android.view.View[contains(@content-desc,"AI")')
    empty_page=(By.XPATH,'//android.widget.ImageView[@content-desc="You haven’t logged any exercise today"]')

    check_for_regression_run_check=(By.XPATH,'//android.view.View[@content-desc="Run\n02:47 PM\n423 Calories\nIntensity: High\n15 Mins"]')

    @staticmethod
    def read_inforamtion(act):
       return (By.XPATH,f'//android.view.View[@content-desc,"{act}"]')






