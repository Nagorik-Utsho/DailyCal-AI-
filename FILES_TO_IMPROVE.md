# Files to Improve - Priority List

## 🔴 CRITICAL PRIORITY (Fix Immediately)

### 1. **Project Root - Create New Files**

#### `requirements.txt` (NEW FILE - CRITICAL)
- **Status:** ❌ Missing
- **Issue:** Cannot install dependencies
- **Action:** Create file with all Python packages
- **Dependencies to include:**
  - selenium
  - appium
  - pytest
  - colorama (if used)
  - Any other packages used

#### `README.md` (NEW FILE - CRITICAL)
- **Status:** ❌ Missing
- **Issue:** No documentation for project setup
- **Action:** Create comprehensive README
- **Should include:**
  - Project description
  - Setup instructions
  - How to run tests
  - Configuration requirements
  - Prerequisites (Appium server, Android SDK, etc.)

#### `config.py` or `.env` (NEW FILE - HIGH PRIORITY)
- **Status:** ❌ Missing
- **Issue:** Hardcoded app configuration
- **Action:** Create configuration file
- **Should contain:**
  - App package name
  - App activity
  - Appium server URL
  - Test data paths
  - Timeout values

---

### 2. **core_features_regression/scan_food.py**
- **Priority:** 🔴 CRITICAL
- **Lines to fix:** 1-7 (imports), 40, 60
- **Issues:**
  - ❌ Missing `import time` (used on line 40)
  - ❌ Missing `TimeoutException` import (used on line 60)
- **Action:** Add missing imports at top of file

---

### 3. **core/locators.py**
- **Priority:** 🔴 CRITICAL
- **Line to fix:** 157
- **Issue:**
  - ❌ Incomplete XPath: `update_current_weight_button=(By.XPATH,'//')`
- **Action:** Complete the locator or remove if unused

---

### 4. **core/driver_setup.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** 40-42
- **Issues:**
  - ❌ Hardcoded app package and activity
  - ❌ Hardcoded Appium server URL
- **Action:** Move to configuration file

---

## ⚠️ HIGH PRIORITY (Fix This Week)

### 5. **tests/test_signin_functionality.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** 9, 77, 136
- **Issues:**
  - ❌ Hardcoded absolute path: `r"C:\Users\USER\PythonProject\DailyCal_Automation\Test Data\..."`
  - ❌ Large blocks of commented code (lines 25-51, 88-114, 153-178)
  - ❌ Missing `import pytest` (if pytest decorators used)
- **Action:** 
  1. Replace hardcoded paths with relative paths using `os.path.join()`
  2. Remove commented code blocks
  3. Add missing imports

---

### 6. **tests/test_update_exercise_todays_burn.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** 9, 71, 98
- **Issues:**
  - ❌ Hardcoded absolute paths (3 occurrences)
- **Action:** Replace all hardcoded paths with relative paths

---

### 7. **tests/test_water_settings.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** Check for hardcoded paths
- **Issues:**
  - ❌ Hardcoded absolute path (if exists)
- **Action:** Replace with relative path

---

### 8. **tests/test_update_current_weight.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** 16
- **Issues:**
  - ❌ Hardcoded absolute path
- **Action:** Replace with relative path

---

### 9. **tests/test_update_nutrition_page.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** 14
- **Issues:**
  - ❌ Hardcoded absolute path
- **Action:** Replace with relative path

---

### 10. **tests/test_update_goal_weight.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** 11
- **Issues:**
  - ❌ Hardcoded absolute path
- **Action:** Replace with relative path

---

### 11. **premium_features/food_database/food_database.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** Check for hardcoded paths
- **Issues:**
  - ❌ Hardcoded absolute path (if exists)
- **Action:** Replace with relative path

---

### 12. **premium_features/scan_food/scan_food.py**
- **Priority:** ⚠️ HIGH
- **Lines to fix:** Check for hardcoded paths
- **Issues:**
  - ❌ Hardcoded absolute path (if exists)
- **Action:** Replace with relative path

---

## 📝 MEDIUM PRIORITY (Fix Next Sprint)

