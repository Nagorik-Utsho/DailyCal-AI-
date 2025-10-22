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

def adb_hard_tap(x, y, device_udid="R4BW600110K"):
    """
    Perform a single tap on the screen at the given position using ADB.
    """
    print(f"Trying to tap at ({x}, {y})")

    cmd = ["adb"]
    if device_udid:
        cmd += ["-s", device_udid]

    # Single tap
    cmd += ["shell", "input", "tap", str(x), str(y)]

    subprocess.run(cmd, check=True)
    time.sleep(0.3)  # small delay to ensure tap registers
    print(f"✅ ADB tapped at ({x}, {y})")




