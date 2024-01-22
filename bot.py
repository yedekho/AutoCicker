from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Get the webdriver for Firefox 
# Install geckodriver and add it to your system PATH
# https://github.com/mozilla/geckodriver/releases
driver = webdriver.Firefox() 

# Repeat our actions in a loop
while True:

    # Go to initial page
    driver.get("https://shrs.link/0cGhFo")

    # Find all links with class='ob-dynamic-rec-link'
    # These have the Outbrain URLs
    links = driver.find_elements(By.CSS_SELECTOR, "a.ob-dynamic-rec-link")

    # Select a random link to click
    random_link = random.choice(links)
    random_link.click()

    # Wait 6 seconds on the Outbrain URL
    time.sleep(6)  

    # Go back in browser history to repeat
    driver.back()
    
    # Wait 2 seconds before repeating the loop
    time.sleep(2)
