from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

def open_website_in_resolution(url, width, height):

    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--window-size={width},{height}")


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
resolutions = [(1920, 1080), (1366, 768), (1536, 864)]

for url in url:
    for resolution in mobile_resolutions:
        width, height = resolution
        open_website_in_mobile_resolution(url, width, height)
