# Code Examples: Before & After (Professional Standards)

**Real examples from your codebase showing professional improvements**

---

## Example 1: driver_setup.py

### **BEFORE (Current Code):**
```python

from .necessary_packages import *

def get_connected_device_info():
    """
    Detects connected Android devices and fetches UDID and Android version.
    Returns the first device found.
    """
    # Get list of connected devices
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')[1:]  # Skip first line
    devices = [line.split('\t')[0] for line in lines if 'device' in line]

    if not devices:
        raise Exception("No connected Android devices found.")

    device_udid = devices[0]

    # Get Android version
    result_version = subprocess.run(['adb', '-s', device_udid, 'shell', 'getprop', 'ro.build.version.release'],
                                    capture_output=True, text=True)
    android_version = result_version.stdout.strip()

    return device_udid, android_version

def setup_driver():
    device_udid, android_version = get_connected_device_info()

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = android_version
    options.device_name = device_udid
    options.automation_name = "UiAutomator2"
    options.no_reset = True
    options.new_command_timeout = 300
    options.auto_grant_permissions = True
    options.ensure_webviews_have_pages = True
    options.dont_stop_app_on_reset = True

    # Replace with your app info
    options.app_package = "com.dailycalai.app"
    options.app_activity = "com.dailycalai.app.MainActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    print("Driver setup successful for device:", driver.capabilities['deviceName'])

    return driver
```

### **AFTER (Professional Standard):**
```python
"""
Driver setup and configuration for Appium mobile automation.

This module provides functions to initialize and configure the Appium
WebDriver for Android device automation.
"""

import logging
import subprocess
from typing import Tuple, Optional

from appium import webdriver
from appium.options.android import UiAutomator2Options

from core.config import (
    APPIUM_SERVER_URL,
    APP_PACKAGE,
    APP_ACTIVITY,
    DEVICE_UDID,
    APPIUM_CAPABILITIES
)

logger = logging.getLogger(__name__)


class DeviceNotFoundError(Exception):
    """Raised when no Android device is connected."""
    pass


def get_connected_device_info() -> Tuple[str, str]:
    """
    Detect connected Android devices and fetch device UDID and Android version.
    
    This function uses ADB to detect connected Android devices and retrieves
    the first available device's UDID and Android version.
    
    Returns:
        Tuple[str, str]: A tuple containing (device_udid, android_version).
                        Example: ("emulator-5554", "11.0")
    
    Raises:
        DeviceNotFoundError: If no connected Android devices are found.
        subprocess.SubprocessError: If ADB command execution fails.
    
    Example:
        >>> udid, version = get_connected_device_info()
        >>> print(f"Device: {udid}, Android: {version}")
        Device: emulator-5554, Android: 11.0
    """
    logger.info("Detecting connected Android devices...")
    
    try:
        # Get list of connected devices
        result = subprocess.run(
            ['adb', 'devices'],
            capture_output=True,
            text=True,
            check=True
        )
        
        lines = result.stdout.strip().split('\n')[1:]  # Skip header
        devices = [
            line.split('\t')[0]
            for line in lines
            if 'device' in line and '\tdevice' in line
        ]
        
        if not devices:
            error_msg = "No connected Android devices found. Please connect a device or start an emulator."
            logger.error(error_msg)
            raise DeviceNotFoundError(error_msg)
        
        device_udid = devices[0]
        logger.info(f"Found device: {device_udid}")
        
        # Get Android version
        result_version = subprocess.run(
            ['adb', '-s', device_udid, 'shell', 'getprop', 'ro.build.version.release'],
            capture_output=True,
            text=True,
            check=True
        )
        android_version = result_version.stdout.strip()
        logger.info(f"Android version: {android_version}")
        
        return device_udid, android_version
    
    except subprocess.CalledProcessError as e:
        logger.error(f"ADB command failed: {e}")
        raise
    except FileNotFoundError:
        error_msg = "ADB not found. Please ensure Android SDK is installed and in PATH."
        logger.error(error_msg)
        raise DeviceNotFoundError(error_msg)


def setup_driver(
    device_udid: Optional[str] = None,
    android_version: Optional[str] = None
) -> webdriver.Remote:
    """
    Initialize and configure Appium WebDriver for Android automation.
    
    This function creates an Appium WebDriver instance with the specified
    or auto-detected device configuration and app settings.
    
    Args:
        device_udid: Optional device UDID. If None, auto-detects first connected device.
        android_version: Optional Android version. If None, auto-detects from device.
    
    Returns:
        webdriver.Remote: Configured Appium WebDriver instance.
    
    Raises:
        DeviceNotFoundError: If no device is connected and UDID not provided.
        ConnectionError: If unable to connect to Appium server.
    
    Example:
        >>> driver = setup_driver()
        >>> driver.find_element(By.ID, "button")
    
    Note:
        Ensure Appium server is running before calling this function.
        Default server URL: http://127.0.0.1:4723/wd/hub
    """
    logger.info("Setting up Appium WebDriver...")
    
    # Get device info if not provided
    if not device_udid or not android_version:
        detected_udid, detected_version = get_connected_device_info()
        device_udid = device_udid or detected_udid
        android_version = android_version or detected_version
    
    # Use provided UDID or default from config
    final_udid = device_udid or DEVICE_UDID or detected_udid
    
    # Configure Appium options
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = android_version
    options.device_name = final_udid
    options.automation_name = "UiAutomator2"
    
    # Apply capabilities from config
    for key, value in APPIUM_CAPABILITIES.items():
        setattr(options, key, value)
    
    # App configuration
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    
    try:
        # Create driver instance
        driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
        device_name = driver.capabilities.get('deviceName', 'Unknown')
        
        logger.info(f"✅ Driver setup successful for device: {device_name}")
        logger.debug(f"Driver capabilities: {driver.capabilities}")
        
        return driver
    
    except Exception as e:
        logger.error(f"❌ Failed to setup driver: {e}")
        raise ConnectionError(
            f"Unable to connect to Appium server at {APPIUM_SERVER_URL}. "
            f"Ensure Appium server is running. Error: {e}"
        )
```

