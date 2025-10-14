
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


