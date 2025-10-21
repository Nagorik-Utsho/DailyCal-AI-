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



