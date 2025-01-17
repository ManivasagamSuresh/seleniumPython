import sys
sys.path.append("E:/front-end/automation_selenium/")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from PatientWeb import login
import random
import time
from faker import Faker
from variable import URL


fake = Faker()


def generate_unique_mobile_number():
    first_digit = random.randint(6, 9)  
    remaining_digits = random.randint(10**8, 10**9 - 1)
    return f"{first_digit}{remaining_digits}"



def selectTypeSignedUser(driver, testcase):
    try:
        care_options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".care-type-dropdown-lists .mental-heath-btn, .care-type-dropdown-lists .medical-doctor-btn")
            )
        )
        selected_option = random.choice(care_options)  # Randomly select one
        selected_option.click()
        print('-'*10 + "Selected care type" + '-'*10) 
        time.sleep(0.5)
        return True
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error in {testcase}: {e}"  + "🥲"*4 + '-'*10)
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
        print('-'*10 + "🥲"*4 + f"An error occurred while selecting care type and appointment in {testcase} - {e}" + "🥲"*4 + '-'*10)
        return False
 
# options 
# 1. Myself
# 2. My Child
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
        print('-'*10 + f"Selected '{type}' from the dropdown." + '-'*10)
        return True
    except Exception as e:
        print( '-'*10 + "🥲"*4 + f"Error in {testcase} while selecting '{type}': {e}"  + "🥲"*4 + '-'*10)
        try:
            appointment_banner = driver.find_element(By.CLASS_NAME, "patient-type-banner")
            appointment_banner.click()
            time.sleep(0.5)
            print('-'*10 + "Clicked on 'Appointment for'."  + '-'*10)
            dropdown_list = driver.find_element(By.CLASS_NAME, "name-dropdown-lists")
            option = dropdown_list.find_element(By.XPATH, f".//span[text()='{type}']")
            option.click()
            print('-'*10 + f"Selected '{type}' after opening 'Appointment for'." + '-'*10)
            return True
        except Exception as inner_e:
            print('-'*10 + "🥲"*4 + f"Failed to select '{type}' in retry for {testcase}: {inner_e}"  + "🥲"*4 + '-'*10)
            return False

def selectConsultationType(driver, consultation_type, testcase):
    try:
        dropdown_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-type-dropdown"))
        )
        option = dropdown_list.find_element(By.XPATH, f".//div[@id='{consultation_type}']")
        option.click()
        print('-'*10 + f"Selected '{consultation_type}' from the dropdown. " + '-'*10)
        return True
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error in {testcase} while selecting '{consultation_type}': {e}" + "🥲"*4 + '-'*10)
        try:
            consultation_banner = driver.find_element(By.CLASS_NAME, "search-type-banner")
            consultation_banner.click()
            time.sleep(0.5)
            print('-'*10 + " Clicked on 'Consultation Type'. " + '-'*10)
            dropdown_list = driver.find_element(By.CLASS_NAME, "search-type-dropdown")
            option = dropdown_list.find_element(By.XPATH, f".//div[@id='{consultation_type}']")
            option.click()
            print('-'*10 + f" Selected '{consultation_type}' after opening 'Consultation Type'." + '-'*10)
            return True
        except Exception as inner_e:
            print( '-'*10 + f" Failed to select '{consultation_type}' in retry for {testcase}: {inner_e}"  + '-'*10)
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
                print('-'*10 + f"Selected random symptom: {selected_text} "  '-'*10)
                return True
           
            else:
                print('-'*10 + "🥲"*4 + "No symptoms found in the dropdown. " + "🥲"*4 + '-'*10)
                return False
        except Exception as e:
            print('-'*10 + "🥲"*4 + f"Attempt {attempt + 1} failed with error in {testcase}: {e}"  + "🥲"*4 + '-'*10)
            time.sleep(1)
 
    print('-'*10 + "🥲"*4 + f"Failed to select a symptom after multiple attempts for {testcase}." + "🥲"*4 + '-'*10)
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
                print('-'*10 + f"Selected time slot: {slot_text} " + '-'*10)
                return True
            else:
                print('-'*10 + "No available time slots found." + '-'*10)
                return False
        except Exception as e:
            print('-'*10 + "🥲"*4 + f"Attempt {attempt + 1} failed with error in {testcase}: {e}" + "🥲"*4 + '-'*10)
            time.sleep(1)

    print('-'*10 + "🥲"*4 + f"Failed to select a time slot after multiple attempts for {testcase}. " + "🥲"*4 + '-'*10)
    return False

