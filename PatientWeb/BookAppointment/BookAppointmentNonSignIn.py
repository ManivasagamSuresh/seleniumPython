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
from variable import user_details_multiple_login as user_details
from variable import PROMO_CODE


# user_details = {
#         "first_name": "Manivasagam",
#         "last_name": "S",
#         "gender": "Male",
#         "dob": "1998-10-12",
#         "mobile": "9566991210",
#         "email": "s.kishore123.64@gmail.com",
#         "password": "Ayoo@123"
#     }

def non_signedUserMyself(driver):
    print("=" * 10 + " Executing Test: non_signed_User_Myself " + "=" * 10)

    if not AppointmentFunctions.setup_appointment_nonsignedIn(driver, 'Myself', 'Non-Signed User: Myself'):
        return


    if not AppointmentFunctions.select_signin(driver, 'Non-Signed User: Myself'):
        print("-" * 10 + "🥲"*4 +  "Failed to select sign-in option. Stopping test execution." + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.login_patient(driver, user_details, 'Non-Signed User: Myself'):
        print("-" * 10 + "🥲"*4 +  "Failed to log in patient. Stopping test execution. 🥲🥲 " + "🥲"*4 + "-" * 10)
        return

    if not AppointmentFunctions.checkConfirmationPage(driver, PROMO_CODE, 'Non-Signed User: Myself'):
        print("-" * 10 + "🥲"*4 +  " Failed to confirm page. Stopping test execution."  + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)


def non_signedUserAddedRelative(driver):
    print("=" * 10 + " Executing Test: non_signed_User_AddedRelative " + "=" * 10)

    if not AppointmentFunctions.setup_appointment_nonsignedIn(driver, 'My Spouse', 'Non-Signed User: Added_Relative'):
        return
   

    if not AppointmentFunctions.select_signin(driver, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + "🥲"*4 +   "Failed to select sign-in option. Stopping test execution. "  + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.login_patient(driver, user_details, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + "🥲"*4 +  "Failed to log in patient. Stopping test execution. "  + "🥲"*4 + "-" * 10)
        return
    
    if not AppointmentFunctions.patientDetailsConfirmationPage(driver, 'Signed User: Added Relative(Spouse)'):
        print("-" * 10 + "🥲"*4 +   "Failed to confirm patient details. Stopping test execution. "  + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)
    

    if not AppointmentFunctions.checkConfirmationPage(driver, PROMO_CODE, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + "🥲"*4 +   " Failed to confirm page. Stopping test execution."  + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)


def non_signedUser_NewRelative(driver):
    print("=" * 10 +  "Executing Test: non_signed_User_NewRelative " + "=" * 10)

    if not AppointmentFunctions.setup_appointment_nonsignedIn(driver, 'My Spouse', 'Non-Signed User: Added_Relative'):
        return

    if not AppointmentFunctions.select_signin(driver, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + "🥲"*4 +   "Failed to select sign-in option. Stopping test execution. "  + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.login_patient(driver, user_details, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + "🥲"*4 +   "Failed to log in patient. Stopping test execution."  + "🥲"*4 + "-" * 10)
        return
    time.sleep(5)
    
    if not AppointmentFunctions.patientDetailsAddNewRelative(driver, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + "🥲"*4 +   "Failed to add new relative details. Stopping test execution."  + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)
    

    if not AppointmentFunctions.checkConfirmationPage(driver, PROMO_CODE, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + "🥲"*4 +   "Failed to confirm page. Stopping test execution."  + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)





def non_signed_User():
  execute_test(non_signedUserMyself)
  execute_test(non_signedUserAddedRelative)
  execute_test(non_signedUser_NewRelative)
  
    

def execute_test(test_function):
    driver = webdriver.Chrome()
    try:
        test_function(driver)
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error executing {test_function.__name__}: {e}"  + "🥲"*4 + '-'*10)
    finally:
        driver.quit()


if __name__ == "__main__": 
    non_signed_User()
    
   
