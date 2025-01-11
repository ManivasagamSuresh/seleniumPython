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
from PatientWeb.login import user_details


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
    print("-" * 10 + " Executing Test: non_signed_User_Myself " + "-" * 10)

    driver.get("https://uat.ayoo.care")
    driver.maximize_window()
    driver.implicitly_wait(10)

    if not AppointmentFunctions.selectTypeUnSignedUser(driver, 'Non-Signed User: Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectAppointmentFor(driver, 'Myself', 'Non-Signed User: Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select appointment. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.selectConsultationType(driver, 'Virtual', 'Non-Signed User: Myself'):  # InClinic
        print("-" * 10 + " 🥲🥲 Failed to select consultation type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectRandomSymptom(driver, 'Non-Signed User: Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select random symptom. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.select_time_slot(driver, 'Non-Signed User: Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select time slot. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.select_signin(driver, 'Non-Signed User: Myself'):
        print("-" * 10 + " 🥲🥲 Failed to select sign-in option. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.login_patient(driver, user_details, 'Non-Signed User: Myself'):
        print("-" * 10 + " 🥲🥲 Failed to log in patient. Stopping test execution. 🥲🥲 " + "-" * 10)
        return

    if not AppointmentFunctions.checkConfirmationPage(driver, 'AUTOTEST', 'Non-Signed User: Myself'):
        print("-" * 10 + " 🥲🥲 Failed to confirm page. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)


def non_signedUserAddedRelative(driver):
    print("-" * 10 + " Executing Test: non_signed_User_AddedRelative " + "-" * 10)

    driver.get("https://uat.ayoo.care")
    driver.maximize_window()
    driver.implicitly_wait(10)

    if not AppointmentFunctions.selectTypeUnSignedUser(driver, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + " 🥲🥲 Failed to select type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectAppointmentFor(driver, 'My Spouse', 'Non-Signed User: Added_Relative'):
        print("-" * 10 + " 🥲🥲 Failed to select appointment. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.selectConsultationType(driver, 'Virtual', 'Non-Signed User: Added_Relative'):  # InClinic
        print("-" * 10 + " 🥲🥲 Failed to select consultation type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectRandomSymptom(driver, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + " 🥲🥲 Failed to select random symptom. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.select_time_slot(driver, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + " 🥲🥲 Failed to select time slot. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.select_signin(driver, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + " 🥲🥲 Failed to select sign-in option. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.login_patient(driver, user_details, 'Non-Signed User: Added_Relative'):
        print("-" * 10 + " 🥲🥲 Failed to log in patient. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    
    if not AppointmentFunctions.patientDetailsConfirmationPage(driver, 'Signed User: Added Relative(Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to confirm patient details. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)
    

    if not AppointmentFunctions.checkConfirmationPage(driver, 'AUTOTEST', 'Non-Signed User: Added_Relative'):
        print("-" * 10 + " 🥲🥲 Failed to confirm page. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)


def non_signedUser_NewRelative(driver):
    print("-" * 10 + " Executing Test: non_signed_User_NewRelative " + "-" * 10)

    driver.get("https://uat.ayoo.care")
    driver.maximize_window()
    driver.implicitly_wait(10)

    if not AppointmentFunctions.selectTypeUnSignedUser(driver, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectAppointmentFor(driver, 'My Spouse', 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select appointment. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.selectConsultationType(driver, 'Virtual', 'Non-Signed User: Add New Relative(My Spouse)'):  # InClinic
        print("-" * 10 + " 🥲🥲 Failed to select consultation type. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.selectRandomSymptom(driver, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select random symptom. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(1)

    if not AppointmentFunctions.select_time_slot(driver, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select time slot. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.select_signin(driver, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to select sign-in option. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)

    if not AppointmentFunctions.login_patient(driver, user_details, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to log in patient. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(5)
    
    if not AppointmentFunctions.patientDetailsAddNewRelative(driver, 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to add new relative details. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)
    
    # if not AppointmentFunctions.patientDetailsConfirmationPage(driver, 'Non-Signed User: Add New Relative(My Spouse)(My Spouse)'):
    #     print("-" * 10 + " 🥲🥲 Failed to confirm patient details. Stopping test execution. 🥲🥲 " + "-" * 10)
    #     return
    # time.sleep(2)
    

    if not AppointmentFunctions.checkConfirmationPage(driver, 'AUTOTEST', 'Non-Signed User: Add New Relative(My Spouse)'):
        print("-" * 10 + " 🥲🥲 Failed to confirm page. Stopping test execution. 🥲🥲 " + "-" * 10)
        return
    time.sleep(2)





def non_signed_User():
#   execute_test(non_signedUserMyself)
#   execute_test(non_signedUserAddedRelative)
  execute_test(non_signedUser_NewRelative)
  
    

def execute_test(test_function):
    driver = webdriver.Chrome()
    try:
        test_function(driver)
    except Exception as e:
        print(f"Error executing {test_function.__name__}: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    driver = webdriver.Chrome()  
    try:
        non_signed_User()
    finally:
        driver.quit()