def select_signin(driver, testcase):
    try:
        element_selector = ".userData-form"

        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            is_visible = element.is_displayed()
        except NoSuchElementException:
            print('-'*10 + "🥲"*4 + f"Error in {testcase}: User details Page not found" + "🥲"*4 + '-'*10)
            return False

        if is_visible:
            print('-'*10 + f"Element 'User details Page' is visible in {testcase}! " + '-'*10)
            try:
                signin_button = driver.find_element(By.XPATH, "//span[normalize-space()='Sign in']")
                signin_button.click()
                print('-'*10 + f"Successfully clicked the 'Sign-In' button in {testcase}! "  + '-'*10)
                return True
            except NoSuchElementException:
                print('-'*10 + "🥲"*4 + f"Error in {testcase}: 'Sign-In' button with text 'Next' not found!" + "🥲"*4 + '-'*10)
                return False
            except Exception as e:
                print('-'*10 + "🥲"*4 + f"Error in {testcase}: 'Sign-In' button is not interactable! {str(e)}" + "🥲"*4 + '-'*10)
                return False
        else:
            print('-'*10 + "🥲"*4 + f"Error in {testcase}: User details Page is not visible!" + "🥲"*4 + '-'*10)
            return False

    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error in {testcase}: {str(e)}" + "🥲"*4 + '-'*10)
        return False

def patientDetailsConfirmationPage(driver, testcase):
    print('-'*10 + f"Running Testcase: {testcase}" + '-'*10)
    try:
        element_selector = ".userData-form"

        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            is_visible = element.is_displayed()
        except NoSuchElementException:
            print('-'*10 + "🥲"*4 + f"Error in {testcase}: User details Page not found!" + "🥲"*4 + '-'*10)
            return False

        if is_visible:
            print('-'*10 + f"Element 'User details Page' is visible in {testcase}! " + '-'*10)
            time.sleep(5)
            try:
                next_button = driver.find_element(By.XPATH, "//button[normalize-space()='Next']")
                next_button.click()
                print( '-'*10 + f"Successfully clicked the 'Next' button in {testcase}! "  + '-'*10)   
                return True
            except NoSuchElementException:
                print('-'*10 + "🥲"*4 + f"Error in {testcase}: 'Next' button with text 'Next' not found!" + "🥲"*4 + '-'*10)
                return False
            except Exception as e:
                print('-'*10 + "🥲"*4 + f"Error in {testcase}: 'Next' button is not interactable! {str(e)}" + "🥲"*4 + '-'*10)
                return False
        else:
            print('-'*10 + "🥲"*4 + f"Error in {testcase}: User details Page is not visible! " + "🥲"*4 + '-'*10)
            return False

    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error in {testcase}: {str(e)} " + "🥲"*4 + '-'*10)
        return False

def patientDetailsAddNewRelative(driver, testcase):  
    print('-'*10 + f"Running Testcase: {testcase}" + '-'*10)
    try:
        element_selector = ".userData-form"

        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            is_visible = element.is_displayed()
        except NoSuchElementException:
            print('-'*10 + "🥲"*4 + f"Error in {testcase}: User details Page not found!" + "🥲"*4 + '-'*10)
            return False

        if is_visible:
            print('-'*10 + f"Element 'User details Page' is visible in {testcase}! " + '-'*10)
            try:
                wait = WebDriverWait(driver, 10)
                combobox = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='combobox']"))
                )
                combobox.click()
                print('-'*10 + "Successfully clicked the combobox." + '-'*10)
                
                add_new_item = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//li[text()='Add New']"))
                )
                add_new_item.click()
                print('-'*10 + "Successfully clicked 'Add New' from the dropdown." + '-'*10)
                time.sleep(1)

                if testcase == "Non-Signed User: Add New Relative(My Spouse)":
                    if not replace_spouse(driver, testcase):
                        print('-'*10 + "🥲"*4 + f"Error in {testcase}: Unable to Replace Spouse. Stopping test case." + "🥲"*4 + '-'*10)
                        return False
                    time.sleep(3)

                details_fill = fillPatientDetails(driver, testcase)
                if details_fill:
                    driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
                    return True
                else:
                    return False 
            except NoSuchElementException:
                print('-'*10 + "🥲"*4 + f"Error in {testcase}: SVG element not found!"+ "🥲"*4 + '-'*10)
                return False
            except Exception as e:
                print('-'*10 + "🥲"*4 + f"Error in {testcase}: Unable to interact with the SVG element - {str(e)}"+ "🥲"*4 + '-'*10 )
                return False
        else:
            print('-'*10 + "🥲"*4 + f"Error in {testcase}: User details Page is not visible! " + "🥲"*4 + '-'*10)
            return False

    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error in {testcase}: {str(e)} " + "🥲"*4 + '-'*10)
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
            print('-'*10 + "🥲"*4 + f"Replace Spouse Modal not displayed for testcase: {testcase}"+ "🥲"*4 + '-'*10)
            return False
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error in replace_spouse during {testcase}: {e}"+ "🥲"*4 + '-'*10)
        return False   