---

## Example 2: activities.py - fill_input_field

### **BEFORE (Current Code):**
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

### **AFTER (Professional Standard):**
```python
"""
Core utility functions for mobile automation interactions.

This module provides reusable functions for common automation actions
like clicking elements, filling input fields, and scrolling.
"""

import time
import logging
from typing import Tuple, Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementNotInteractableException,
    IndexError as SeleniumIndexError
)

from core.config import (
    DEFAULT_TIMEOUT,
    ELEMENT_WAIT_DELAY
)

logger = logging.getLogger(__name__)


def fill_input_field(
    driver: WebDriver,
    locator: Tuple[By, str],
    value: str,
    index: int = 0,
    timeout: int = DEFAULT_TIMEOUT
) -> WebElement:
    """
    Fill an input field with the specified value.
    
    This function locates an input field using the provided locator, waits
    for it to be present, clicks on it, clears existing content, and enters
    the new value. If multiple fields match the locator, the function selects
    the one at the specified index.
    
    Args:
        driver: Appium/Selenium WebDriver instance.
        locator: Tuple of (By strategy, locator string).
                 Example: (By.XPATH, "//input[@id='name']")
        value: The text value to enter into the input field.
        index: Zero-based index of the field if multiple fields match.
               Defaults to 0 (first field).
        timeout: Maximum time in seconds to wait for element presence.
                 Defaults to DEFAULT_TIMEOUT (30 seconds).
    
    Returns:
        WebElement: The input field element that was filled.
    
    Raises:
        TimeoutException: If elements are not found within the timeout period.
        IndexError: If the specified index exceeds the number of found elements.
        ElementNotInteractableException: If the element cannot be clicked or filled.
    
    Example:
        >>> from selenium.webdriver.common.by import By
        >>> locator = (By.CLASS_NAME, "android.widget.EditText")
        >>> field = fill_input_field(driver, locator, "John Doe", index=0)
        >>> assert field.get_attribute("text") == "John Doe"
    
    Note:
        Includes a small delay (ELEMENT_WAIT_DELAY) after clicking to ensure
        the field is ready for input. This may need adjustment based on app performance.
    """
    logger.debug(
        f"Filling input field at index {index} with value: '{value}' "
        f"(locator: {locator})"
    )
    
    try:
        # Wait for elements to be present
        wait = WebDriverWait(driver, timeout)
        fields = wait.until(EC.presence_of_all_elements_located(locator))
        
        # Validate index
        if len(fields) <= index:
            error_msg = (
                f"Not enough input fields found. "
                f"Expected at least {index + 1}, but found {len(fields)}. "
                f"Locator: {locator}"
            )
            logger.error(error_msg)
            raise IndexError(error_msg)
        
        # Get the target field
        field = fields[index]
        
        # Interact with field
        field.click()
        time.sleep(ELEMENT_WAIT_DELAY)  # Wait for field to be ready
        field.clear()
        field.send_keys(value)
        
        logger.debug(f"✅ Successfully filled input field with value: '{value}'")
        return field
    
    except TimeoutException:
        error_msg = f"Elements not found within {timeout} seconds: {locator}"
        logger.error(error_msg)
        raise
    except ElementNotInteractableException as e:
        error_msg = f"Element at index {index} is not interactable: {e}"
        logger.error(error_msg)
        raise
    except Exception as e:
        error_msg = f"Unexpected error filling input field: {e}"
        logger.error(error_msg)
        raise
```

