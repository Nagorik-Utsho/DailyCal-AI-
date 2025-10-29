import pytest

from premium_features.exercise.check_update_exercise_page import check_intensity_update
from premium_features.exercise.go_to_target_page import go_to_update_run_page


@pytest.mark.run_feature
def test_run_feature(driver):
    go_to_update_run_page(driver)
    assert check_intensity_update(driver)