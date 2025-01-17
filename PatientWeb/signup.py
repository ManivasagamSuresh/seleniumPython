import sys
sys.path.append("E:/front-end/automation_selenium/")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PatientWeb.BookAppointment import AppointmentFunctions
import time
import random
from faker import Faker

fake = Faker()
MOBILE_EXISTS_MESSAGE = "Phone Number Already in Use"
EMAIL_EXISTS_MESSAGE = "Email Already in Use"

def check_popup(driver, message):
    print("-" * 10 + f" Checking for popup: {message} " + "-" * 10)
    try:
        popup = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'phone-email-used-modal'))
        )
        
       
    
        if popup.is_displayed():
            print("-" * 10 + f" Popup displayed: {message} " + "-" * 10)
            return True
    except Exception as e:
        print("-" * 10 + f" No popup displayed for: {message}, Error: {e} " + "-" * 10)
        return False

def test_signup(driver, num=None, email=None):
    print("-" * 10 + " Executing Test: Sign Up " + "-" * 10)
    driver.get("https://uat.ayoo.care/Login")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Navigate to the signup page
    driver.find_element(By.ID, "loginPage-signup").click()
    print("-" * 10 + " Navigated to signup page " + "-" * 10)
    
    provideUserDetails(driver)

    if num:
        # number_input = driver.find_element(By.ID, "mui-7")
        number_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//label[contains(text(), 'Phone Number')]"))
        )
        
        # Find the input element following the label
        input_field = number_input.find_element(By.XPATH, "following-sibling::div//input")
        
        # Clear the input field and fill in the value
        input_field.clear()
        print("-" * 10 + " Using registered mobile number " + "-" * 10)
        for char in num:
            input_field.send_keys(char)
            time.sleep(0.1) 
       
        if check_popup(driver, MOBILE_EXISTS_MESSAGE):
            print("-" * 10 + " Mobile number already exists. Test Passed. " + "-" * 10)
            return
        else:
            print("-" * 10 + " 🥲🥲🥲 Mobile number already exists. Test Failed 🥲🥲🥲 " + "-" * 10)
            return
    else:
        unique_mobile = AppointmentFunctions.generate_unique_mobile_number()
        AppointmentFunctions.fill_input_by_label(driver, 'Phone Number', unique_mobile)
        print("-" * 10 + f" Generated and entered mobile number: {unique_mobile} " + "-" * 10)

    # Input email
    if email:
        # email_input = driver.find_element(By.ID, "mui-8")
        email_input_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//label[contains(text(), 'Email Id')]"))
        )
        
        # Find the input element following the label
        email_input = email_input_select.find_element(By.XPATH, "following-sibling::div//input")
        
        # Clear the input field and fill in the value
        email_input.clear()
        print("-" * 10 + " Using registered email " + "-" * 10)
        for char in email:
            email_input.send_keys(char)
            time.sleep(0.1) 
       
        if check_popup(driver, EMAIL_EXISTS_MESSAGE):
            print("-" * 10 + " Email already exists. Test Passed. " + "-" * 10)
            return
        else:
            print("-" * 10 + " 🥲🥲🥲 Email already exists. Test Failed 🥲🥲🥲 " + "-" * 10)
            return
    else:
        unique_email = fake.email()
        AppointmentFunctions.fill_input_by_label(driver, 'Email Id', unique_email)
        print("-" * 10 + f" Generated and entered email: {unique_email} " + "-" * 10)

    # Provide password and confirm password
    AppointmentFunctions.fill_input_by_label(driver, 'Password', 'Ayoo@123')
    AppointmentFunctions.fill_input_by_label(driver, 'Confirm Password', 'Ayoo@123')
    

    # Click Sign Up
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    time.sleep(2)

    # Validate OTP Verification page
    try:
        otp_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'OTP Verification')]"))
        )
        if otp_page.is_displayed():
            print("-" * 10 + " SignUp Test Passed " + "-" * 10)
        else:
            print("-" * 10 + " 🥲🥲🥲 SignUp Test Failed 🥲🥲🥲 " + "-" * 10)
    except Exception as e:
        print("-" * 10 + " 🥲🥲🥲 SignUp Test Failed 🥲🥲🥲 " + "-" * 10)
        print("-" * 10 + f" Error: {e} " + "-" * 10)

    time.sleep(2)



def provideUserDetails(driver):
     # Provide first and last name
    random_first_name = fake.first_name()
    random_last_name = fake.last_name()
    print("-" * 10 + f" First name: {random_first_name}, Last name: {random_last_name} " + "-" * 10)
    AppointmentFunctions.fill_input_by_label(driver,'First Name', random_first_name)
    AppointmentFunctions.fill_input_by_label(driver,'Last Name', random_last_name)
    
    # Select Gender
    label = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Gender')]"))
    )

    # Find the input field associated with the label and click on it
    input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Gender')]/following-sibling::div//div[@role='combobox']"))
    )
    input_field.click()
    print('Gender clicked')


    options = driver.find_elements(By.XPATH, "//li[@data-value]") 
    random_option = random.choice(options)
    print("-" * 10 + f" Selected gender option: {random_option.text} " + "-" * 10)
    random_option.click()
    

    # Select date of birth
    date_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Date of Birth']/following::input[@type='text' and @placeholder='YYYY-MM-DD'][1]"))
        )
    date_input.click()
    date_input.send_keys(Keys.CONTROL + "a")
    date_input.send_keys(Keys.DELETE)
    date_input.send_keys("1976-06-17")
    date_input.send_keys(Keys.ENTER)



def mainTest_signup(driver):
    print("-" * 10 + " Running Sign Up Test with unique details... " + "-" * 10)
    test_signup(driver)
    time.sleep(2)
    registered_mobile = "9566991210"
    print("-" * 10 + " Running Sign Up Test with registered mobile number... " + "-" * 10)
    test_signup(driver, num=registered_mobile)
    time.sleep(2)
    registered_email = "s.kishore123.64@gmail.com"
    print("-" * 10 + " Running Sign Up Test with registered email... " + "-" * 10)
    test_signup(driver, email=registered_email)
    

# file usage
if __name__ == "__main__":
    driver = webdriver.Chrome()  
    try:
        mainTest_signup(driver)
    finally:
        driver.quit()
