import sys
sys.path.append("E:/front-end/automation_selenium/")

from PatientWeb.BookAppointment import AppointmentFunctions
from PatientWeb import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


# Test case for user already signed in and booking for "Myself"
def signedUserMyself(driver):
    print("-" * 10 + " Executing Test: signed_User_Myself " + "-" * 10)

    login.test_login(driver)
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "care-type-banner").click()

    if not AppointmentFunctions.selectTypeSignedUser(driver, 'Signed User:Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.selectAppointmentFor(driver, 'Myself', 'Signed User:Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select appointment. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.selectConsultationType(driver, 'Virtual', 'Signed User:Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select consultation type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectRandomSymptom(driver, 'Signed User:Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select random symptom. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.select_time_slot(driver, 'Signed User:Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select time slot. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.checkConfirmationPage(driver, 'AUTOTESTT', 'Signed User:Myself'):
        print("-" * 10 + " 🥲🥲 Failed to confirm page. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

# Test case for user already signed in and booking for relative added to his/her account 
def signedUserAddedRelative(driver):
    print("-" * 10 + " Executing Test: signed_User_Added_Relative " + "-" * 10)

    login.test_login(driver)
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "care-type-banner").click()

    if not AppointmentFunctions.selectTypeSignedUser(driver, 'Signed User: Added Relative(Spouse)'):  # Physical Health
        print("-" * 10 + " 🥲🥲 Failed to select type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.selectAppointmentFor(driver, 'My Spouse', 'Signed User: Added Relative(Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select appointment. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectConsultationType(driver, 'Virtual', 'Signed User: Added Relative(Spouse)'):  # InClinic
        print("-" * 10 + " 🥲🥲 Failed to select consultation type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectRandomSymptom(driver, 'Signed User: Added Relative(Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select random symptom. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.select_time_slot(driver, 'Signed User: Added Relative(Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select time slot. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.patientDetailsConfirmationPage(driver, 'Signed User: Added Relative(Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to confirm patient details. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.checkConfirmationPage(driver, 'AUTOTESTT', 'Signed User: Added Relative(Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to confirm page. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

# Test case for user already signed in and booking for new relative 
def signedUserNewRelative(driver):
    print("-" * 10 + " Executing Test: signed_User_Add_New_Relative " + "-" * 10)

    login.test_login(driver)
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "care-type-banner").click()

    if not AppointmentFunctions.selectTypeSignedUser(driver, 'Signed User: Add New Relative(Parent)'):  # Physical Health
        print("-" * 10 + " 🥲🥲 Failed to select type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.selectAppointmentFor(driver, 'My Parents', 'Signed User: Add New Relative(Parent)'):
        print("-" * 10 + " 🥲🥲 Failed to select appointment. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectConsultationType(driver, 'Virtual', 'Signed User: Add New Relative(Parent)'):  # InClinic
        print("-" * 10 + " 🥲🥲 Failed to select consultation type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectRandomSymptom(driver, 'Signed User: Add New Relative(Parent)'):
        print("-" * 10 + " 🥲🥲 Failed to select random symptom. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.select_time_slot(driver, 'Signed User: Add New Relative(Parent)'):
        print("-" * 10 + " 🥲🥲 Failed to select time slot. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.patientDetailsAddNewRelative(driver, 'Signed User: Add New Relative(Parent)'):
        print("-" * 10 + " 🥲🥲 Failed to add new relative details. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)


    if not AppointmentFunctions.checkConfirmationPage(driver, 'AUTOTESTT', 'Signed User: Add New Relative(Parent)'):
        print("-" * 10 + " 🥲🥲 Failed to confirm page. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)



def signedUser():
    execute_test(signedUserMyself)
    execute_test(signedUserAddedRelative)
    execute_test(signedUserNewRelative)
    
    
    
    
def execute_test(test_function):
    driver = webdriver.Chrome()
    try:
        test_function(driver)
    except Exception as e:
        print(f"Error executing {test_function.__name__}: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    signedUser()

