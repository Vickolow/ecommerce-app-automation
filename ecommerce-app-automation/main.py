from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
search_box.send_keys(Keys.RETURN)
print("Searched for 'cup warmer'.")
time.sleep(10)

# Locate the product and click to add it to the cart
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