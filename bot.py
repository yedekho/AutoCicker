import requests
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Download ChromeDriver (optional, if not uploaded to your repo)
# url = "https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip"
# response = requests.get(url)
# with open('chromedriver.zip', 'wb') as f:
#   f.write(response.content)

# Unzip ChromeDriver (optional, if not uploaded to your repo)
# with zipfile.ZipFile("chromedriver.zip","r") as zip_ref:
#    zip_ref.extractall()

# Set ChromeDriver location
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

# Replace "path/to/chromedriver.exe" with the actual path to your local or repository chromedriver executable
chrome_options.binary_location = "path/to/chromedriver.exe"

driver = webdriver.Chrome(options=chrome_options)

# Bot logic
while True:

  driver.get("https://shrs.link/0cGhFo")

  links = driver.find_elements(By.PARTIAL_LINK_TEXT, "https://paid.outbrain.com")

  random_link = random.choice(links)
  random_link.click()

  time.sleep(6)  

  driver.back()

  time.sleep(2)

driver.quit() # Close the browser after the bot is done
