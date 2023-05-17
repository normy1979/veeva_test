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
        href_value = "javascript:void AOP(&#39;/VEV-901/SubjectPop.aspx?__SubjectID=8d50de76-d251-486d-83c3-dff2d3211bec&#39;, 280, 250, &#39;no&#39;);"
        anchor = self.driver.find_element(By.XPATH, "//a[@href='" + href_value + "']")
        # anchor = self.driver.find_element(By.CLASS_NAME, "fa-gen menu")
        print(anchor.text)
        anchor.click()
                
        print("[+] Record Subject Data Completed")