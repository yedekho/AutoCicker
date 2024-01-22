from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import random

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

while True:
    
    # Go to initial page
    driver.get("https://shrs.link/0cGhFo")
    
    # Find links containing outbrain URL
    links = driver.find_elements(By.PARTIAL_LINK_TEXT, "https://paid.outbrain.com")
    
    # Pick random link to click
    random_link = random.choice(links)
    random_link.click()
    
    # Wait 6 seconds
    time.sleep(6)
    
    # Go back
    driver.back()

    # Wait 2 seconds
    time.sleep(2)