---

## Example 3: Step1.py - go_to_step_2

### **BEFORE (Current Code):**
```python
def go_to_step_2(driver,day,month,year):

    print("Going to step 2")
    # Fill fields using locators
    fill_input_field(driver, Step_1.input_filed, day, index=0)  # day
    fill_input_field(driver, Step_1.input_filed, month, index=1)  # month
    fill_input_field(driver, Step_1.input_filed, year, index=2)  # year
    # Click on the next button
    click_on(driver, Step_1.next_button)
```

### **AFTER (Professional Standard):**
```python
"""
Step 1 page object for sign-in flow.

This module handles the first step of the sign-in process, which collects
user's gender and birthdate information.
"""

import logging
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

from core.activities import fill_input_field, click_on
from core.locators import Step1
from core.config import DEFAULT_TIMEOUT

logger = logging.getLogger(__name__)


def go_to_step_2(
    driver: WebDriver,
    day: str,
    month: str,
    year: str
) -> None:
    """
    Navigate from Step 1 to Step 2 by filling birthdate information.
    
    This function fills the day, month, and year fields in Step 1 of the
    sign-in flow and clicks the Next button to proceed to Step 2. It assumes
    the user is already on Step 1 and has selected their gender.
    
    Args:
        driver: Appium WebDriver instance for mobile automation.
        day: Day of birth in DD format. Must be a valid day (01-31).
             Example: "15", "05", "31"
        month: Month of birth in MM format. Must be a valid month (01-12).
               Example: "06", "12", "01"
        year: Year of birth in YYYY format. Must be a valid year.
              Example: "2000", "1995", "2010"
    
    Raises:
        TimeoutException: If elements are not found within the timeout period.
        ElementNotInteractableException: If elements cannot be interacted with.
        ValueError: If birthdate values are invalid format.
    
    Example:
        >>> driver = setup_driver()
        >>> # Assume user is on Step 1 and has selected gender
        >>> go_to_step_2(driver, "15", "06", "2000")
        >>> # User is now on Step 2 page
    
    Note:
        - This function assumes the user is already on Step 1
        - Gender must be selected before calling this function
        - The function will wait for elements with the default timeout
        - Date validation is handled by the app, not this function
    """
    logger.info(f"Navigating to Step 2 with birthdate: {day}/{month}/{year}")
    
    # Validate input format (basic validation)
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        error_msg = (
            f"Invalid date format. Day, month, and year must be numeric. "
            f"Received: day={day}, month={month}, year={year}"
        )
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    try:
        # Fill day field
        logger.debug(f"Filling day field: {day}")
        fill_input_field(driver, Step1.input_field, day, index=0)
        
        # Fill month field
        logger.debug(f"Filling month field: {month}")
        fill_input_field(driver, Step1.input_field, month, index=1)
        
        # Fill year field
        logger.debug(f"Filling year field: {year}")
        fill_input_field(driver, Step1.input_field, year, index=2)
        
        # Click Next button to proceed to Step 2
        logger.debug("Clicking Next button")
        click_on(driver, Step1.next_button)
        
        logger.info("✅ Successfully navigated to Step 2")
    
    except Exception as e:
        error_msg = f"Failed to navigate to Step 2: {e}"
        logger.error(error_msg)
        raise
```

