import sys
sys.path.append("E:/front-end/automation_selenium/")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import random
import time
from faker import Faker
from PatientWeb.signup import generate_unique_mobile_number

fake = Faker()




def selectTypeSignedUser(driver, testcase):
    try:
        care_options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".care-type-dropdown-lists .mental-heath-btn, .care-type-dropdown-lists .medical-doctor-btn")
            )
        )
        selected_option = random.choice(care_options)  # Randomly select one
        selected_option.click()
        print("---------- Selected care type ----------")
        time.sleep(0.5)
        return True
    except Exception as e:
        print(f"---------- Error in {testcase}: {e} ----------")
        return False

def selectTypeUnSignedUser(driver, testcase):
    try:
        # Wait for the action buttons to be present and collect them
        action_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'appointment-action'))
        )

        # Select a random action button and click it
        random_button = random.choice(action_buttons)
        random_button.click()
        print('-' * 10 + " Randomly clicked on a care type button. " + '-' * 10)
        time.sleep(3)

        # Wait for the appointment list items to be present and collect them
        appointment_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'appointment-list-item'))
        )

        # Select a random appointment list item and click it
        random_appointment = random.choice(appointment_items)
        random_appointment.click()
        print('-' * 10 + " Selected and clicked on a random appointment. " + '-' * 10)
        time.sleep(3)

        return True

    except Exception as e:
        print(f"An error occurred while selecting care type and appointment in {testcase} - {e}")
        return False

# options 
# 1. Myself
# 2. My Spouse
# 3. My Spouse
# 4. My Parents
# 5. Couple/Family
# 6. Other
def selectAppointmentFor(driver, type, testcase):
    try:
        dropdown_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "name-dropdown-lists"))
        )
        option = dropdown_list.find_element(By.XPATH, f".//span[text()='{type}']")
        option.click()
        print(f"---------- Selected '{type}' from the dropdown. ----------")
        return True
    except Exception as e:
        print(f"---------- Error in {testcase} while selecting '{type}': {e} ----------")
        try:
            appointment_banner = driver.find_element(By.CLASS_NAME, "patient-type-banner")
            appointment_banner.click()
            time.sleep(0.5)
            print("---------- Clicked on 'Appointment for'. ----------")
            dropdown_list = driver.find_element(By.CLASS_NAME, "name-dropdown-lists")
            option = dropdown_list.find_element(By.XPATH, f".//span[text()='{type}']")
            option.click()
            print(f"---------- Selected '{type}' after opening 'Appointment for'. ----------")
            return True
        except Exception as inner_e:
            print(f"---------- Failed to select '{type}' in retry for {testcase}: {inner_e} ----------")
            return False

def selectConsultationType(driver, consultation_type, testcase):
    try:
        dropdown_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-type-dropdown"))
        )
        option = dropdown_list.find_element(By.XPATH, f".//div[@id='{consultation_type}']")
        option.click()
        print(f"---------- Selected '{consultation_type}' from the dropdown. ----------")
        return True
    except Exception as e:
        print(f"---------- Error in {testcase} while selecting '{consultation_type}': {e} ----------")
        try:
            consultation_banner = driver.find_element(By.CLASS_NAME, "search-type-banner")
            consultation_banner.click()
            time.sleep(0.5)
            print("---------- Clicked on 'Consultation Type'. ----------")
            dropdown_list = driver.find_element(By.CLASS_NAME, "search-type-dropdown")
            option = dropdown_list.find_element(By.XPATH, f".//div[@id='{consultation_type}']")
            option.click()
            print(f"---------- Selected '{consultation_type}' after opening 'Consultation Type'. ----------")
            return True
        except Exception as inner_e:
            print(f"---------- Failed to select '{consultation_type}' in retry for {testcase}: {inner_e} ----------")
            return False

