
from core_features_regression.exercise import *
from core.locators import *
from core_features_regression.scan_food import scan_food_functionality_check
from features.home_page import *
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    force=True  # override pytest logging capture
)
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)



@pytest.mark.run_feature
def test_loss_weight_features(driver):
    """
    Regression test for core app features:
    1. Read initial value from the progress bar
    2. Save food
    3. Run activity
    4. Weight lifting
    5. Manual calories
    6. Describe exercise
    7. Validate today's burn value update
    """

    failures = []  # Collect soft assertion errors

    try:
        # 1️⃣ Read initial calories before any activity
        initial_calories = read_information_from_daily_progressbar(driver)
        logger.info(f"📊 Initial calories: {initial_calories}")

        # 2️⃣ Add food calories (fixed or via scan_food_functionality_check)
        food_calories = 0
        status, food_calories = scan_food_functionality_check(driver)
        logger.info(f"🍽️  Food calories added: {food_calories}")

        # 3️⃣ Record calories burned — manual run
        check_run_manual_duration_intensity(driver)
        calories_burn_1 = read_calories_burn_from_activity_log_run(driver)
        logger.info(f"🏃 Manual run calories burned: {calories_burn_1}")

        # 4️⃣ Record calories burned — manual input
        status, calories_burn_2 = check_manual_calories(driver)
        logger.info(f"🔥 Manual calories burned entry: {calories_burn_2}")

        # 5️⃣ Read final calories after all actions
        final_calories = read_information_from_daily_progressbar(driver)
        logger.info(f"📈 Final calories on progress bar: {final_calories}")

        # 6️⃣ Calculate expected result
        expected_result = (
            int(initial_calories)
            + int(food_calories)
            - (int(calories_burn_1) + int(calories_burn_2))

        )
        logger.info(f"🧮 Expected calories: {expected_result}")

        # 7️⃣ Validate weight gain calculation
        if int(final_calories) == expected_result:
            logger.info("✅ Weight gain functionality PASSED")
        else:
            logger.error(
                f"❌ Weight gain functionality FAILED — "
                f"Expected {expected_result}, got {final_calories}"
            )
            failures.append("Weight gain functionality mismatch")

    except Exception as e:
        logger.error(f"❌ Exception during test execution: {e}")
        failures.append(f"Exception occurred: {e}")

    # 8️⃣ Soft assertion: fail at the end if any issues collected
    assert not failures, (
        "\n🧾 Some core features failed:\n" + "\n".join(f"• {f}" for f in failures)
    )
