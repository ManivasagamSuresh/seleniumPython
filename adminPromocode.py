from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize ChromeDriver
driver = webdriver.Chrome()

try:
    # Open the Admin Panel login page
    driver.get("https://uat.ayoo.care/ayooadmin/login")
    driver.maximize_window()
    driver.implicitly_wait(5)  # Implicit wait

  
    driver.find_element(By.ID, "username").send_keys("admin@ayoo.care")
    driver.find_element(By.ID, "password").send_keys("ayoo-admin-uat!")
    driver.find_element(By.ID, "loginbtn").click()

    
    driver.find_element(By.XPATH, "(//span[contains(text(),'Promo Code')])[1]").click()

   
    driver.find_element(By.XPATH, "(//span[contains(text(),'All Promo Codes')])[1]").click()
    time.sleep(2)  
    driver.back() 

    
    driver.find_element(By.XPATH, "(//span[contains(text(),'Promo Code')])[1]").click()
    driver.find_element(By.XPATH, "(//span[contains(text(),'Create Promo Code')])[1]").click()

    # Fill out the Promo Code form
    driver.find_element(By.XPATH, "//label[text()='Promotion Code'][1]/following-sibling::input").send_keys("AYOO102")
    driver.find_element(By.XPATH, "//label[text()='Promotion Name'][1]/following-sibling::input").send_keys("Discount")
    driver.find_element(By.XPATH, "//label[text()='Promotion Description'][1]/following-sibling::input").send_keys("Testing")
    
    # Select Discount Type
    discount_type_dropdown = driver.find_element(By.XPATH, "//label[text()='Discount Type']//following-sibling::select")
    Select(discount_type_dropdown).select_by_index(2)
    
    # Enter other fields
    driver.find_element(By.XPATH, "//label[text()='Discount Of']//following-sibling::input").send_keys("100")
    driver.find_element(By.XPATH, "//label[text()='Max use(per user)']//following-sibling::input").send_keys("10")
    driver.find_element(By.XPATH, "//label[text()='Valid From']//following-sibling::input").send_keys("05-22-2024")
    driver.find_element(By.XPATH, "//label[text()='Valid Until']//following-sibling::input").send_keys("06-22-2024")

    # Click "Create" button
    driver.find_element(By.XPATH, "//button[contains(text(),'Create')]").click()
    time.sleep(5)  # Wait to ensure the process completes

finally:
    # Close the browser
    driver.quit()
