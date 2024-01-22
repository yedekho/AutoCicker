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

# Check GLIBC version (adjust command based on your server)
glibc_version = ""
try:
    glibc_version = open("/proc/version", "r").read().split()[2]
except:
    print("Error reading GLIBC version")

# Choose ChromeDriver based on installed GLIBC version
chrome_driver_path = None
if glibc_version.startswith("GLIBC_2.29"):
    chrome_driver_path = "path/to/chromedriver_glibc_2.29.exe"  # Update with actual path for downloaded binary
elif glibc_version.startswith("GLIBC_2.27"):
    chrome_driver_path = "path/to/chromedriver_glibc_2.27.exe"  # Update with actual path for downloaded binary
else:
    print(f"Unknown GLIBC version: {glibc_version}")

# Set ChromeDriver location and PATH environment variable (adjust paths as needed)
if chrome_driver_path:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    # Specify path to downloaded ChromeDriver binary
    chrome_options.binary_location = chrome_driver_path

    # Set PATH environment variable (ensure it persists across deployments)
    os.environ["PATH"] = f"{os.environ['PATH']}:{chrome_driver_path}"

    driver = webdriver.Chrome(options=chrome_options)
else:
    print("Unable to find compatible ChromeDriver for installed GLIBC version")
    exit(1)

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