def selectRandomSymptom(driver, testcase):
    retries = 3
    for attempt in range(retries):
        try:
            dropdown_list = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "symptoms-dropdown-list-col"))
            )
            if dropdown_list:
                selected_option = random.choice(dropdown_list)
                selected_text = selected_option.text
                selected_option.click()
                print(f"---------- Selected random symptom: {selected_text} ----------")
                return True
            else:
                print("---------- No symptoms found in the dropdown. ----------")
                return False
        except Exception as e:
            print(f"---------- Attempt {attempt + 1} failed with error in {testcase}: {e} ----------")
            time.sleep(1)

    print(f"---------- Failed to select a symptom after multiple attempts for {testcase}. ----------")
    return False


def select_time_slot(driver, testcase):
    retries = 3
    for attempt in range(retries):
        try:
            first_outer_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".outer-box"))
            )
            time_slots = WebDriverWait(first_outer_box, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 
                    ".apppointment-time-lists-col.mental, .apppointment-time-lists-col.medical"))
            )

            if time_slots:
                random_slot = random.choice(time_slots)
                slot_text = random_slot.text.strip()
                ActionChains(driver).move_to_element(random_slot).click().perform()
                print(f"---------- Selected time slot: {slot_text} ----------")
                return True
            else:
                print("---------- No available time slots found. ----------")
                return False
        except Exception as e:
            print(f"---------- Attempt {attempt + 1} failed with error in {testcase}: {e} ----------")
            time.sleep(1)

    print(f"---------- Failed to select a time slot after multiple attempts for {testcase}. ----------")
    return False

def select_signin(driver, testcase):
    try:
        element_selector = ".userData-form"

        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            is_visible = element.is_displayed()
        except NoSuchElementException:
            print(f"🥲🥲🥲🥲----------\nError in {testcase}: User details Page not found! 🥲🥲🥲🥲\n----------")
            return False

        if is_visible:
            print(f"----------\nElement 'User details Page' is visible in {testcase}! ✅\n----------")
            try:
                signin_button = driver.find_element(By.XPATH, "//span[normalize-space()='Sign in']")
                signin_button.click()
                print(f"----------\nSuccessfully clicked the 'Sign-In' button in {testcase}! ✅\n----------")
                return True
            except NoSuchElementException:
                print(f"🥲🥲🥲🥲----------\nError in {testcase}: 'Sign-In' button with text 'Next' not found! 🥲🥲🥲🥲\n----------")
                return False
            except Exception as e:
                print(f"🥲🥲🥲🥲----------\nError in {testcase}: 'Sign-In' button is not interactable! {str(e)} 🥲🥲🥲🥲\n----------")
                return False
        else:
            print(f"🥲🥲🥲🥲----------\nError in {testcase}: User details Page is not visible! 🥲🥲🥲🥲\n----------")
            return False

    except Exception as e:
        print(f"🥲🥲🥲🥲----------\nError in {testcase}: {str(e)} 🥲🥲🥲🥲\n----------")
        return False

def patientDetailsConfirmationPage(driver, testcase):
    print(f"----------\nRunning Testcase: {testcase}\n----------")
    try:
        element_selector = ".userData-form"

        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            is_visible = element.is_displayed()
        except NoSuchElementException:
            print(f"🥲🥲🥲🥲----------\nError in {testcase}: User details Page not found! 🥲🥲🥲🥲\n----------")
            return False

        if is_visible:
            print(f"----------\nElement 'User details Page' is visible in {testcase}! ✅\n----------")
            try:
                next_button = driver.find_element(By.XPATH, "//button[normalize-space()='Next']")
                next_button.click()
                print(f"----------\nSuccessfully clicked the 'Next' button in {testcase}! ✅\n----------")
                return True
            except NoSuchElementException:
                print(f"🥲🥲🥲🥲----------\nError in {testcase}: 'Next' button with text 'Next' not found! 🥲🥲🥲🥲\n----------")
                return False
            except Exception as e:
                print(f"🥲🥲🥲🥲----------\nError in {testcase}: 'Next' button is not interactable! {str(e)} 🥲🥲🥲🥲\n----------")
                return False
        else:
            print(f"🥲🥲🥲🥲----------\nError in {testcase}: User details Page is not visible! 🥲🥲🥲🥲\n----------")
            return False

    except Exception as e:
        print(f"🥲🥲🥲🥲----------\nError in {testcase}: {str(e)} 🥲🥲🥲🥲\n----------")
        return False

