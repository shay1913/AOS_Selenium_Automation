from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_LoginPopUp:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        """returns the element of username field"""
        return self.driver.find_element(By.NAME, "username")

    def password_field(self):
        """returns the element of password field"""
        return self.driver.find_element(By.NAME, "password")

    def remember_me_box(self):
        """returns the element of 'remember me' checkbox"""
        return self.driver.find_element(By.NAME, "remember_me")

    def sign_in_button(self):
        """returns the element of 'sign in' button"""
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    def enter_username(self, username):
        """enters a username"""
        self.username_field().send_keys(username)

    def enter_password(self, password):
        """enters a password"""
        self.password_field().send_keys(password)

    def check_remember_me_box(self):
        """clicking on 'remember me' checkbox"""
        self.remember_me_box().click()

    def sign_in_button_click(self):
        """clicking on 'sign in'"""
        self.sign_in_button().click()

    def sign_in(self, username, password, remember_me="no"):
        """Login process"""
        self.enter_username(username)
        self.enter_password(password)
        if remember_me == "yes":
            self.remember_me_box().click()
        self.sign_in_button_click()