def fillPatientDetails(driver, testcase):
    try:
        unique_email = fake.email()
        random_first_name = fake.first_name()
        random_last_name = fake.last_name()
        unique_mob = generate_unique_mobile_number()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'First-Name'))
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
        print('-'*10 + "Successfully opened the country code dropdown."+ '-'*10)
        time.sleep(1)

        # Select the +91 option
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@data-value='+91' and text()='+91 IN']"))
        )
        option.click()
        print('-'*10 + "Successfully selected '+91 IN' from the list."+ '-'*10)

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
        print('-'*10 + f"Patient details filled successfully for :{testcase}."+ '-'*10)
        return True

    except TimeoutException as e:
        print('-'*10 + "🥲"*4 + f"Timeout occurred while executing test case: {testcase} during Fill patient details  {e}"+ "🥲"*4 + '-'*10)
        return False
    except NoSuchElementException as e:
        print('-'*10 + "🥲"*4 + f"Element not found for {testcase} during Fill patient details: {e}"+ "🥲"*4 + '-'*10)
        return False
    except Exception as e:
        print('-'*10 + "🥲"*4 + f" An unexpected error occurred while performing case- {testcase} during Fill patient details: {e} "+ "🥲"*4 + '-'*10)
        return False


def fillUserDetails(driver, userDetails, testcase):
    try:  
        # Fill First Name
        print('-'*10 + "- Filling First Name" + '-'*10)
        fill_input_by_label(driver, 'First Name', userDetails.get('first_name', ''))
        time.sleep(1)

        # Fill Last Name
        print('-'*10 + " Filling Last Name" + '-'*10)
        fill_input_by_label(driver, 'Last Name', userDetails.get('last_name', ''))
        time.sleep(1)

        # Select Gender
        print('-'*10 + "Selecting Gender" + '-'*10)
        gender_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='Gender-select']"))
        )
        gender_dropdown.click()

        gender = userDetails.get('gender', '').strip()
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[@data-value]"))
        )
        matched_option = next((option for option in options if option.text.strip().lower() == gender.lower()), None)

        if matched_option:
            matched_option.click()
            print('-'*10 + f"Gender selected: {gender}" + '-'*10)
        else:
            print('-'*10 + "🥲"*4 + f" Gender '{gender}' not found, skipping selection " + "🥲"*4 + '-'*10)
        time.sleep(1)

        # Fill Date of Birth
        print('-'*10 + " Filling Date of Birth" + '-'*10)
        dob_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Date of Birth']/following::input[@type='text' and @placeholder='YYYY-MM-DD'][1]"))
        )
        dob_field.click()
        dob_field.send_keys(Keys.CONTROL + "a")
        dob_field.send_keys(Keys.DELETE)
        dob_field.send_keys(userDetails.get('dob', ''))
        dob_field.send_keys(Keys.ENTER)
        time.sleep(10)

        # Fill Phone Number
        print('-'*10 + "Filling Phone Number " + '-'*10)
        phone_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Phone Number']/following::input[@type='text'][1]"))
        )
        phone_field.send_keys(userDetails.get('mobile', ''))
        time.sleep(1)

        # Fill Email Id
        print('-'*10 + "Filling Email Id" + '-'*10)
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Email Id']/following::input[@type='text'][1]"))
        )
        email_field.send_keys(userDetails.get('email', ''))
        time.sleep(1)

        print('-'*10 + f"Patient details filled successfully for: {testcase}" + '-'*10)
        return True

    except Exception as e:
        print('-'*10 + "🥲"*4 + f"An error occurred while executing: {testcase} " + "🥲"*4 + '-'*10)
        print('-'*10 + "🥲"*4 + f" Error Details : {e} " + "🥲"*4 + '-'*10)
        return False