def patientDetailsAddNewRelative(driver, testcase):
    print(f"----------\nRunning Testcase: {testcase}\n----------")
    try:
        element_selector = ".userData-form"

        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            is_visible = element.is_displayed()
        except NoSuchElementException:
            print(f"🥲🥲🥲🥲----------\nError in {testcase}: User details Page not found! 🥲🥲🥲🥲\n----------")
            return False

        if is_visible:
            print(f"----------\nElement 'User details Page' is visible in {testcase}! ✅\n----------")
            try:
                wait = WebDriverWait(driver, 10)
                combobox = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='combobox']"))
                )
                combobox.click()
                print("✅ Successfully clicked the combobox.")
                
                add_new_item = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//li[text()='Add New']"))
                )
                add_new_item.click()
                print("✅ Successfully clicked 'Add New' from the dropdown.")
                time.sleep(1)

                if testcase == "Non-Signed User: Add New Relative(My Spouse)":
                    if not replace_spouse(driver, testcase):
                        print(f"🥲🥲🥲🥲----------\nError in {testcase}: Unable to Replace Spouse. Stopping test case. 🥲🥲🥲🥲\n----------")
                        return False
                    time.sleep(3)

                details_fill = fillPatientDetails(driver, testcase)
                if details_fill:
                    driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
                    return True
                else:
                    return False
            except NoSuchElementException:
                print(f"🥲🥲🥲🥲----------\nError in {testcase}: SVG element not found! 🥲🥲🥲🥲\n----------")
                return False
            except Exception as e:
                print(f"🥲🥲🥲🥲----------\nError in {testcase}: Unable to interact with the SVG element - {str(e)} 🥲🥲🥲🥲\n----------")
                return False
        else:
            print(f"🥲🥲🥲🥲----------\nError in {testcase}: User details Page is not visible! 🥲🥲🥲🥲\n----------")
            return False

    except Exception as e:
        print(f"🥲🥲🥲🥲----------\nError in {testcase}: {str(e)} 🥲🥲🥲🥲\n----------")
        return False

def replace_spouse(driver, testcase):
    try:
        # Wait for the modal to appear
        modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-body"))
        )
        
        # Check if the modal is displayed
        if modal.is_displayed():
            print('-' * 10 + f" Replace Spouse Modal displayed for testcase: {testcase} " + '-' * 10)
            
            # Click "Yes" button
            yes_button = modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f".//button[text()='Yes']"))
             )
        
            # yes_button = modal.find_element(By.XPATH, f".//button[text()='Yes']")
            yes_button.click()
            
            print('-' * 10 + " Successfully clicked 'Yes' to replace spouse. " + '-' * 10)
            return True
        else:
            print(f"-----🥲🥲🥲🥲 Replace Spouse Modal not displayed for testcase: {testcase} 🥲🥲🥲🥲-----")
            return False
    except Exception as e:
        print(f"-----🥲🥲🥲 Error in replace_spouse during {testcase}: {e} 🥲🥲🥲-----")
        return False   

