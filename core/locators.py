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

    sedentary=(By.XPATH,' //android.view.View[@content-desc="Sedentary Little to no exercise"]')
    light_active=(By.XPATH,'//android.view.View[@content-desc="Lightly Active Light exercise/sports 1–3 days/week"]')
    moderately_active=(By.XPATH,'//android.view.View[@content-desc="Moderately Active Moderate exercise 3–5 days/week"]')
    very_active=(By.XPATH,'//android.view.View[@content-desc="Very Active Hard exercise 6–7 days/week"]')
    super_active=(By.XPATH,'//android.view.View[@content-desc="Super Active Very hard exercise/sports & physical job or training twice a day"]')

     #Progress Blocking
    lack_of_consistency=(By.XPATH,'//android.view.View[@content-desc="Lack of consistency"]')
    lack_of_support=(By.XPATH,'//android.view.View[@content-desc="Lack of support"]')
    busy_schedule=(By.XPATH,'//android.view.View[@content-desc="Busy schedule"]')
    lack_of_meal_inspiration=(By.XPATH,'//android.view.View[@content-desc="Lack of meal inspiration"]')
    unhealthy_eating_habits=(By.XPATH,'//android.view.View[@content-desc="Unhealthy eating habits"]')


class Step_5:
    step_no=(By.XPATH,'//android.view.View[@content-desc="Step 5 of 6"]')
    weight_bar=(By.XPATH,'//android.widget.SeekBar[@content-desc="42%"]')


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