def fill_input_by_label(driver, label_text, value_to_fill):
    try:
        # Wait until the label with the specified text is visible
        label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//label[contains(text(), '{label_text}')]"))
        )
        
        # Find the input element following the label
        input_field = label.find_element(By.XPATH, "following-sibling::div//input")
        
        # Clear the input field and fill in the value
        input_field.clear()
        input_field.send_keys(value_to_fill)
        print('-'*10 +f"Filled '{label_text}' with '{value_to_fill}' successfully." + '-'*10)
        
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"An error occurred: {e}" + "🥲"*4 + '-'*10)


def checkConfirmationPage(driver, promo_code, testcase):
    try:
        action_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".action-section"))
        )
        paragraph = action_section.find_element(By.TAG_NAME, "p")
        action_section_text = paragraph.text.strip().replace("\n", " ")

        required_text = "By confirming the appointment you consent to abide by Ayoo’s Terms & Conditions"

        if required_text == action_section_text:
            print('-'*10 + "Confirmation Page is displayed. Proceeding to apply promo code." + '-'*10)

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
                print('-'*10 + "🥲"*4 + f"Invalid Promo Code in {testcase}. Test failed." + "🥲"*4 + '-'*10)
                return False
            except TimeoutException:
                print('-'*10 + "Valid Promo Code applied. Proceeding."  + '-'*10)

            confirm_button = driver.find_element(By.ID, "confirmAppointment")
            confirm_button.click()

            confirmation_page = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.ID, "appointment-confirmation"))
            )
            if confirmation_page.is_displayed():
                print("-" * 10 + f" Appointment Booked Successfully for {testcase} " + "-" * 10)
                return True
            else:
                print('-'*10 + "🥲"*4 + f"Confirmation page not displayed in {testcase}. Test failed." + "🥲"*4 + '-'*10)
                return False
        else:
            print('-'*10 + "🥲"*4 + f" Confirmation page not displayed in {testcase}. Test failed." + "🥲"*4 + '-'*10)
            return False
    except TimeoutException as e:
        print('-'*10 + "🥲"*4 + f"Timeout occurred in {testcase}: {e}" + "🥲"*4 + '-'*10)
        return False
    except NoSuchElementException as e:
        print('-'*10 + "🥲"*4 + f"Element not found in {testcase}: {e}"+ "🥲"*4 + '-'*10)
        return False
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"An unexpected error occurred in {testcase}: {e}"+ "🥲"*4 + '-'*10)
        return False

def login_patient(driver, userdetails, testcase):
    try:
       
        driver.find_element(By.XPATH, "//input[@placeholder='Email/Phone number']").send_keys(userdetails["email"])
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(userdetails["password"])
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='sign in']").click()
        print('-'*10 + f"Login successful for {testcase}." + '-'*10)
        time.sleep(5) 
        return True
    except TimeoutException as e:
        print('-'*10 + "🥲"*4 + f" Timeout during login in {testcase}: {e}" + "🥲"*4 + '-'*10)
        return False
    except NoSuchElementException as e:
        print('-'*10 + "🥲"*4 + f" Element not found during login in {testcase}: {e} " + "🥲"*4 + '-'*10)
        return False
    except Exception as e:
        print('-'*10 + "🥲"*4 + f" An unexpected error occurred during login in {testcase}: {e} " + "🥲"*4 + '-'*10)
        return False

