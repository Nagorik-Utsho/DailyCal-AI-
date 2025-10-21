import pytest
from premium_features.exercise.run import check_run_page

@pytest.mark.run_feature
def test_run_feature(driver):
    assert check_run_page(driver), "Run feature validation failed"
