from selenium import webdriver
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

#Ignore Errors
options = webdriver.ChromeOptions()
options.add_argument('--start-maximixed')

#WebDriver
driver= webdriver.Chrome(executable_path='./webdriver/chromedriver.exe', chrome_options=options)

driver.get('https://web.whatsapp.com/send?phone=+34')

time.sleep(20)

driver.find_element(by=By.CLASS_NAME, value="p3_M1").click()
pyautogui.typewrite("")
pyautogui.press("enter")




