from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_dasboardDoctorsList(driver):
    print("Executing Test: Dashboard Doctors List")
    driver.get("https://uat.ayoo.care/")

    driver.implicitly_wait(10)

    slick_list = driver.find_element(By.CLASS_NAME, "slick-track")

    doctor_elements = slick_list.find_elements(By.CLASS_NAME, "our-doctors-box")

    number_of_doctors = len(doctor_elements)

    if number_of_doctors == 4:
        print("Dashboard Doctors List Test Passed")
        
    else:
        print("-----🥲🥲🥲----------------Dashboard Doctors List Test Failed---------------🥲🥲🥲-----------")
        print(f"There are {number_of_doctors} doctors in the list.")
        return
   
