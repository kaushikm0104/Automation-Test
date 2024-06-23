from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


def open_website_in_mobile_resolution(url, width, height):
    chrome_options = ChromeOptions()
    mobile_emulation = {
        "deviceMetrics": {"width": width, "height": height, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    driver.get(url)

    time.sleep(5)

    driver.quit()

url = ["https://www.getcalley.com/",
       "https://www.getcalley.com/calley-call-from-browser/",
       "https://www.getcalley.com/calley-pro-features/",
       "https://www.getcalley.com/best-auto-dialer-app/",
       "https://www.getcalley.com/how-calley-auto-dialer-app-works/"
 ]
mobile_resolutions = [(360, 640), (414, 896), (375, 667)]

for url in url:
    for resolution in mobile_resolutions:
        width, height = resolution
        open_website_in_mobile_resolution(url, width, height)
