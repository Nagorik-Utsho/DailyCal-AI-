import subprocess


def adb_tap_gallery(x, y, device_udid="R4BW600110K"):
    """
    Tap on the screen at coordinates (x, y) using adb.

    :param x: X coordinate
    :param y: Y coordinate
    :param device_udid: Optional, specify device UDID if multiple devices are connected
    """
    cmd = ["adb"]
    if device_udid:
        cmd += ["-s", device_udid]
    cmd += ["shell", "input", "tap", str(x), str(y)]

    subprocess.run(cmd)
    print(f"✅ ADB tapped at ({x}, {y})")





import subprocess
import time

import subprocess

def adb_tap_element_bottom(driver, xpath, device_udid="R4BW600110K", offset=10):
    """
    Tap on the bottom of a given element using adb coordinates.

    :param driver: Appium driver
    :param xpath: XPath of the target element
    :param device_udid: Device UDID (optional if only one device connected)
    :param offset: How far above the bottom edge to tap (in pixels)
    """
    # Find the element using Appium
    element = driver.find_element("xpath", xpath)

    # Get element bounds
    location = element.location
    size = element.size

    # Calculate tap position (bottom-center minus small offset)
    x = location["x"] + size["width"] / 2
    y = location["y"] + size["height"] - offset

    # Build adb command
    cmd = ["adb"]
    if device_udid:
        cmd += ["-s", device_udid]
    cmd += ["shell", "input", "tap", str(int(x)), str(int(y))]

    # Execute adb tap
    subprocess.run(cmd, check=True)
    print(f"✅ ADB tapped near bottom of element at ({int(x)}, {int(y)})")





