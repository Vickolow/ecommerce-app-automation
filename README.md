# E-commerce App Automation

This project automates basic workflows for an e-commerce application using Selenium WebDriver.

## Features
- Navigate to the e-commerce website.
- Search for a specific product.
- Add the product to the cart.
- Proceed to checkout.

## Technologies Used
- Python
- Selenium WebDriver

## Setup
1. Clone this repository:
git clone  https://github.com/Vickolow/ecommerce-app-automation.git cd ecommerce-app-automation

2. Install dependencies:

3 
3. Run the script:

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import time



# Initialize WebDriver
driver: WebDriver = webdriver.Chrome()  # Or webdriver.Firefox(), etc.
driver.maximize_window()


# Navigate to Konga
driver.get('https://www.konga.com/')
print("Navigated to Konga's homepage.")
time.sleep(10)

# Search for cup warmer
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[3]/nav/div[2]/div[1]/div/div/div[2]/div/form/div[1]/input')
search_box.send_keys('cup warmer')
time.sleep(10)
search_box.send_keys(Keys.RETURN)
print("Searched for 'cup warmer'.")
time.sleep(10)

# Locate the product and click to add it to the cart
# Note: You may need to update the selector to match the correct button or element
add_to_cart_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[3]/section/main/section[3]/section/section/section/section/ul/li[1]/article/div[2]/form/div[2]/button")
add_to_cart_button.click()
print("Clicked 'Add to Cart' button.")

# Sleep for 5 minutes
time.sleep(10)

# Proceed to checkout
checkout_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/nav/div[2]/div[1]/div/div/a[2]/span[1]")
checkout_button.click()
print("Proceeded to checkout.")
time.sleep(10)

# Add assertions and validations as needed to verify each step
print("Automation script completed successfully!")


# Close the browser window
driver.quit()
