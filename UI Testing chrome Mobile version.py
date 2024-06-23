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

    # Capture screenshot and save
    screenshot_path = os.path.join(device_name, resolution, f"screenshot-{time.strftime('%Y%m%d-%H%M%S')}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")


def open_website_in_mobile_resolution(url, width, height, device_name):
    chrome_options = ChromeOptions()
    mobile_emulation = {
        "deviceMetrics": {"width": width, "height": height, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)


    driver.get(url)

    take_screenshot(driver, device_name, f"{width}x{height}")


    driver.quit()

urls=["https://www.getcalley.com/",
       "https://www.getcalley.com/calley-call-from-browser/",
       "https://www.getcalley.com/calley-pro-features/",
       "https://www.getcalley.com/best-auto-dialer-app/",
       "https://www.getcalley.com/how-calley-auto-dialer-app-works/"
 ]


device_name = "iPhone12Pro"


mobile_resolutions = [(360, 640), (414, 896), (375, 667)]

# Iterate over each URL and resolution
for url in urls:
    for resolution in mobile_resolutions:
        width, height = resolution
        open_website_in_mobile_resolution(url, width, height, device_name)
        time.sleep(2)
