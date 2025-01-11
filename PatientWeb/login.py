from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_details = {
        "first_name": "Manivasagam",
        "last_name": "S",
        "gender": "Male",
        "dob": "1998-10-12",
        "mobile": "9566991210",
        "email": "s.kishore123.64@gmail.com",
        "password": "Ayoo@123"
    }

def test_login(driver):
    print("-" * 10 + "Executing Test: Login"+ "-" * 10)
    driver.get("https://uat.ayoo.care/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    
    # Input email and password
    driver.find_element(By.ID, "Email").send_keys(user_details['email'])
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(user_details['password'])
    driver.find_element(By.XPATH, "//button[text()='sign in']").click()

    try:
        # Check for success condition
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'main-banner'))
        )
        print("-" * 10 + "Login Test Passed" + "-" * 10)
    except:
        try:
            # Check for failure condition
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//span[text()="Email, phone number or password incorrect."]'))
            )
            print("-" * 10 + "Cannot login: Email, phone number or password incorrect." + "-" * 10)
        except Exception as e:
            print("-" * 10 + "🥲🥲🥲--Login Test Failed: Unexpected error--🥲🥲🥲" + "-" * 10)

# Example usage
if __name__ == "__main__":
    driver = webdriver.Chrome()  
    try:
        test_login(driver)
    finally:
        driver.quit()  