def setup_appointment_signedIn(driver, testcase, appointment_for, consultation_type):
    print('='*10 + f" Starting test for {testcase} "  + '='*10)

    # Login
    login.test_login(driver)
    time.sleep(1)

    # Select care type
    driver.find_element(By.CLASS_NAME, "care-type-banner").click()

    # Select appointment type
    if not selectTypeSignedUser(driver, testcase):
        print('-'*10 + "🥲"*4 + f"Failed to select type for {testcase}. Stopping test." + "🥲"*4 + '-'*10)
        return False
    time.sleep(1)

    # Select appointment for
    if not selectAppointmentFor(driver, appointment_for, testcase):
        print('-'*10 + "🥲"*4 + f"Failed to select appointment for {testcase}. Stopping test." + "🥲"*4 + '-'*10)
        return False
    time.sleep(2)

    # Select consultation type
    if not selectConsultationType(driver, consultation_type, testcase):
        print('-'*10 + "🥲"*4 + f"Failed to select consultation type for {testcase}. Stopping test." + "🥲"*4 + '-'*10)
        return False
    time.sleep(2)

    # Select random symptom
    if not selectRandomSymptom(driver, testcase):
        print('-'*10 + "🥲"*4 + f"Failed to select random symptom for {testcase}. Stopping test." + "🥲"*4 + '-'*10)
        return False
    time.sleep(2)

    # Select time slot
    if not select_time_slot(driver, testcase):
        print('-'*10 + "🥲"*4 + f"Failed to select time slot for {testcase}. Stopping test." + "🥲"*4 + '-'*10)
        return False
    time.sleep(2)

    return True



def setup_appointment_nonsignedIn(driver, appt_For ,testcase):
    driver.get(f"{URL}")
    driver.maximize_window()
    driver.implicitly_wait(10)

    if not selectTypeUnSignedUser(driver, f'{testcase}'):
        print("-" * 10 + "🥲"*4 +  "Failed to select type. Stopping test execution." + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)

    if not selectAppointmentFor(driver, appt_For, f'{testcase}'):
        print("-" * 10 + "🥲"*4 +  "Failed to select appointment. Stopping test execution." + "🥲"*4 + "-" * 10)
        return
    time.sleep(1)

    if not selectConsultationType(driver, 'Virtual', f'{testcase}'):  # InClinic
        print("-" * 10 + "🥲"*4 +  "Failed to select consultation type. Stopping test execution." + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)

    if not selectRandomSymptom(driver, f'{testcase}'):
        print("-" * 10 + "🥲"*4 +  "Failed to select random symptom. Stopping test execution." + "🥲"*4 + "-" * 10)
        return
    time.sleep(1)

    if not select_time_slot(driver, f'{testcase}'):
        print("-" * 10 + "🥲"*4 +  "Failed to select time slot. Stopping test execution." + "🥲"*4 + "-" * 10)
        return
    time.sleep(2)
    return True

def fillNUmandemail_unreg(driver, header, testcase):
    try:
        header_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, f"//h5[contains(normalize-space(.), \"{header}\")]"))
)
     
        # Locate the parent container of the form fields
        form_container = header_element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'userData-form')]")
       
        # Helper function to fill input fields based on label
        def fill_field_by_label(form, label_text, value):
            input_element = form.find_element(
                By.XPATH, f".//label[contains(text(), '{label_text}')]/following-sibling::div//input"
            )
            input_element.click()
            input_element.clear()
            input_element.send_keys(value)
        
        unique_email = fake.email()
        unique_mob = generate_unique_mobile_number()

        fill_field_by_label(form_container, 'Phone Number', unique_mob)
        fill_field_by_label(form_container, 'Email Id', unique_email)
    except:
        print('-'*10 + "🥲"*4 + f'error while printing emaila nd mobile for new user in: {testcase}' + "🥲"*4 + '-'*10)



