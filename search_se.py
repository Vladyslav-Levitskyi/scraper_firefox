#   Let's start to scrape some data from the movie website.
#   In this first part of code we will go to the website, automatically logging in,
#   go to the desired section and save html code of 20 pages,
#   that we can scrape soon on our local machine.


#   Import all needed modules 
import time
import codecs
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, dotenv_values
import os


#   To ensure safety for all sensitive data we will use "dotenv" module.
load_dotenv()
config = dotenv_values(".env")
URL = os.getenv("URL")
USERNAME = config["USERNAME"]   #   This is the solution for .env conflict with a symbol "@"
PASSWORD = os.getenv("PASSWORD")
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
service = Service(executable_path=r"C:\Users\Admin\Desktop\Cursorprojcts\web-scraper-firefox\geckodriver.exe")
driver = webdriver.Firefox(options, service=service)


# Class LogInGetPages has two main functions that can logging in and save html
# page source to local machine.
class LogInGetPages:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def login_func(self):
        driver.get(url=self.url)  
        log_in = driver.find_element(By.CLASS_NAME, "b-tophead__login")
        log_in.click()      
        time.sleep(2)
        field_login = driver.find_element(By.ID, "login_name")
        field_login.send_keys(self.username)
        field_password = driver.find_element(By.ID, "login_password")
        field_password.send_keys(self.password)
        time.sleep(3)
        field_password.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.close()
        self.get_html_source()

    def get_html_source(self):
        for page in range(1, 20 + 1):
            driver.get(url=self.url + str("films/page/") + str(page))   
            #   driver.find_element(By.XPATH, "//a[@href='/films/']").click() - This is alternative method
            #   to find needed tab on website.
            time.sleep(2)
            source = driver.page_source
            time.sleep(2)
            with codecs.open("source_file", "a", encoding="utf-8") as file:
                file.write(source)
            time.sleep(1)
        time.sleep(3)
        driver.close()
        driver.quit()


get_page_func = LogInGetPages(URL, USERNAME, PASSWORD)
get_page_func.login_func()