### 13. **core/locators.py** (Naming Conventions)
- **Priority:** 📝 MEDIUM
- **Lines to fix:** Throughout file
- **Issues:**
  - ⚠️ Inconsistent naming: `Step_1`, `Step_2` vs `OnBoarding`, `Create_An_Account`
  - ⚠️ Should be: `Step1`, `Step2` (PascalCase)
  - ⚠️ Class names with underscores inconsistent
- **Action:** Standardize all class names to PascalCase without underscores

---

### 14. **signin_pages/Step1.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** 5, 35
- **Issues:**
  - ⚠️ Function `validation_of_birthdate()` lacks docstring
  - ⚠️ Function `go_to_step_2()` lacks docstring
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 15. **signin_pages/Step2.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints to all functions

---

### 16. **signin_pages/Step3.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints to all functions

---

### 17. **signin_pages/Step4.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** All functions
- **Issues:**
  - ⚠️ All functions lack docstrings
  - ⚠️ Function `check_one_time_step_4()` doesn't return anything (line 127)
  - ⚠️ No type hints
- **Action:** 
  1. Add docstrings to all functions
  2. Fix `check_one_time_step_4()` to return value or remove
  3. Add type hints

---

### 18. **signin_pages/Step5.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 19. **signin_pages/Step6.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 20. **signin_pages/create_account_page.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 21. **core/activities.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** 7, 30, 59, 66, 103, 114
- **Issues:**
  - ⚠️ All functions lack type hints
  - ⚠️ Some functions lack comprehensive docstrings
  - ⚠️ Magic numbers (timeout=30, time.sleep values)
- **Action:** 
  1. Add type hints to all functions
  2. Enhance docstrings
  3. Extract magic numbers to constants

---

### 22. **core_features_regression/exercise.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** 31, 54, 80, 86, 111, 139, 155, 174
- **Issues:**
  - ⚠️ Functions lack docstrings
  - ⚠️ No type hints
  - ⚠️ Line 80 returns tuple but caller expects single value
  - ⚠️ Magic numbers (time.sleep values)
- **Action:** 
  1. Add docstrings and type hints
  2. Fix return type consistency
  3. Extract magic numbers

---

### 23. **core_features_regression/scan_food.py**
- **Priority:** 📝 MEDIUM (after fixing imports)
- **Lines to fix:** 8, 40
- **Issues:**
  - ⚠️ Function lacks comprehensive docstring
  - ⚠️ No type hints
  - ⚠️ Magic number: `time.sleep(10)`
- **Action:** 
  1. Add docstring and type hints
  2. Extract magic numbers

---

### 24. **core_features_regression/save_food.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 25. **features/home_page.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** 10, 24, 35
- **Issues:**
  - ⚠️ Functions lack docstrings
  - ⚠️ No type hints
  - ⚠️ `main()` function seems unused
- **Action:** 
  1. Add docstrings and type hints
  2. Remove or document `main()` function

---

### 26. **features/nutrition_page.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 27. **features/water_settings_page.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 28. **features/update_current_weight_page.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 29. **features/update_goal_weight_page.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 30. **premium_features/exercise/run.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** 25, 53, 82, 165
- **Issues:**
  - ⚠️ Functions lack docstrings
  - ⚠️ No type hints
  - ⚠️ Typo in line 119: `time` variable should be `minutes`
- **Action:** 
  1. Add docstrings and type hints
  2. Fix variable naming typo

---

### 31. **premium_features/exercise/weight_lifting.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 32. **premium_features/exercise/manual.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 33. **premium_features/exercise/describe.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 34. **premium_features/exercise/go_to_target_page.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 35. **premium_features/exercise/check_update_exercise_page.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 36. **premium_features/exercise/check_log_exercise.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 37. **premium_features/food_database/food_database.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
  - ⚠️ Hardcoded path (if exists)
- **Action:** 
  1. Add docstrings and type hints
  2. Fix hardcoded paths

---

### 38. **premium_features/scan_food/scan_food.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
  - ⚠️ Hardcoded path (if exists)
- **Action:** 
  1. Add docstrings and type hints
  2. Fix hardcoded paths

---

### 39. **tests/test_core_feature_fucntionality.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** 15
- **Issues:**
  - ⚠️ Typo in filename: `fucntionality` should be `functionality`
  - ⚠️ Function has good docstring but could add type hints
