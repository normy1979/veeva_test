from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class RecordSubjectDataTest:
    def __init__(self, driver):
        self.driver = driver

    def click(self):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "grid"))
        )
        tr = self.driver.find_element(By.CLASS_NAME, "mygrid")
        td = tr.find_element(By.TAG_NAME, "td")
        anchor = td.find_element(By.TAG_NAME, "a")
        print("Text: " + anchor.text)
        anchor.click()
                
        print("[+] Record Subject Data Completed")