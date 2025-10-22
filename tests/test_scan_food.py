import pytest
from premium_features.scan_food.scan_food import check_scan_food

@pytest.mark.run_feature
def test_scan_food_functionality(driver):
    """
    Simple pytest test that runs the scan food feature.
    Assertions are inside check_scan_food function.
    """
    check_scan_food(driver)