- **Action:** 
  1. Rename file to fix typo
  2. Add type hints

---

### 40. **tests/test_run.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 41. **tests/test_loss_weight_functinoality.py**
- **Priority:** 📝 MEDIUM
- **Lines to fix:** Filename
- **Issues:**
  - ⚠️ Typo in filename: `functinoality` should be `functionality`
- **Action:** Rename file to fix typo

---

### 42. **tests/test_weight_gain_functionality.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Functions likely lack docstrings
  - ⚠️ No type hints
- **Action:** Add docstrings and type hints

---

### 43. **tests/conftest.py**
- **Priority:** 📝 MEDIUM
- **Issues:**
  - ⚠️ Docstring exists but could be enhanced
  - ⚠️ No type hints
- **Action:** Add type hints

---

## 🔧 LOW PRIORITY (Technical Debt)

### 44. **All Files - Wildcard Imports**
- **Priority:** 🔧 LOW
- **Files Affected:** Multiple files using `from core.locators import *`
- **Issues:**
  - ⚠️ Wildcard imports make dependencies unclear
- **Action:** Replace with explicit imports

---

### 45. **All Files - Magic Numbers**
- **Priority:** 🔧 LOW
- **Files Affected:** Multiple files
- **Issues:**
  - ⚠️ Hardcoded time.sleep values, timeouts
- **Action:** Extract to constants file

---

### 46. **All Files - Code Formatting**
- **Priority:** 🔧 LOW
- **Files Affected:** All Python files
- **Issues:**
  - ⚠️ Inconsistent spacing
  - ⚠️ Multiple blank lines
- **Action:** Run `black` formatter and `flake8` linter

---

## 📋 Summary by Priority

### 🔴 CRITICAL (Do First - This Week)
1. Create `requirements.txt`
2. Create `README.md`
3. Create `config.py` or `.env`
4. Fix `core_features_regression/scan_food.py` (missing imports)
5. Fix `core/locators.py` (incomplete locator)
6. Fix `core/driver_setup.py` (hardcoded config)

### ⚠️ HIGH (Do This Week)
7. Fix all hardcoded paths in test files (9 files)
   - `tests/test_signin_functionality.py`
   - `tests/test_update_exercise_todays_burn.py`
   - `tests/test_water_settings.py`
   - `tests/test_update_current_weight.py`
   - `tests/test_update_nutrition_page.py`
   - `tests/test_update_goal_weight.py`
   - `premium_features/food_database/food_database.py`
   - `premium_features/scan_food/scan_food.py`

### 📝 MEDIUM (Do Next Sprint)
8. Add docstrings and type hints to all functions (30+ files)
9. Fix naming conventions in `core/locators.py`
10. Remove commented code blocks
11. Fix typos in filenames
12. Fix return type inconsistencies

### 🔧 LOW (Technical Debt)
13. Replace wildcard imports
14. Extract magic numbers to constants
15. Run code formatter (`black`) on all files
16. Run linter (`flake8`) and fix issues

---

## ✅ Quick Action Checklist

### Week 1 (Critical)
- [ ] Create `requirements.txt`
- [ ] Create `README.md`
- [ ] Create `config.py`
- [ ] Fix missing imports in `scan_food.py`
- [ ] Fix incomplete locator in `locators.py`
- [ ] Fix hardcoded paths (start with test files)

### Week 2 (High Priority)
- [ ] Complete all hardcoded path fixes
- [ ] Move app config to config file
- [ ] Remove commented code blocks
- [ ] Fix typos in filenames

### Week 3-4 (Medium Priority)
- [ ] Add docstrings to all functions
- [ ] Add type hints to all functions
- [ ] Fix naming conventions
- [ ] Fix return type inconsistencies

### Ongoing (Low Priority)
- [ ] Replace wildcard imports
- [ ] Extract magic numbers
- [ ] Format code with black
- [ ] Run linter and fix issues

---

**Total Files to Improve: 46+ files**

**Estimated Time:**
- Critical fixes: 1-2 days
- High priority fixes: 3-5 days
- Medium priority fixes: 1-2 weeks
- Low priority fixes: 1 week (ongoing)

