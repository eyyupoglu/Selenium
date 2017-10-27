from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://auth.dtu.dk/dtu")

    def test_Login(self):
        driver = self.driver
        dtuUsername = "s174448"


        dtuPassword ="PASSWORD"
        usernameID = "ContentPlaceHolder1_Textbox_Username"
        passwordID = "ContentPlaceHolder1_TextBox_Password"
        loginbuttonXPATH ="//*[@id=\"Button_Login\"]"
        DTUinsideHref = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/span/ul/li[1]/a"


        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(usernameID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passwordID))
        loginFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginbuttonXPATH))



        emailFieldElement.clear()
        emailFieldElement.send_keys(dtuUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(dtuPassword)

        loginFieldElement.click()

        next_page = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(DTUinsideHref))
        next_page.click()
        time.sleep(3)


        english_button_Xpath="/html/body/form/div[3]/header/div[1]/div[2]/div/div[2]/nav/div[3]/a"
        english_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(english_button_Xpath))
        english_button.click()

    def tearDown(self):
        time.sleep(300)

        self.driver.quit()


if __name__ =='__main__':
    unittest.main()

    LoginTest()

