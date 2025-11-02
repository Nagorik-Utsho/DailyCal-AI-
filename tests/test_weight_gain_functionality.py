import logging
import pytest
from core.activities import click_on
from core_features_regression.exercise import *
from core_features_regression.save_food import check_save_food_functionality
from core_features_regression.scan_food import scan_food_functionality_check
from core.locators import *

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


@pytest.mark.run_feature
def test_gain_weight_features(driver):
    """
    Regression test for core app features:
    1. read initial value from the progress bar
    2. Save food
    3. Run activity
    4. Weight lifting
    5. Manual calories
    6. Describe exercise
    7. Today's burn value update
    """

    failures = []  # Collect failures for soft assertion

    # Helper function to reduce repetition
    def verify_feature(feature_func, success_msg, fail_msg):
        try:
            result = feature_func(driver)
            if result:
                logger.info(f"✅ {success_msg}")
            else:
                logger.error(f"❌ {fail_msg}")
                failures.append(fail_msg)
            return result
        except Exception as e:
            logger.error(f"❌ {fail_msg} - Exception: {e}")
            failures.append(f"{fail_msg} - Exception: {e}")
            return False

    # 1️⃣ Scan food functionality
    result = verify_feature(scan_food_functionality_check,
                            "Scan food functionality tested",
                            "Food title not found in activity logs")

    # 2️⃣ Check saved food
    try:
        result_saved_food = check_save_food_functionality(driver)
        if "TEST - 1" in result_saved_food:
            logger.info("✅ Test passed: 'TEST - 1' is present in saved food")
        else:
            logger.error("❌ Test failed: 'TEST - 1' not found in saved food")
            failures.append("Saved food check failed")
    except Exception as e:
        logger.error(f"❌ Saved food check exception: {e}")
        failures.append(f"Saved food check exception: {e}")

    driver.back()
    # 3️⃣ Run activity — Preset
    verify_feature(check_run_preset_intensity_duration,
                   "Preset intensity & duration Tested (Run)",
                   "Preset intensity & duration failed (Run)")

    # 4️⃣ Run activity — Manual
    verify_feature(check_run_manual_duration_intensity,
                   "Manual duration with intensity Tested (Run)",
                   "Manual duration activity failed (Run)")

    # 5️⃣ Weight lifting — Preset
    verify_feature(check_weight_preset_intensity_duration,
                   "Preset intensity & duration Tested for Weight Lifting",
                   "Preset intensity & duration failed (Weight Lifting)")

    # 6️⃣ Weight lifting — Manual
    verify_feature(check_weight_manual_duration_intensity,
                   "Manual duration with intensity Tested (Weight Lifting)",
                   "Manual duration activity failed (Weight Lifting)")

    # 7️⃣ Manual calories input
    verify_feature(check_manual_calories,
                   "Manual calories functionality tested",
                   "Manual calories input activity failed")

    # 8️⃣ Describe exercise
    verify_feature(check_describe_exercise,
                   "Describe exercise functionality tested",
                   "Describe exercise activity failed")

    # 9️⃣ Today's burn update
    try:
        updated_value = check_amount_today_burn(driver)
        if updated_value == 300:
            logger.info("✅ Value updated at the home page successfully")
        else:
            logger.error(f"❌ Test failed: Today's burn value {updated_value} did not match expected 300")
            failures.append(f"Today's burn value check failed: {updated_value}")
    except Exception as e:
        logger.error(f"❌ Today's burn value check exception: {e}")
        failures.append(f"Today's burn value exception: {e}")

    # Final assertion for soft assertion failures
    assert not failures, "Some core features failed:\n" + "\n".join(failures)
