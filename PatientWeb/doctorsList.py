import sys
sys.path.append("E:/front-end/automation_selenium/")

from selenium.webdriver.common.by import By
from variable import URL

def test_dasboardDoctorsList(driver):
    print('='*10 + "Executing Test: Dashboard Doctors List" + '='*10)
    driver.get(f"{URL}")

    driver.implicitly_wait(20)

    slick_list = driver.find_element(By.CLASS_NAME, "slick-track")

    doctor_elements = slick_list.find_elements(By.CLASS_NAME, "our-doctors-box")

    number_of_doctors = len(doctor_elements)

    if number_of_doctors == 5:
        print( '-'*10 + "Dashboard Doctors List Test Passed"+ '-'*10)
        
    else:
        print( '-'*10 + "🥲"*4 + "Dashboard Doctors List Test Failed" + "🥲"*4 + '-'*10)
        print('-'*10 + "🥲"*4 + f"There are {number_of_doctors} doctors in the list."+ "🥲"*4 + '-'*10)
        return
    
   