---

## Example 4: locators.py - Class Definition

### **BEFORE (Current Code):**
```python
class Step_1:
    step_no=(By.XPATH,'//android.view.View[@content-desc="Step 1 of 6"]')
    female=(By.XPATH,'//android.widget.ImageView[@content-desc="female"]')
    male=(By.XPATH,'//android.widget.ImageView[@content-desc="male"]')
    Other=(By.XPATH,'//android.widget.ImageView[@content-desc="other"]')
    input_filed=(By.CLASS_NAME,'android.widget.EditText')
    next_button=(By.XPATH,'//android.widget.Button[@content-desc="Next"]')
```

### **AFTER (Professional Standard):**
```python
"""
Page Object locators for DailyCal mobile app.

This module contains all locator definitions organized by page/component.
Locators use XPath, ID, or ClassName strategies for element identification.
"""

from selenium.webdriver.common.by import By
from typing import Tuple


class Step1:
    """
    Page Object for Step 1 of the sign-in flow.
    
    Step 1 collects user's gender and birthdate information. The page contains:
    - Gender selection buttons (Male, Female, Other)
    - Birthdate input fields (Day, Month, Year)
    - Navigation button (Next)
    
    Attributes:
        step_no: Locator for the step indicator text ("Step 1 of 6").
        female: Locator for the Female gender selection button.
        male: Locator for the Male gender selection button.
        other: Locator for the Other gender selection button.
        input_field: Locator for birthdate input fields.
                    Fields are accessed by index: 0=Day, 1=Month, 2=Year.
        next_button: Locator for the Next button to proceed to Step 2.
    
    Example:
        >>> from core.locators import Step1
        >>> # Select gender
        >>> click_on(driver, Step1.male)
        >>> # Fill birthdate
        >>> fill_input_field(driver, Step1.input_field, "15", index=0)  # Day
        >>> fill_input_field(driver, Step1.input_field, "06", index=1)  # Month
        >>> fill_input_field(driver, Step1.input_field, "2000", index=2)  # Year
        >>> # Navigate to next step
        >>> click_on(driver, Step1.next_button)
    
    Note:
        - All locators use XPath or ClassName strategies
        - The input_field locator matches multiple EditText elements
        - Use index parameter when interacting with specific fields
        - Locators are tuples of (By strategy, locator string)
    """
    
    # Step indicator
    step_no: Tuple[By, str] = (
        By.XPATH,
        '//android.view.View[@content-desc="Step 1 of 6"]'
    )
    
    # Gender selection buttons
    female: Tuple[By, str] = (
        By.XPATH,
        '//android.widget.ImageView[@content-desc="female"]'
    )
    male: Tuple[By, str] = (
        By.XPATH,
        '//android.widget.ImageView[@content-desc="male"]'
    )
    other: Tuple[By, str] = (
        By.XPATH,
        '//android.widget.ImageView[@content-desc="other"]'
    )
    
    # Birthdate input fields (Day=0, Month=1, Year=2)
    input_field: Tuple[By, str] = (
        By.CLASS_NAME,
        'android.widget.EditText'
    )
    
    # Navigation button
    next_button: Tuple[By, str] = (
        By.XPATH,
        '//android.widget.Button[@content-desc="Next"]'
    )
```

---

## 📋 Quick Reference Checklist

### **Every Function Should Have:**
- [ ] Type hints for all parameters
- [ ] Return type annotation
- [ ] Google-style docstring
- [ ] Proper error handling
- [ ] Logging instead of print statements
- [ ] Constants instead of magic numbers

### **Every Class Should Have:**
- [ ] Class docstring
- [ ] Type hints for attributes
- [ ] PascalCase naming (no underscores)
- [ ] Clear organization

### **Every File Should Have:**
- [ ] Module docstring at top
- [ ] Organized imports (stdlib, third-party, local)
- [ ] Logger configuration
- [ ] No wildcard imports

---

**These examples show the difference between current code and professional standards!**