def fillFormBasedOnHeader(driver, header, testcase, userDetails=None):
    try:
        # Locate the header element
        
        header_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, f"//h5[contains(normalize-space(.), \"{header}\")]"))
)
     
        # Locate the parent container of the form fields
        form_container = header_element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'userData-form')]")
       
        # Helper function to fill input fields based on label
        def fill_field_by_label(form, label_text, value):
            input_element = form.find_element(
                By.XPATH, f".//label[contains(text(), '{label_text}')]/following-sibling::div//input"
            )
            input_element.click()
            input_element.clear()
            input_element.send_keys(value)

        # Helper function to select a gender
        # Updated helper function to select gender
        def fill_gender(form, value='Male'):
            try:
                # Locate the Gender dropdown within the form
                gender_dropdown = WebDriverWait(form, 20).until(
                EC.element_to_be_clickable(
                (By.XPATH, ".//div[@aria-labelledby='Gender-label Gender-select' and contains(@id, 'Gender-select')]")
              )
            )
        
                 # Click to open the dropdown
                gender_dropdown.click()

                # Identify the aria-controls attribute of the dropdown
                aria_controls = gender_dropdown.get_attribute("aria-controls")

        # Use aria-controls to locate the correct dropdown options list
                options_list = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                (By.XPATH, f"//ul[@id='{aria_controls}']")
            )
        )

        # Locate and click the desired option
                options = options_list.find_elements(By.XPATH, ".//li[@data-value]")
                for option in options:
                    if option.text.strip().lower() == value.lower():
                        option.click()
                        return True  # Exit once the correct option is clicked
       
                print('-'*10 + "🥲"*4 + f"Gender option '{value}' not found in dropdown." + "🥲"*4 + '-'*10)
                return False
            except Exception as e:
                print('-'*10 + "🥲"*4 + f"Failed to select gender: {e}" + "🥲"*4 + '-'*10)
                return False

        # Helper function to fill Date of Birth
        # Helper function to fill Date of Birth dynamically
        def fill_dob(form, dob='2000-01-01'):
            try:
                label_element = form.find_element(By.XPATH, f".//label[text()='Date of Birth']")
                # Get the 'for' attribute (or 'id') of the label to identify the corresponding input field
                input_id = label_element.get_attribute("for")
        
                # Use the 'id' to locate the input field
                input_field = WebDriverWait(form, 10).until(
                 EC.visibility_of_element_located(
                (By.XPATH, f"//input[@id='{input_id}']")
                        )
                        )

                 # Clear and fill the input field
                input_field.click()
                input_field.send_keys(Keys.CONTROL + "a") 
                input_field.send_keys(Keys.DELETE) 
                input_field.send_keys(dob)  
                input_field.send_keys(Keys.ENTER)  
                time.sleep(1)
                
            except Exception as e:
                print('-'*10 + "🥲"*4 + f"Failed to fill Date of Birth: {e}" + "🥲"*4 + '-'*10)

  
        # Filling form fields based on the header
        if header.lower() == "patient's information":
            print('-'*10 + f" Filling Patient's Information for {testcase} " + '-'*10)
            fill_field_by_label(form_container, 'First Name', fake.first_name())
            fill_field_by_label(form_container, 'Last Name', fake.last_name())
            time.sleep(1)
            fill_gender(form_container, 'Female') 
            time.sleep(1)
            fill_dob(form_container, '2000-01-01')
            fill_field_by_label(form_container, 'Phone Number', generate_unique_mobile_number())
            fill_field_by_label(form_container, 'Email Id', fake.email())
        elif header.lower() == "caretaker / account manager's information": 
            print('-'*10 + f"Filling Caretaker / Account Manager's Information for {testcase} "+ '-'*10)
            time.sleep(1)
            if userDetails:
                fill_field_by_label(form_container, 'First Name', userDetails.get('first_name', ''))
                fill_field_by_label(form_container, 'Last Name', userDetails.get('last_name', ''))
                time.sleep(1)
                
                fill_gender(form_container, userDetails.get('gender', ''))  
                time.sleep(1)
                fill_dob(form_container, userDetails.get('dob', ''))
                # fill_field_by_label(form_container, 'Phone Number', userDetails.get('mobile', ''))
                # fill_field_by_label(form_container, 'Email Id', userDetails.get('email', ''))
            else: 
                print('-'*10 + "🥲"*4 + "User details are not provided for caretaker. " + "🥲"*4 + '-'*10)
        else:
            print('-'*10 + "🥲"*4 + f"Unknown header: {header} " + "🥲"*4 + '-'*10)

        print('-'*10 + f"Form filling completed for header: {header}, testcase: {testcase}" + '-'*10)
        return True

    except TimeoutException as e:
        print('-'*10 + "🥲"*4 + f" Timeout occurred while locating header: {header} " + "🥲"*4 + '-'*10)
        print('-'*10 + "🥲"*4 + f" Error Details : {e} " + "🥲"*4 + '-'*10)
        return False
    except NoSuchElementException as e:
        print('-'*10 + "🥲"*4 + f"Form fields not found for header: {header} " + "🥲"*4 + '-'*10)
        print('-'*10 + "🥲"*4 + f"Error Details : {e} " + "🥲"*4 + '-'*10)
        return False
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"An unexpected error occurred while handling header: {header} " + "🥲"*4 + '-'*10)
        print('-'*10 + "🥲"*4 + f"Error Details : {e} " + "🥲"*4 + '-'*10)
        return False
