from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


def open_website_in_resolution(url, width, height):
    firefox_options = FirefoxOptions()
    firefox_options.add_argument(f"--width={width}")
    firefox_options.add_argument(f"--height={height}")

    driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)

    driver.get(url)

    time.sleep(5)

    driver.quit()

urls = ["https://www.getcalley.com/",
       "https://www.getcalley.com/calley-call-from-browser/",
       "https://www.getcalley.com/calley-pro-features/",
       "https://www.getcalley.com/best-auto-dialer-app/",
       "https://www.getcalley.com/how-calley-auto-dialer-app-works/"
 ]

desktop_resolutions = [(1920, 1080), (1366, 768), (1536, 864)]

for url in urls:
    for resolution in desktop_resolutions:
        width, height = resolution
        open_website_in_resolution(url, width, height)
