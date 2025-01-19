import sys
sys.path.append("E:/front-end/automation_selenium/")

from selenium import webdriver
from PatientWeb.login import test_login
from PatientWeb.signup import mainTest_signup
from PatientWeb.doctorsList import test_dasboardDoctorsList
from PatientWeb.SignUpPII import checkPIISingleAcnt
from PatientWeb.SignUpPII import checkPIIMultipleAcnt
from PatientWeb.BookAppointment.BookAppointmentSignIn import signedUser
from PatientWeb.BookAppointment.BookAppointmentNonSignIn import non_signed_User
from PatientWeb.BookAppointment.BookAppointmentUnReg import unregUsers
from PatientWeb.Policies import callPolicies



def execute_test(test_function):
    """Wrapper to execute a test in a fresh browser session."""
    driver = webdriver.Chrome()
    try:
        test_function(driver)
    except Exception as e:
        print(f"Error executing {test_function.__name__}: {e}")
    finally:
        driver.quit()


def main():
    print("Starting Test Execution...")

    # execute_test(test_dasboardDoctorsList)
    # execute_test(callPolicies)
    # execute_test(test_login)
    execute_test(mainTest_signup)
    # execute_test(checkPIISingleAcnt)
    # execute_test(checkPIIMultipleAcnt)
    signedUser()
    non_signed_User()
    unregUsers()

if __name__ == "__main__":
    main()

    '='*10 + '-'*10 + "🥲"*4 + "🥲"*4 + '-'*10 + '='*10