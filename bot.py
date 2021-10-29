import os
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By #type : ignore
from selenium.webdriver.support.ui import WebDriverWait #type : ignore
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH']+=r"C:\Users\ADMIN\Desktop\Scarpper"
driver=webdriver.Chrome()

driver.get('https://codeforces.com/problemset')
driver.implicitly_wait(5)
box = driver.find_element_by_css_selector(
    'input[name="minDifficulty"]'
)
box.send_keys(1600)