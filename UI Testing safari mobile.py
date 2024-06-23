from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def open_website_in_safari(url, width, height):

    BROWSERSTACK_USERNAME = 'kaushik_PAL5g6'
    BROWSERSTACK_ACCESS_KEY = 'Sf61kV8cbfpMphsxWo77'

    desired_cap = {
        'os': 'OS X',
        'os_version': 'Monterey',
        'browser': 'Safari',
        'browser_version': '15.6',
        'deviceName': 'iPhone 15',
        'osVersion': '17',
        'browserName': 'safari',
        'deviceOrientation': 'portrait',
        'name': 'Safari Test',  # test name
        'build': 'Safari Build',  # CI/CD job or build name
        'browserstack.local': 'false'
    }
    options = webdriver.ChromeOptions()
    options.set_capability('browserstack.user', BROWSERSTACK_USERNAME)
    options.set_capability('browserstack.key', BROWSERSTACK_ACCESS_KEY)
    options.set_capability('os', desired_cap['os'])
    options.set_capability('os_version', desired_cap['os_version'])
    options.set_capability('browser', desired_cap['browser'])
    options.set_capability('browser_version', desired_cap['browser_version'])
    options.set_capability('name', desired_cap['name'])
    options.set_capability('build', desired_cap['build'])
    options.set_capability('browserstack.local', desired_cap['browserstack.local'])

    driver = webdriver.Remote(
     command_executor='https://hub-cloud.browserstack.com/wd/hub',
        options=options
    )


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
    for resolution in desktop_resolutions:
        width, height = resolution
        open_website_in_safari(url, width, height)
