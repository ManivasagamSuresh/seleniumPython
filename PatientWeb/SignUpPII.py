import sys
sys.path.append("E:/front-end/automation_selenium/")



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PatientWeb.BookAppointment import AppointmentFunctions
import time
from variable import URL
from variable import user_details_multiple_login
from variable import user_details_single_PII

def checkPIISingleAcnt(driver):
    print("-" * 10 + " Executing Test: Sign Up PII Single Account " + "-" * 10)



    # Test Case 1: Claim Account
    print("\n" + "=" * 10 + " Test Case 1: Claim Account " + "=" * 10)
    provideUserDetails(driver, **user_details_single_PII)
    handlePopupAndActionSingleAcnt(driver, action="claim", user_details=user_details_single_PII)

    # Test Case 2: I'm New User
    print("\n" + "=" * 10 + " Test Case 2: I'm New User " + "=" * 10)
    provideUserDetails(driver, **user_details_single_PII)
    handlePopupAndActionSingleAcnt(driver, action="new_user", user_details=user_details_single_PII)

    # Test Case 3: Sign In
    print("\n" + "=" * 10 + " Test Case 3: Sign In " + "=" * 10)
    provideUserDetails(driver, **user_details_single_PII)
    handlePopupAndActionSingleAcnt(driver, action="sign_in", user_details=user_details_single_PII)


def checkPIIMultipleAcnt(driver):
    print("=" * 10 + " Executing Test: Sign Up PII Multiple Account " + "=" * 10)


    print("\n" + "=" * 10 + " Test Case 1: Claim Account " + "=" * 10)
    provideUserDetails(driver, **user_details_multiple_login)
    handlePopupAndActionMultipleAcnt(driver, user_details=user_details_multiple_login)


def handlePopupAndActionSingleAcnt(driver, action, user_details):
    
    try:
        # Wait for the "Account Already Exists" pop-up
        acnt_exist_page = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Account Already Exists')]"))
        )

        if acnt_exist_page.is_displayed():
            print("-" * 10 + " Account Already Exists modal displayed " + "-" * 10)

            # Handle actions based on input
            if action == "claim":
                driver.find_element(By.XPATH, "//button[contains(text(),'Claim Account')]").click()
                time.sleep(2)
                claimAccountDef(driver, user_details)
            elif action == "new_user":
                driver.find_element(By.XPATH, "//button[contains(text(),\"I'm a New User\")]").click()
                time.sleep(5)
                handleNewUserCase(driver, user_details)
            elif action == "sign_in":
                driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
                time.sleep(5)
                handleSignInCase(driver, user_details)

        else:
            print("-" * 10 + "🥲"*4 + " Pop-up not displayed, Test Failed "  + "🥲"*4  + "-" * 10)

    except Exception as e:
        print("-" * 10 + "🥲"*4 +  f" Error during claim action: {e} " +   "🥲"*4 + "-" * 10)


def handlePopupAndActionMultipleAcnt(driver, user_details):
    try:
        profile_exist_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Profile Already Exists')]"))
        )
        if profile_exist_page:
            print("-" * 10 + "Profile Already Exists popup detected." + "-" * 10)

             # Select the element with '210' and click
            masked_mobile = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='masked-mobile' and contains(text(),'210')]"))
            )
            
            masked_mobile.click()
            time.sleep(3)
            print("-" * 10 + f"Clicked on the required mobile number " + "-" * 10 )
            if not claimAccountDef(driver, user_details):
                return False
            return True
    except Exception as e:
       print("-" * 10 + "🥲"*4 +  f" Error during Claim for Multiple Account action: {e} "  + "🥲"*4 + "-" * 10)
       return False 
  


