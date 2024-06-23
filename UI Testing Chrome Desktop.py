from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from PIL import Image
import time
import os


def take_screenshot(driver, device_name, resolution):

    if not os.path.exists(device_name):
        os.makedirs(device_name)
    if not os.path.exists(os.path.join(device_name, resolution)):
        os.makedirs(os.path.join(device_name, resolution))


    screenshot_path = os.path.join(device_name, resolution, f"screenshot-{time.strftime('%Y%m%d-%H%M%S')}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")


def open_website_in_resolution(url, width, height, device_name):

    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--window-size={width},{height}")


    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    driver.get(url)

    take_screenshot(driver, device_name, f"{width}x{height}")

    driver.quit()

urls = ["https://www.getcalley.com/",
       "https://www.getcalley.com/calley-call-from-browser/",
       "https://www.getcalley.com/calley-pro-features/",
       "https://www.getcalley.com/best-auto-dialer-app/",
       "https://www.getcalley.com/how-calley-auto-dialer-app-works/"
 ]

device_name = "DesktopChrome"

desktop_resolutions = [(1920, 1080), (1366, 768), (1536, 864)]

for url in urls:
    for resolution in desktop_resolutions:
        width, height = resolution
        open_website_in_resolution(url, width, height, device_name)
        time.sleep(2)

