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
    driver.get("https://uat.ayoo.care/Login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    
    # Input email and password
    driver.find_element(By.XPATH, "//input[@placeholder='Email/Phone number']").send_keys(user_details['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(user_details['password'])
    driver.find_element(By.XPATH, "//button[text()='sign in']").click()

    try:
        # Check for success condition
        WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'caption-box.book-appointment'))
            )
        print("-" * 10 + "Login Test Passed" + "-" * 10)
        return
    except:
        print("-" * 10 + "🥲🥲🥲--Login Test Failed: Unexpected error--🥲🥲🥲" + "-" * 10)
        return

# Example usage
if __name__ == "__main__":
    driver = webdriver.Chrome()  
    try:
        test_login(driver)
    finally:
        driver.quit()  