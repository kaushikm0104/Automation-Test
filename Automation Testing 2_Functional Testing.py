from appium.webdriver.extensions.keyboard import Keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

serv_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.dealsdray.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("prexo.mis@dealsdray.com")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("prexo.mis@dealsdray.com")
time.sleep(1)
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".MuiButtonBase-root.has-submenu.compactNavItem.css-46up3a").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@href='/mis/orders']//button[@name='child']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Add Bulk Orders']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='MuiOutlinedInput-root MuiInputBase-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall css-uodm64'])[1]").click()
time.sleep(2)
keyboard = Controller()
keyboard.type("C:\\Users\\kaush\\Downloads\\demo-data.xlsx")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Import']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Validate Data']").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(5)
# Close the browser
driver.quit()
