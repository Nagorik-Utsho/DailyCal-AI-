import json
import os

from core.activities import *
from core.locators import *
from core.driver_setup import *
from signin_pages.Step1 import validation_of_birthdate
from signin_pages.Step2 import validation_of_height_weight


def step_2_checking(driver):
    validation_of_height_weight(driver)

