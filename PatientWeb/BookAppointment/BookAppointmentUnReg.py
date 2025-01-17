import sys
sys.path.append("E:/front-end/automation_selenium/")

from PatientWeb.BookAppointment import AppointmentFunctions
from PatientWeb import login
from PatientWeb import SignUpPII
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from faker import Faker

fake = Faker()

userDetails = {
    "first_name": "Aaru",
    "last_name": "S",
    "gender": "Male",
    "dob": "1987-01-01",
    "mobile": "9434549466",
    "email": "xoloyi4956@giratex.com",
    "password": "Ayoo@123"
}

def unreg_user_myself_singleAccount_Claim(driver):
    print("-" * 10 + " Executing Test: Non-Registered: Myself PII Single Account Claim " + "-" * 10)

    try:
        if not AppointmentFunctions.setup_appointment(driver, 'Myself', 'Non-Registered: Myself PII Single Account Claim'):
            return

        if not AppointmentFunctions.fillUserDetails(driver, userDetails, 'Non-Registered: Myself PII Single Account Claim'):
            return

        print("\n" + "=" * 10 + " Test Case 1: Claim Account " + "=" * 10)
        SignUpPII.handlePopupAndActionSingleAcnt(driver, action="claim", user_details=userDetails)
    except Exception as e:
        print("-" * 10 + f" 🥲🥲 Error: {e} 🥲🥲 " + "-" * 10)

def unreg_user_myself_singleAccount_new_user(driver):
    print("-" * 10 + " Executing Test: Non-Registered: Myself PII Single Account - New User " + "-" * 10)

    try:
        if not AppointmentFunctions.setup_appointment(driver, 'My Child', 'Non-Registered: Myself PII Single Account - New User'):
            return

        if not AppointmentFunctions.fillFormBasedOnHeader(driver, "Patient's Information", 'Non-Registered: Myself PII Single Account - New User'):
            return

        if not AppointmentFunctions.fillFormBasedOnHeader(driver, "Caretaker / Account Manager's Information", 'Non-Registered: Myself PII Single Account - New User', userDetails):
            return

        SignUpPII.handlePopupAndActionSingleAcnt(driver, action="new_user", user_details=userDetails)
        time.sleep(2)

        AppointmentFunctions.fillNUmandemail_unreg(driver, "Caretaker / Account Manager's Information", 'Non-Registered: Myself PII Single Account - New User')

        
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
        )
        button.click()

        Account_setup_page = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Account Setup']"))
        )
        if Account_setup_page.is_displayed():
            print("-" * 10 + " Account Setup Page is visible. " + "-" * 10)

    except Exception as e:
        print("-" * 10 + f" 🥲🥲 Error: {e} 🥲🥲 " + "-" * 10)

def unreg_user_myself_singleAccount_signin(driver):
    print("-" * 10 + " Executing Test: Non-Registered: Myself PII Single Account - SignIn " + "-" * 10)

    try:
        if not AppointmentFunctions.setup_appointment(driver, 'Myself', 'Non-Registered: Myself PII Single Account - SignIn'):
            return

        if not AppointmentFunctions.fillUserDetails(driver, userDetails, 'Non-Registered: Myself PII Single Account - SignIn'):
            return

        print("\n" + "=" * 10 + " Test Case 3: Sign In " + "=" * 10)
        SignUpPII.handlePopupAndActionSingleAcnt(driver, action="sign_in", user_details=userDetails)
        time.sleep(1)

        logindetails = {
            "email": "s.kishore123.64@gmail.com",
            "password": "Ayoo@123"
        }

        if not AppointmentFunctions.login_patient(driver, logindetails, 'Non-Registered: Myself PII Single Account - SignIn'):
            print("-" * 10 + " 🥲🥲 Failed to log in patient. Stopping test execution. 🥲🥲 " + "-" * 10)
            return

        if not AppointmentFunctions.checkConfirmationPage(driver, 'AUTOTESTT', 'Non-Registered: Myself PII Single Account - SignIn'):
            print("-" * 10 + " 🥲🥲 Failed to confirm page. Stopping test execution. 🥲🥲 " + "-" * 10)
            return

        time.sleep(1)
    except Exception as e:
        print("-" * 10 + f" 🥲🥲 Error: {e} 🥲🥲 " + "-" * 10)

def unreg_user_myself_MultipleAccountPII(driver):
    user_details = {
        "first_name": "Manivasagam",
        "last_name": "S",
        "gender": "Male",
        "dob": "1998-10-12",
        "mobile": "9566991210",
        "email": "s.kishore123.64@gmail.com",
    }

    print("-" * 10 + " Executing Test: Non-Registered: Myself PII Multiple Account " + "-" * 10)

    try:
        if not AppointmentFunctions.setup_appointment(driver, 'Myself', 'Non-Registered: Myself PII Multiple Account'):
            return

        if not AppointmentFunctions.fillUserDetails(driver, user_details, 'Non-Registered: Myself PII Multiple Account'):
            return

        if not SignUpPII.handlePopupAndActionMultipleAcnt(driver, user_details):
            print("-" * 10 + " 🥲🥲 Failed to display PII Popup. Stopping test execution. 🥲🥲 " + "-" * 10)
            return

        time.sleep(2)
    except Exception as e:
        print("-" * 10 + f" 🥲🥲 Error: {e} 🥲🥲 " + "-" * 10)

def unregUsers():
    # execute_test(unreg_user_myself_singleAccount_Claim)
    execute_test(unreg_user_myself_singleAccount_new_user)
    # execute_test(unreg_user_myself_singleAccount_signin)
    # execute_test(unreg_user_myself_MultipleAccountPII)

def execute_test(test_function):
    driver = webdriver.Chrome()
    try:
        test_function(driver)
    except Exception as e:
        print("-" * 10 + f" 🥲🥲 Error executing {test_function.__name__}: {e} 🥲🥲 " + "-" * 10)
    finally:
        driver.quit()

if __name__ == "__main__":
    unregUsers()
