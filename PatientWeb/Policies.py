import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import URL from external file
sys.path.append("E:/front-end/automation_selenium/")
from variable import URL


def navigate_and_check(driver, nav_text, header_text, close_icon_xpath):
    
    try:
        # Wait for the navigation link to be present
        nav_link = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, nav_text))
        )
        
        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", nav_link)
        
        # Use JavaScript to click if normal click is intercepted
        try:
            nav_link.click()
        except Exception:
            # print( '-'*10 + "🥲"*4 + f"Click intercepted for {nav_text}, using JavaScript click." + "🥲"*4 + '-'*10)
            driver.execute_script("arguments[0].click();", nav_link)
            
        # Wait for the header element with the specified text to be visible
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[text()='{header_text}']"))
        )
        print( '-'*10 + f"Successfully navigated to page with header: '{header_text}'"  + '-'*10)

        # Wait for the close icon to be clickable and click it
        close_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, close_icon_xpath))
        )
        close_icon.click()

        print('-'*10 + f"Successfully closed the policy page and navigated back to the home screen." + '-'*10)
        return True
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Failed to navigate to page with header: '{header_text}'. Error: {e}" "🥲"*4 + '-'*10 )
        return False

    
def callPolicies(driver):
   
    # List of policies with their corresponding headers
    policies = [
        ("Cancellation Policy", "CANCELLATION AND REFUND POLICY"),
        ("Terms of Use", "TERMS OF USE"),
        ("Privacy Policy", "Privacy Policy")
    ]
    # XPath for the close icon
    close_icon_xpath = "//img[@src='/images/modal-close-primary-color.svg']"

    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(20)

    for i, (nav_text, header_text) in enumerate(policies):
        if not navigate_and_check(driver, nav_text, header_text, close_icon_xpath):
            print('-'*10 + "🥲"*4 + f"Failed to process policy: {nav_text}" + "🥲"*4 + '-'*10)
            return

        # Check if it's the third policy
        if i == len(policies) - 1:
            print('-'*10 + "Successfully navigated all policies. Test completed."+ '-'*10)
            return


def execute_test(test_function):
    
    driver = webdriver.Chrome()
    try:
        test_function(driver)
    except Exception as e:
        print('-'*10 + "🥲"*4 + f"Error executing {test_function.__name__}: {e}"  + "🥲"*4 + '-'*10 )
    finally:
        driver.quit()


if __name__ == "__main__":
    execute_test(callPolicies)
 