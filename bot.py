from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import random

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

while True:

    driver.get("https://shrs.link/0cGhFo")
    
    links = driver.find_elements(By.CSS_SELECTOR, "a.ob-dynamic-rec-link")

    random_link = random.choice(links)
    random_link.click()

    time.sleep(6)   

    driver.back()
    
    time.sleep(2)
