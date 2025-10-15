from core.activities import match_element, click_on
from core.locators import Step_5, common_button


def title_check(driver):
        """Exact match version"""
        try:
                title = match_element(driver, Step_5.step_no)
                expected = "step 5 of 6"  # Direct lowercase match

                print(f"🔍 Title: '{title}' vs Expected: '{expected}'")

                if title == expected:  # Exact match
                        print("✅ Exact match - Step 5 verified")
                        click_on(driver, common_button.next_button)
                        return True
                else:
                        print(f"❌ Exact match failed")
                        return False

        except Exception as e:
                print(f"⚠️ Title check failed: {e}")
                return False











