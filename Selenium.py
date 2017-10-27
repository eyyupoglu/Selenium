#This is just a project that automates to get the messages coming from my DTU instructors.
#What it does in a nutshell: login DTU campusnet website and login the username password
#turning page to english and checkinng the times of the posts on the left side
#if the very top one is different from the last date, then clicks on it and navigates to the next page and taking the bo
#paragraph of the next page and sending it with mail to me.
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import smtplib
#This is just the name of the python file named scrape in the repository.Not a well named name
import scrape

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://auth.dtu.dk/dtu")

    def test_Login(self):
        driver = self.driver
        dtuUsername = "s174448"
        dtuPassword ="PASSWORD(Sorry I cannot share this one)"

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
        time.sleep(1)


        english_button_Xpath="/html/body/form/div[3]/header/div[1]/div[2]/div/div[2]/nav/div[3]/a"
        english_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(english_button_Xpath))
        english_button.click()

        text1 = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath("//*[@id=\"outercontent\"]/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/span[1]"))
        text = text1.text

        last_date ="27 Oct 2017, kl. 14:16"
        print(text)
        print(last_date)
        if not text == last_date:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//*[@id=\"outercontent\"]/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/h2/a")).click()
            mail_text = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//*[@id=\"koContainer\"]/div[1]/div[3]/div/div[2]")).text



            scrape.send_mail(mail_text)



    def tearDown(self):
        time.sleep(10)

        self.driver.quit()

#Unittesting
if __name__ =='__main__':
    unittest.main()

    LoginTest()

