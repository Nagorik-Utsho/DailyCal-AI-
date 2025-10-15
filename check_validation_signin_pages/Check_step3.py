
from core.activities import *
from core.locators import *
from signin_pages.Step3 import validation_of_weight
import pytest

def select_gender(driver):
    click_on(driver,Step_3.gain_weight)



def step_3_checking(driver):
    select_gender(driver)
    validation_of_weight(driver)


