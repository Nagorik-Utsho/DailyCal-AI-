import pytest
from core.driver_setup import setup_driver

@pytest.fixture(scope="session")
def driver():
    """
    Creates and tears down the Appium driver for the test session.
    """
    driver = setup_driver()
    yield driver
    driver.quit()