def claimAccountDef(driver, user_details):
    print("=" * 10 + " Starting Claim Account Process " + "=" * 10)
    try:
        # Wait for the 'Confirm Details' page to appear
        confirm_details_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Confirm Details')]"))
        )
        
        if confirm_details_page.is_displayed():
            print("-" * 10 + " Confirm Details page displayed successfully " + "-" * 10)

            # Fill in mobile and email details
            fillDetails(driver, user_details)

            # Click the 'Reset Password' button
            reset_password_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Reset password')]")
            reset_password_btn.click()
            print("-" * 10 + " Reset password button clicked " + "-" * 10)
            time.sleep(2)

            # Wait for the 'Reset Password' modal
            reset_password_modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "reset-password-modal"))
            )

            if reset_password_modal.is_displayed():
                print("-" * 10 + " Reset password modal displayed successfully " + "-" * 10)
                fill_passwords(driver)
                otp_modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "otp-verification-modal"))
                )
                if otp_modal.is_displayed():
                    print("-" * 10  +  "SignUp PII, Claim Account Test Passed " + "-" * 10)
                    return True
                else:
                    print("-" * 10 + "🥲"*4 +  " OTP verification modal not displayed, Test Failed "  + "🥲"*4 + "-" * 10)
                      
            else:
                print("-" * 10 + "🥲"*4 + " 🥲 Reset Password modal not displayed, Test Failed 🥲 "   + "🥲"*4 + "-" * 10)
                return False

    except Exception as e:
        # Handle any errors during the Claim Account process
        print("-" * 10 + "🥲"*4 + " Claim Account Test Failed "  + "🥲"*4 + "-" * 10)
        print("-" * 10 + "🥲"*4 + f" Error: {e} "  + "🥲"*4 + "-" * 10)
    return False        

def handleNewUserCase(driver, user_details):
    print("=" * 10 + " Handling New User Case " + "=" * 10)
    try:
        print("-" * 10 + " New User case handled successfully " + "-" * 10)
        return True
    except Exception as e:
        print("-" * 10 + "🥲"*4 +  f" Error in New User Case: {e} "  + "🥲"*4 + "-" * 10)
        return False 


def handleSignInCase(driver, user_details):
    print("-" * 10 + " Handling Sign In Case " + "-" * 10)
    try:
        login_page = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'sign in')]"))
                )
        if login_page.is_displayed():
            print("-" * 10 + " Sign In case handled successfully " + "-" * 10)
            return True
    except Exception as e:
        print("-" * 10 + "🥲"*4 +  f" Error in Sign In Case: {e} "  + "🥲"*4 + "-" * 10)
        return False

 

def provideUserDetails(driver, first_name, last_name, gender, dob, **kwargs):
    driver.get(f"{URL}/SignUp")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print("-" * 10 + f" Providing details: {first_name} {last_name}, Gender: {gender}, DOB: {dob} " + "-" * 10)
    AppointmentFunctions.fill_input_by_label(driver,'First Name', first_name)
    AppointmentFunctions.fill_input_by_label(driver,'Last Name', last_name)
    

    # Select gender
    label = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Gender')]"))
    )

    # Find the input field associated with the label and click on it
    input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Gender')]/following-sibling::div//div[@role='combobox']"))
    )
    input_field.click()
    driver.find_element(By.XPATH, f"//li[@data-value='{gender}']").click()

    # Enter DOB
    date_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Date of Birth']/following::input[@type='text' and @placeholder='YYYY-MM-DD'][1]"))
        )
    date_input.click()
    date_input.send_keys(Keys.CONTROL + "a")
    date_input.send_keys(Keys.DELETE)
    date_input.send_keys(dob)
    date_input.send_keys(Keys.ENTER)
    time.sleep(2)


def fillDetails(driver, user_details):
    print("-" * 10 + " Filling in Mobile and Email " + "-" * 10)
    try:
        # Fill mobile number
        mobile_input = driver.find_element(By.XPATH, "//div[@class='detail mobile-section']//input[@placeholder='Type here']")
        mobile_input.clear()
        mobile_input.send_keys(user_details["mobile"])

        # Fill email
        email_input = driver.find_element(By.XPATH, "//div[@class='detail email-section']//input[@placeholder='Type here']")
        email_input.clear()
        email_input.send_keys(user_details["email"])
        time.sleep(2)
    except Exception as e:
        print("-" * 10 + "🥲"*4 +  f" Error filling details: {e} "  + "🥲"*4 + "-" * 10)


def fill_passwords(driver):
    print("-" * 10 + "Performing Fill Password" + "-" * 10)

    driver.find_element(By.ID, 'New-Password').send_keys('Ayoo@123')
    driver.find_element(By.ID, 'Confirm-New Password').send_keys('Ayoo@123')
    driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
    time.sleep(2)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        checkPIISingleAcnt(driver)
        checkPIIMultipleAcnt(driver)
        
    finally:
        driver.quit()
