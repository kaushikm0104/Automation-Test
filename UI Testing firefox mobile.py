from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

def open_website_in_mobile_resolution(url, width, height):

    firefox_options = FirefoxOptions()
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/14.0 Mobile/15A372 Safari/604.1"
    firefox_options.set_preference("general.useragent.override", user_agent)
    firefox_options.set_preference("layout.css.devPixelsPerPx", "3.0")

    driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)

    driver.set_window_size(width, height)

    driver.get(url)

    time.sleep(5)

    driver.quit()

urls = ["https://www.getcalley.com/",
       "https://www.getcalley.com/calley-call-from-browser/",
       "https://www.getcalley.com/calley-pro-features/",
       "https://www.getcalley.com/best-auto-dialer-app/",
       "https://www.getcalley.com/how-calley-auto-dialer-app-works/"
 ]

mobile_resolutions = [(360, 640), (414, 896), (375, 667)]

for url in urls:
    for resolution in mobile_resolutions:
        width, height = resolution
        open_website_in_mobile_resolution(url, width, height)
