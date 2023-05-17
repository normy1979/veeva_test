from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginTest:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):
        login_form_id = "Form1"
        username_login_id = "txtLogin"
        password_login_id = "txtPassword"
        button_login_id = "btnLogin"
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, username_login_id))
        )

        # find username/email field and send the username itself to the input field
        element.send_keys(self.username)
        # find password input field and insert password as well
        element2 = self.driver.find_element(By.ID, password_login_id)
        element2.send_keys(self.password)
        # click login button
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, button_login_id))))
                
        print("[+] Login successful")