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
    exercise_activities_run=(By.XPATH,'////android.view.View[contains(@content-desc,"RUN")]')
    exercise_activities_weight_lifting=(By.XPATH,'////android.view.View[contains(@content-desc,"WEIGHT")]')
    exercise_activities_manual=(By.XPATH,'////android.view.View[contains(@content-desc,"MANUAL")]')
    exercise_activities_describe = (By.XPATH, '////android.view.View[contains(@content-desc,"DESCRIBE")]')

class Features:
    log_exercise=(By.XPATH,'//android.widget.ImageView[@content-desc="Log exercise"]')
    saved_foods=(By.XPATH,'//android.widget.ImageView[@content-desc="Saved foods"]')
    food_database=(By.XPATH,'//android.widget.ImageView[@content-desc="Food database"]')
    scan_food=(By.XPATH,'//android.widget.ImageView[@content-desc="Scan food"]')


class log_exercise:
    run_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Run")]')
    weight_lifting_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Weight")]')
    manual_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Manual")]')
    describe_exercise=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Describe")]')


class intensity_set_duration:
    high_intensity=(By.XPATH,'//android.widget.ImageView[contains(@content-desc,"High")]')
    medium_intensity = (By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Medium")]')
    low_intensity = (By.XPATH,'//android.widget.ImageView[contains(@content-desc,"Low")]')

    duration_15min=(By.XPATH,'//android.view.View[@content-desc="15 mins"]')
    duration_30min=(By.XPATH,'//android.view.View[@content-desc="30 mins"]')
    duration_60min=(By.XPATH,'//android.view.View[@content-desc="60 mins"]')
    duration_90min=(By.XPATH,'//android.view.View[@content-desc="90 mins"]')

    duration_text_field=(By.CLASS_NAME,'android.widget.EditText')

    add_button=(By.XPATH,'//android.widget.Button[@content-desc="Add"]')


class describe_exercise:
    describe_text_field = (By.CLASS_NAME,'android.widget.EditText')

    add_button=(By.XPATH,'//android.widget.Button[@content-desc="Add Exercise"]')