def fillPatientDetails(driver, testcase):
    try:
        unique_email = fake.email()
        random_first_name = fake.first_name()
        random_last_name = fake.last_name()
        unique_mob = generate_unique_mobile_number()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'patinet-firstname'))
        ).send_keys(random_first_name)

        last_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Last Name']/following::input[@type='text' and @required][1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", last_name_field)
        last_name_field.send_keys(random_last_name)

        gender_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='Gender-select' and @aria-labelledby='Gender-label Gender-select']"))
        )
        gender_dropdown.click()

        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[@data-value]"))
        )
        random.choice(options).click()

        dob_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Date of Birth']/following::input[@type='text' and @placeholder='YYYY-MM-DD'][1]"))
        )
        dob_field.click()
        dob_field.send_keys(Keys.CONTROL + "a")
        dob_field.send_keys(Keys.DELETE)
        dob_field.send_keys("1986-06-17")
        dob_field.send_keys(Keys.ENTER)
        time.sleep(1)

        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'country-code')]//div[contains(@class, 'MuiSelect-select')]"))
        )
        dropdown.click()
        print("✅ Successfully opened the country code dropdown.")
        time.sleep(1)

        # Select the +91 option
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@data-value='+91' and text()='+91 IN']"))
        )
        option.click()
        print("✅ Successfully selected '+91 IN' from the list.")

        phone_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Phone Number']/following::input[@type='text'][1]"))
        )
        phone_field.send_keys(unique_mob)
        time.sleep(1)

        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Email Id']/following::input[@type='text'][1]"))
        )
        email_field.send_keys(unique_email)
        time.sleep(5)
        print(f"---------- Patient details filled successfully for :{testcase}. ----------")
        return True

    except TimeoutException as e:
        print(f"----------🥲🥲🥲🥲 Timeout occurred while executing test case: {testcase} during Fill patient details  {e} 🥲🥲🥲🥲----------")
        return False
    except NoSuchElementException as e:
        print(f"----------🥲🥲🥲🥲 Element not found for {testcase} during Fill patient details: {e} 🥲🥲🥲🥲----------")
        return False
    except Exception as e:
        print(f"----------🥲🥲🥲🥲 An unexpected error occurred while performing case- {testcase} during Fill patient details: {e} 🥲🥲🥲🥲----------")
        return False

def checkConfirmationPage(driver, promo_code, testcase):
    try:
        action_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".action-section"))
        )
        paragraph = action_section.find_element(By.TAG_NAME, "p")
        action_section_text = paragraph.text.strip().replace("\n", " ")
        print(action_section_text)

        required_text = "By confirming the appointment you consent to abide by Ayoo’s Terms & Conditions"

        if required_text == action_section_text:
            print("---------- Confirmation Page is displayed. Proceeding to apply promo code. ----------")

            promo_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "applyPromoCode"))
            )
            promo_input.clear()
            promo_input.send_keys(promo_code)

            promo_button = driver.find_element(By.CLASS_NAME, "promo-code-apply")
            promo_button.click()

            try:
                invalid_promo = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid')]")
                ))
                print(f"---------- Invalid Promo Code in {testcase}. Test failed. ----------")
                return False
            except TimeoutException:
                print("---------- Valid Promo Code applied. Proceeding. ----------")

            confirm_button = driver.find_element(By.ID, "confirmAppointment")
            confirm_button.click()

            confirmation_page = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.ID, "appointment-confirmation"))
            )
            if confirmation_page.is_displayed():
                print("-" * 10 + f" Appointment Booked Successfully for {testcase} " + "-" * 10)
                return True
            else:
                print(f"---------- Confirmation page not displayed in {testcase}. Test failed. ----------")
                return False
        else:
            print(f"---------- Confirmation page not displayed in {testcase}. Test failed. ----------")
            return False
    except TimeoutException as e:
        print(f"---------- Timeout occurred in {testcase}: {e} ----------")
        return False
    except NoSuchElementException as e:
        print(f"---------- Element not found in {testcase}: {e} ----------")
        return False
    except Exception as e:
        print(f"---------- An unexpected error occurred in {testcase}: {e} ----------")
        return False

def login_patient(driver, userdetails, testcase):
    try:
        print(userdetails)
        driver.find_element(By.ID, "Email").send_keys(userdetails["email"])
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(userdetails["password"])
        driver.find_element(By.XPATH, "//button[text()='sign in']").click()
        print(f"---------- Login successful for {testcase}. ----------")
        time.sleep(5)
        return True
    except TimeoutException as e:
        print(f"---------- Timeout during login in {testcase}: {e} ----------")
        return False
    except NoSuchElementException as e:
        print(f"---------- Element not found during login in {testcase}: {e} ----------")
        return False
    except Exception as e:
        print(f"---------- An unexpected error occurred during login in {testcase}: {e} ----------")
        return False



