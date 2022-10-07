import time


def capture_screenshot(d, path):
    file_name = path + "scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    d.save_screenshot(file_name)