# Professional Documentation & Standard Coding Guide

**For:** DailyCal Automation Framework  
**Purpose:** Show professional documentation standards and coding best practices

---

## 📚 TABLE OF CONTENTS

1. [Professional README.md](#1-professional-readmemd)
2. [Professional Docstrings](#2-professional-docstrings)
3. [Standard Coding Examples](#3-standard-coding-examples)
4. [Configuration Files](#4-configuration-files)
5. [Requirements.txt](#5-requirementstxt)
6. [Code Formatting Standards](#6-code-formatting-standards)

---

## 1. PROFESSIONAL README.md

### **Example: Professional README.md**

```markdown
# DailyCal Mobile App Automation Framework

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Appium](https://img.shields.io/badge/Appium-2.0-green.svg)](http://appium.io/)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-orange.svg)](https://pytest.org/)

A comprehensive mobile automation framework for testing the DailyCal Android application using Appium, Selenium, and Pytest.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Test Coverage](#test-coverage)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This automation framework provides comprehensive test coverage for the DailyCal mobile application, including:
- Complete sign-in flow (6 steps)
- Exercise logging (Run, Weight Lifting, Manual, AI-powered)
- Food management (Scan, Save, Database)
- Nutrition tracking
- Water intake management
- Weight management
- Today's burn calculations

**Total Test Coverage:** ~155-220 test cases

## ✨ Features

- ✅ Page Object Model (POM) design pattern
- ✅ Data-driven testing with JSON test data
- ✅ Cross-platform compatibility (Windows, Linux, macOS)
- ✅ Comprehensive error handling and retry mechanisms
- ✅ Detailed test reporting
- ✅ Modular and maintainable code structure

## 📦 Prerequisites

Before running the tests, ensure you have the following installed:

### Required Software

1. **Python 3.9 or higher**
   ```bash
   python --version
   ```

2. **Appium Server**
   ```bash
   npm install -g appium
   appium --version
   ```

3. **Android SDK**
   - Android Studio or standalone SDK
   - ADB (Android Debug Bridge)
   - Set ANDROID_HOME environment variable

4. **Java JDK 8 or higher**
   ```bash
   java -version
   ```

5. **Node.js and npm** (for Appium)
   ```bash
   node --version
   npm --version
   ```

### Required Hardware

- Android device (physical or emulator)
- USB cable (for physical device)
- Stable internet connection

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/DailyCal_Automation.git
cd DailyCal_Automation
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Appium Drivers

```bash
appium driver install uiautomator2
```

### Step 5: Start Appium Server

```bash
# In a separate terminal
appium
```

## ⚙️ Configuration

### Environment Setup

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file with your configuration:
   ```env
   # Appium Configuration
   APPIUM_SERVER_URL=http://127.0.0.1:4723/wd/hub
   
   # App Configuration
   APP_PACKAGE=com.dailycalai.app
   APP_ACTIVITY=com.dailycalai.app.MainActivity
   APK_PATH=path/to/your/app.apk
   
   # Device Configuration
   DEVICE_UDID=  # Leave empty for auto-detection
   USE_EMULATOR=false
   
   # Timeouts
   DEFAULT_TIMEOUT=30
   ```

### Device Setup

#### Physical Device:
1. Enable Developer Options on your Android device
2. Enable USB Debugging
3. Connect device via USB
4. Verify connection:
   ```bash
   adb devices
   ```

#### Emulator:
1. Start Android emulator from Android Studio
2. Verify connection:
   ```bash
   adb devices
   ```

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests by Marker

```bash
# Run sign-in tests only
pytest -m signin

# Run core feature tests
pytest -m run_feature

# Run regression tests
pytest -m regression
```

### Run Specific Test File

```bash
pytest tests/test_signin_functionality.py
```

### Run with HTML Report

```bash
pytest --html=reports/test_report.html --self-contained-html
```

### Run with Verbose Output

```bash
pytest -v
```

### Run Specific Test Case

```bash
pytest tests/test_signin_functionality.py::test_step1 -v
```

## 📁 Project Structure

```
DailyCal_Automation/
│
├── core/                          # Core utilities and configurations
│   ├── __init__.py
│   ├── driver_setup.py           # Appium driver initialization
│   ├── activities.py             # Common actions (click, fill, etc.)
│   ├── locators.py               # Page Object locators
│   └── necessary_packages.py     # Shared imports
│
├── features/                      # Feature-specific page objects
│   ├── home_page.py
│   ├── nutrition_page.py
│   ├── water_settings_page.py
│   ├── update_current_weight_page.py
│   └── update_goal_weight_page.py
│
├── signin_pages/                  # Sign-in flow pages
│   ├── Step1.py
│   ├── Step2.py
│   ├── Step3.py
│   ├── Step4.py
│   ├── Step5.py
│   └── Step6.py
│
├── core_features_regression/      # Core feature implementations
│   ├── exercise.py
│   ├── scan_food.py
│   └── save_food.py
│
├── premium_features/              # Premium feature implementations
│   ├── exercise/
│   ├── food_database/
│   └── scan_food/
│
├── tests/                         # Test files
│   ├── conftest.py               # Pytest fixtures
│   ├── test_signin_functionality.py
│   ├── test_core_feature_functionality.py
│   └── ...
│
├── Test Data/                     # JSON test data files
│   ├── Signin_pages/
│   ├── Features/
│   ├── Water_settings/
│   └── ...
│
├── reports/                       # Test reports
│   └── assets/
│
├── config/                        # Configuration files
│   ├── config.py
│   └── .env.example
│
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest configuration
├── .env.example                   # Environment variables template
└── README.md                      # This file
```

## 📊 Test Coverage

### Feature Coverage

| Feature Area | Test Cases | Coverage % |
|--------------|------------|------------|
| Sign-In Flow | 50-60 | 90% |
| Exercise Features | 30-40 | 85% |
| Food Features | 20-25 | 80% |
| Nutrition Page | 25-30 | 85% |
| Water Settings | 15-20 | 90% |
| Weight Management | 15-20 | 85% |
| Today's Burn | 20-30 | 80% |
| Integration Tests | 5-10 | 70% |
| **TOTAL** | **155-220** | **~85%** |

## 🐛 Troubleshooting

### Common Issues

#### Issue: "No connected Android devices found"
**Solution:**
- Check if device is connected: `adb devices`
- Enable USB Debugging on device
- Install USB drivers if needed

#### Issue: "Appium server not running"
**Solution:**
- Start Appium server: `appium`
- Check if port 4723 is available
- Verify Appium installation: `appium --version`

#### Issue: "Module not found" errors
**Solution:**
- Activate virtual environment
- Install dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version`

#### Issue: "Element not found" errors
**Solution:**
- Increase timeout in config
- Check if app is installed on device
- Verify locators in `core/locators.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Run tests: `pytest`
5. Commit changes: `git commit -m "Add new feature"`
6. Push to branch: `git push origin feature/new-feature`
7. Create Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to all functions
- Write unit tests for new features
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Appium community
- Selenium community
- Pytest framework

## 📞 Support

For issues and questions:
- Create an issue in GitHub
- Contact: your.email@company.com

---

**Last Updated:** 2024
**Version:** 1.0.0
```

---

## 2. PROFESSIONAL DOCSTRINGS

### **Google Style Docstring (Recommended)**

#### **Example 1: Simple Function**

**BEFORE (Current Code):**
```python
def go_to_step_2(driver,day,month,year):
    print("Going to step 2")
    fill_input_field(driver, Step_1.input_filed, day, index=0)
    fill_input_field(driver, Step_1.input_filed, month, index=1)
    fill_input_field(driver, Step_1.input_filed, year, index=2)
    click_on(driver, Step_1.next_button)
```

**AFTER (Professional):**
```python
def go_to_step_2(driver: WebDriver, day: str, month: str, year: str) -> None:
    """
    Navigate from Step 1 to Step 2 by filling birthdate information.
    
    This function fills the day, month, and year fields in Step 1 of the
    sign-in flow and clicks the Next button to proceed to Step 2.
    
    Args:
        driver: Appium WebDriver instance for mobile automation.
        day: Day of birth in DD format (e.g., "15", "05").
        month: Month of birth in MM format (e.g., "06", "12").
        year: Year of birth in YYYY format (e.g., "2000", "1995").
    
    Raises:
        TimeoutException: If elements are not found within the timeout period.
        ElementNotInteractableException: If elements cannot be interacted with.
    
    Example:
        >>> driver = setup_driver()
        >>> go_to_step_2(driver, "15", "06", "2000")
        >>> # User is now on Step 2 page
    
    Note:
        This function assumes the user is already on Step 1 of the sign-in flow.
        The function will wait for elements with the default timeout (30 seconds).
    """
    logger.info(f"Navigating to Step 2 with birthdate: {day}/{month}/{year}")
    
    fill_input_field(driver, Step_1.input_filed, day, index=0)
    fill_input_field(driver, Step_1.input_filed, month, index=1)
    fill_input_field(driver, Step_1.input_filed, year, index=2)
    click_on(driver, Step_1.next_button)
    
    logger.info("Successfully navigated to Step 2")
```

#### **Example 2: Function with Return Value**

**BEFORE (Current Code):**
```python
def check_run_preset_intensity_duration(driver):
    go_to_run(driver)
    click_on(driver,intensity_set_duration.medium_intensity)
    click_on(driver,intensity_set_duration.duration_30min)
    click_on(driver, intensity_set_duration.add_button)
    time.sleep(1)
    actual=match_element(driver,Home_page.testing_title_run_exercise).upper()
    print(actual)
    current_time = datetime.now().strftime("%I:%M %p").upper()
    expected_values = [current_time, "RUN", "368"]
    return all(val in actual for val in expected_values)
```

**AFTER (Professional):**
```python
def check_run_preset_intensity_duration(driver: WebDriver) -> bool:
    """
    Test Run exercise with preset intensity and duration.
    
    This function tests the Run exercise feature by selecting a preset
    intensity level (Medium) and preset duration (30 minutes), then
    validates that the exercise is correctly logged in the activity list.
    
    Args:
        driver: Appium WebDriver instance for mobile automation.
    
    Returns:
        bool: True if the exercise is correctly logged with expected values
              (current time, "RUN" text, and "368" calories), False otherwise.
    
    Raises:
        TimeoutException: If elements are not found within the timeout period.
        ElementNotInteractableException: If elements cannot be clicked.
    
    Example:
        >>> driver = setup_driver()
        >>> result = check_run_preset_intensity_duration(driver)
        >>> assert result == True, "Run exercise test failed"
    
    Note:
        The function expects the user to be on the home page.
        Expected calories burned for 30 min Medium intensity Run: 368 calories.
    """
    logger.info("Testing Run exercise with preset intensity and duration")
    
    # Navigate to Run exercise page
    go_to_run(driver)
    
    # Select Medium intensity
    click_on(driver, intensity_set_duration.medium_intensity)
    logger.debug("Selected Medium intensity")
    
    # Select 30 minutes duration
    click_on(driver, intensity_set_duration.duration_30min)
    logger.debug("Selected 30 minutes duration")
    
    # Add exercise
    click_on(driver, intensity_set_duration.add_button)
    time.sleep(1)  # Wait for activity to be logged
    
    # Validate exercise in activity list
    actual = match_element(driver, Home_page.testing_title_run_exercise).upper()
    logger.debug(f"Actual exercise text: {actual}")
    
    # Prepare expected values
    current_time = datetime.now().strftime("%I:%M %p").upper()
    expected_values = [current_time, "RUN", "368"]
    
    # Check if all expected values are present
    result = all(val in actual for val in expected_values)
    
    if result:
        logger.info("✅ Run exercise test passed")
    else:
        logger.error(f"❌ Run exercise test failed. Expected: {expected_values}, Actual: {actual}")
    
    return result
```

#### **Example 3: Complex Function with Multiple Parameters**

**BEFORE (Current Code):**
```python
def fill_input_field(driver, locator, value, index=0, timeout=30):
    """
    Clicks, clears, and sends keys to an input field at a given index.
    """
    wait = WebDriverWait(driver, timeout)
    fields = wait.until(EC.presence_of_all_elements_located(locator))
    if len(fields) <= index:
        raise Exception(f"Not enough input fields found (index {index})")
    field = fields[index]
    field.click()
    time.sleep(0.5)
    field.clear()
    field.send_keys(value)
    return field
```

**AFTER (Professional):**
```python
def fill_input_field(
    driver: WebDriver,
    locator: Tuple[By, str],
    value: str,
    index: int = 0,
    timeout: int = 30
) -> WebElement:
    """
    Fill an input field with the specified value.
    
    This function finds an input field by locator, waits for it to be present,
    clicks on it, clears existing content, and enters the new value.
    If multiple fields match the locator, the function selects the one at
    the specified index.
    
    Args:
        driver: Appium/Selenium WebDriver instance.
        locator: Tuple of (By strategy, locator string), e.g., (By.XPATH, "//input[@id='name']").
        value: The text value to enter into the input field.
        index: Zero-based index of the field if multiple fields match the locator.
               Defaults to 0 (first field).
        timeout: Maximum time in seconds to wait for the element to be present.
                 Defaults to 30 seconds.
    
    Returns:
        WebElement: The input field element that was filled.
    
    Raises:
        TimeoutException: If the element(s) are not found within the timeout period.
        IndexError: If the specified index is greater than the number of found elements.
        ElementNotInteractableException: If the element cannot be clicked or filled.
    
    Example:
        >>> from selenium.webdriver.common.by import By
        >>> locator = (By.CLASS_NAME, "android.widget.EditText")
        >>> field = fill_input_field(driver, locator, "John Doe", index=0)
        >>> assert field.get_attribute("text") == "John Doe"
    
    Note:
        The function includes a 0.5 second sleep after clicking to ensure
        the field is ready for input. This may need adjustment based on
        app performance.
    """
    logger.debug(f"Filling input field at index {index} with value: {value}")
    
    # Wait for elements to be present
    wait = WebDriverWait(driver, timeout)
    fields = wait.until(EC.presence_of_all_elements_located(locator))
    
    # Validate index
    if len(fields) <= index:
        error_msg = (
            f"Not enough input fields found. "
            f"Expected at least {index + 1}, but found {len(fields)}"
        )
        logger.error(error_msg)
        raise IndexError(error_msg)
    
    # Get the target field
    field = fields[index]
    
    # Interact with field
    field.click()
    time.sleep(0.5)  # Wait for field to be ready
    field.clear()
    field.send_keys(value)
    
    logger.debug(f"Successfully filled input field with value: {value}")
    return field
```

#### **Example 4: Class Documentation**

**BEFORE (Current Code):**
```python
class Step_1:
    step_no=(By.XPATH,'//android.view.View[@content-desc="Step 1 of 6"]')
    female=(By.XPATH,'//android.widget.ImageView[@content-desc="female"]')
    male=(By.XPATH,'//android.widget.ImageView[@content-desc="male"]')
    Other=(By.XPATH,'//android.widget.ImageView[@content-desc="other"]')
    input_filed=(By.CLASS_NAME,'android.widget.EditText')
    next_button=(By.XPATH,'//android.widget.Button[@content-desc="Next"]')
```

**AFTER (Professional):**
```python
class Step1:
    """
    Page Object for Step 1 of the sign-in flow.
    
    Step 1 collects user's gender and birthdate information. The page contains
    gender selection buttons (Male, Female, Other), birthdate input fields
    (Day, Month, Year), and a Next button to proceed to Step 2.
    
    Attributes:
        step_no: Locator for the step indicator text ("Step 1 of 6").
        female: Locator for the Female gender selection button.
        male: Locator for the Male gender selection button.
        other: Locator for the Other gender selection button.
        input_field: Locator for birthdate input fields (Day, Month, Year).
                    Access fields by index: 0=Day, 1=Month, 2=Year.
        next_button: Locator for the Next button to proceed to Step 2.
    
    Example:
        >>> from core.locators import Step1
        >>> click_on(driver, Step1.male)
        >>> fill_input_field(driver, Step1.input_field, "15", index=0)  # Day
        >>> fill_input_field(driver, Step1.input_field, "06", index=1)  # Month
        >>> fill_input_field(driver, Step1.input_field, "2000", index=2)  # Year
        >>> click_on(driver, Step1.next_button)
    
    Note:
        All locators use XPath or ClassName strategies. The input_field
        locator matches multiple EditText elements, so use index parameter
        when interacting with specific fields.
    """
    
    # Step indicator
    step_no = (By.XPATH, '//android.view.View[@content-desc="Step 1 of 6"]')
    
    # Gender selection buttons
    female = (By.XPATH, '//android.widget.ImageView[@content-desc="female"]')
    male = (By.XPATH, '//android.widget.ImageView[@content-desc="male"]')
    other = (By.XPATH, '//android.widget.ImageView[@content-desc="other"]')
    
    # Input fields (Day=0, Month=1, Year=2)
    input_field = (By.CLASS_NAME, 'android.widget.EditText')
    
    # Navigation button
    next_button = (By.XPATH, '//android.widget.Button[@content-desc="Next"]')
```

---

## 3. STANDARD CODING EXAMPLES

### **Example 1: Import Organization**

**BEFORE (Current Code):**
```python
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core.necessary_packages import *
```

**AFTER (Professional - PEP 8 Standard):**
```python
"""
Core utility functions for mobile automation interactions.

This module provides common actions like clicking, filling fields, and
scrolling that are used across the automation framework.
"""

# Standard library imports
import time
from typing import Tuple, Optional, Dict, Any

# Third-party imports
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementNotInteractableException
)

# Local application imports
from core.config import DEFAULT_TIMEOUT, ELEMENT_WAIT_DELAY
from core.locators import Step1
import logging

# Configure logger
logger = logging.getLogger(__name__)
```

### **Example 2: Constants and Configuration**

**BEFORE (Current Code - Magic Numbers):**
```python
def fill_input_field(driver, locator, value, index=0, timeout=30):
    field.click()
    time.sleep(0.5)  # Magic number
    field.clear()
```

**AFTER (Professional - Constants):**
```python
# At top of file or in config.py
# Constants
DEFAULT_TIMEOUT = 30
ELEMENT_WAIT_DELAY = 0.5
MAX_RETRY_ATTEMPTS = 3
RETRY_DELAY = 1.0

# Use constants
def fill_input_field(
    driver: WebDriver,
    locator: Tuple[By, str],
    value: str,
    index: int = 0,
    timeout: int = DEFAULT_TIMEOUT
) -> WebElement:
    field.click()
    time.sleep(ELEMENT_WAIT_DELAY)  # Using constant
    field.clear()
```

### **Example 3: Error Handling**

**BEFORE (Current Code):**
```python
def match_element(driver, locator_value,timeout=30):
    wait=WebDriverWait(driver,timeout)
    field=wait.until(EC.presence_of_element_located((locator_value)))
    text=field.get_attribute('content-desc').strip().lower()
    return text
```

**AFTER (Professional):**
```python
def match_element(
    driver: WebDriver,
    locator_value: Tuple[By, str],
    timeout: int = DEFAULT_TIMEOUT
) -> str:
    """
    Get the content-desc attribute of an element.
    
    Args:
        driver: WebDriver instance.
        locator_value: Tuple of (By strategy, locator string).
        timeout: Maximum wait time in seconds.
    
    Returns:
        str: Lowercased and stripped content-desc text.
    
    Raises:
        TimeoutException: If element not found within timeout.
        AttributeError: If element doesn't have content-desc attribute.
    """
    try:
        wait = WebDriverWait(driver, timeout)
        field = wait.until(EC.presence_of_element_located(locator_value))
        text = field.get_attribute('content-desc')
        
        if text is None:
            logger.warning(f"Element {locator_value} has no content-desc attribute")
            return ""
        
        return text.strip().lower()
    
    except TimeoutException:
        logger.error(f"Element not found within {timeout} seconds: {locator_value}")
        raise
    except AttributeError as e:
        logger.error(f"Error getting attribute from element: {e}")
        raise
```

### **Example 4: Naming Conventions**

**BEFORE (Current Code - Inconsistent):**
```python
class Step_1:  # Underscore
class OnBoarding:  # PascalCase
def go_to_step_2(driver,day,month,year):  # Inconsistent spacing
def check_run_preset_intensity_duration(driver):  # Good
```

**AFTER (Professional - PEP 8):**
```python
# Classes: PascalCase (no underscores)
class Step1:
class OnBoarding:
class CreateAccount:

# Functions: snake_case
def go_to_step_2(driver: WebDriver, day: str, month: str, year: str) -> None:
def check_run_preset_intensity_duration(driver: WebDriver) -> bool:

# Constants: UPPER_SNAKE_CASE
DEFAULT_TIMEOUT = 30
MAX_RETRY_ATTEMPTS = 3

# Variables: snake_case
device_udid = "emulator-5554"
test_results = []
```

### **Example 5: Type Hints**

**BEFORE (Current Code - No Types):**
```python
def validation_of_birthdate(driver, day, month, year):
    # No type information
```

**AFTER (Professional - With Type Hints):**
```python
from typing import Tuple, Optional, Dict, Any, List
from selenium.webdriver.remote.webdriver import WebDriver

def validation_of_birthdate(
    driver: WebDriver,
    day: str,
    month: str,
    year: str
) -> bool:
    """
    Validate birthdate input in Step 1.
    
    Args:
        driver: WebDriver instance.
        day: Day as string (e.g., "15").
        month: Month as string (e.g., "06").
        year: Year as string (e.g., "2000").
    
    Returns:
        bool: True if validation passed, False otherwise.
    """
    # Implementation
```

---

## 4. CONFIGURATION FILES

### **config.py (Professional)**

```python
"""
Configuration management for DailyCal Automation Framework.

This module handles all configuration settings including Appium server URLs,
app package information, device settings, and timeouts. Configuration can
be loaded from environment variables or default values.
"""

import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Appium Configuration
APPIUM_SERVER_URL = os.getenv(
    'APPIUM_SERVER_URL',
    'http://127.0.0.1:4723/wd/hub'
)

# App Configuration
APP_PACKAGE = os.getenv('APP_PACKAGE', 'com.dailycalai.app')
APP_ACTIVITY = os.getenv('APP_ACTIVITY', 'com.dailycalai.app.MainActivity')
APK_PATH = os.getenv('APK_PATH', '')

# Device Configuration
DEVICE_UDID: Optional[str] = os.getenv('DEVICE_UDID') or None
USE_EMULATOR = os.getenv('USE_EMULATOR', 'false').lower() == 'true'

# Timeout Configuration (in seconds)
DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', '30'))
ELEMENT_WAIT_DELAY = float(os.getenv('ELEMENT_WAIT_DELAY', '0.5'))
MAX_RETRY_ATTEMPTS = int(os.getenv('MAX_RETRY_ATTEMPTS', '3'))
RETRY_DELAY = float(os.getenv('RETRY_DELAY', '1.0'))

# Test Data Paths
TEST_DATA_DIR = BASE_DIR / 'Test Data'
SIGNIN_TEST_DATA_DIR = TEST_DATA_DIR / 'Signin_pages'
FEATURES_TEST_DATA_DIR = TEST_DATA_DIR / 'Features'
WATER_TEST_DATA_DIR = TEST_DATA_DIR / 'Water_settings'

# Report Paths
REPORTS_DIR = BASE_DIR / 'reports'
REPORTS_DIR.mkdir(exist_ok=True)

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = os.getenv(
    'LOG_FORMAT',
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Appium Capabilities
APPIUM_CAPABILITIES = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'newCommandTimeout': 300,
    'autoGrantPermissions': True,
    'ensureWebviewsHavePages': True,
    'dontStopAppOnReset': True,
}
```

### **.env.example (Template)**

```env
# Appium Server Configuration
APPIUM_SERVER_URL=http://127.0.0.1:4723/wd/hub

# Application Configuration
APP_PACKAGE=com.dailycalai.app
APP_ACTIVITY=com.dailycalai.app.MainActivity
APK_PATH=

# Device Configuration
# Leave empty for auto-detection
DEVICE_UDID=
USE_EMULATOR=false

# Timeout Configuration (seconds)
DEFAULT_TIMEOUT=30
ELEMENT_WAIT_DELAY=0.5
MAX_RETRY_ATTEMPTS=3
RETRY_DELAY=1.0

# Logging Configuration
LOG_LEVEL=INFO
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

---

## 5. REQUIREMENTS.TXT

### **Professional requirements.txt**

```txt
# DailyCal Automation Framework - Python Dependencies
# Python 3.9+ required

# Core Automation Frameworks
selenium>=4.15.0
Appium-Python-Client>=3.1.0

# Testing Framework
pytest>=7.4.0
pytest-html>=4.1.0
pytest-xdist>=3.5.0  # For parallel test execution
pytest-timeout>=2.2.0  # For test timeout management

# Configuration Management
python-dotenv>=1.0.0

# Logging and Reporting
colorama>=0.4.6  # Colored terminal output

# Type Checking (Optional but recommended)
mypy>=1.7.0
types-requests>=2.31.0

# Code Quality Tools (Development dependencies)
black>=23.11.0  # Code formatter
flake8>=6.1.0  # Linter
pylint>=3.0.0  # Advanced linter (optional)

# Documentation (Optional)
sphinx>=7.2.0  # Documentation generator
```

---

## 6. CODE FORMATTING STANDARDS

### **PEP 8 Compliance**

#### **Line Length:**
- Maximum 79 characters per line (or 99 for modern projects)
- Use parentheses for line continuation

**BEFORE:**
```python
def validate_birthdate(driver, day, month, year):
    result = fill_input_field(driver, Step_1.input_filed, day, index=0) and fill_input_field(driver, Step_1.input_filed, month, index=1) and fill_input_field(driver, Step_1.input_filed, year, index=2)
```

**AFTER:**
```python
def validate_birthdate(
    driver: WebDriver,
    day: str,
    month: str,
    year: str
) -> bool:
    result = (
        fill_input_field(driver, Step1.input_field, day, index=0) and
        fill_input_field(driver, Step1.input_field, month, index=1) and
        fill_input_field(driver, Step1.input_field, year, index=2)
    )
```

#### **Spacing:**
- One space after commas
- No spaces around `=` in function arguments
- Spaces around operators

**BEFORE:**
```python
def test_function(driver,day,month,year):
    x=5+3
    y =x*2
```

**AFTER:**
```python
def test_function(driver: WebDriver, day: str, month: str, year: str) -> None:
    x = 5 + 3
    y = x * 2
```

#### **Function and Class Definitions:**
- Two blank lines before class definitions
- One blank line before function definitions
- One blank line between methods

**BEFORE:**
```python
class Step1:
    def method1(self):
        pass
    def method2(self):
        pass
```

**AFTER:**
```python
class Step1:
    """Page Object for Step 1."""
    
    def method1(self) -> None:
        """Method 1."""
        pass
    
    def method2(self) -> None:
        """Method 2."""
        pass
```

---

## 📝 SUMMARY CHECKLIST

### **Documentation:**
- [ ] Professional README.md with all sections
- [ ] Docstrings for all functions (Google style)
- [ ] Class docstrings
- [ ] Module docstrings
- [ ] Inline comments for complex logic

### **Code Quality:**
- [ ] Type hints on all functions
- [ ] PEP 8 compliant naming
- [ ] Constants instead of magic numbers
- [ ] Proper error handling
- [ ] No wildcard imports
- [ ] Organized imports (stdlib, third-party, local)

### **Configuration:**
- [ ] requirements.txt
- [ ] config.py with environment variables
- [ ] .env.example template
- [ ] pytest.ini configuration

### **Standards:**
- [ ] Consistent naming conventions
- [ ] Proper spacing and formatting
- [ ] Meaningful variable names
- [ ] No commented code blocks
- [ ] Proper logging instead of print statements

---

**This guide provides professional standards for your automation framework!**

