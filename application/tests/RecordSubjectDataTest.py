from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

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
        anchor.click()
        
        time.sleep(1)
        
        #get instance of first pop up  window
        whandle = self.driver.window_handles[1]
        #switch to pop up window
        self.driver.switch_to.window(whandle)
        
        pop_up_anchor_1 = self.driver.find_element(By.ID, "lnkView2")
        pop_up_anchor_1.click()
        
        time.sleep(1)
        
        whandle2 = self.driver.window_handles[1]
        #switch to second pop up window
        self.driver.switch_to.window(whandle2)
        
        site_number = self.driver.find_element(By.ID, "valSiteNum").text
        
        time.sleep(2)
                
        print("[+] Record Subject Data Completed")
        
        return site_number