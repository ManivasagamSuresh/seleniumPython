import sys
sys.path.append("E:/front-end/automation_selenium/")

from PatientWeb.BookAppointment import AppointmentFunctions
from PatientWeb import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variable import PROMO_CODE



# Test case for user already signed in and booking for "Myself"
def signedUserMyself(driver):
    testcase = 'Signed User:Myself'
    if AppointmentFunctions.setup_appointment_signedIn(driver, testcase, 'Myself', 'Virtual'):
        if not AppointmentFunctions.checkConfirmationPage(driver, PROMO_CODE, testcase):
            print('-'*10 + "🥲"*4 + f"Failed to confirm page for {testcase}. Stopping test."  + "🥲"*4 + '-'*10)

# Test case for user already signed in and booking for relative added to his/her account
def signedUserAddedRelative(driver):
    testcase = 'Signed User: Added Relative(Spouse)'
    if AppointmentFunctions.setup_appointment_signedIn(driver, testcase, 'My Spouse', 'Virtual'):
        if not AppointmentFunctions.patientDetailsConfirmationPage(driver, testcase):
            print('-'*10 + "🥲"*4 + f"Failed to confirm patient details for {testcase}. Stopping test."  + "🥲"*4 + '-'*10)
        if not AppointmentFunctions.checkConfirmationPage(driver, PROMO_CODE, testcase):
            print('-'*10 + "🥲"*4 + f"Failed to confirm page for {testcase}. Stopping test."  + "🥲"*4 + '-'*10)

# Test case for user already signed in and booking for new relative
def signedUserNewRelative(driver):
    testcase = 'Signed User: Add New Relative(Parent)'
    if AppointmentFunctions.setup_appointment_signedIn(driver, testcase, 'My Parents', 'Virtual'):
        if not AppointmentFunctions.patientDetailsAddNewRelative(driver, testcase):
            print('-'*10 + "🥲"*4 + f"Failed to add new relative details for {testcase}. Stopping test."  + "🥲"*4 + '-'*10)
        if not AppointmentFunctions.checkConfirmationPage(driver, PROMO_CODE, testcase):
            print('-'*10 + "🥲"*4 + f"Failed to confirm page for {testcase}. Stopping test."  + "🥲"*4 + '-'*10)

# Execute individual test functions
def execute_test(test_function):
    driver = webdriver.Chrome()
    try:
        test_function(driver)
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error executing {test_function.__name__}: {e}"  + "🥲"*4 + '-'*10)
    finally:
        driver.quit()

# Main function to execute all tests
def signedUser():
    execute_test(signedUserMyself)
    execute_test(signedUserAddedRelative)
    execute_test(signedUserNewRelative)

if __name__ == "__main__":
    signedUser()
