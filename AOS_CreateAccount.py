from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AOS_CreateAccount:
    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        """returns the element of username field"""
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def password_field(self):
        """returns the element of password field"""
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password_field(self):
        """returns the element of confirm password field"""
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def email_field(self):
        """returns the element of the email field"""
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def i_agree(self):
        """returns the element of the 'i agree' checkbox"""
        return self.driver.find_element(By.NAME, "i_agree")

    def register_button(self):
        """returns the element for the register button"""
        return self.driver.find_element(By.ID, "register_btnundefined")

    def enter_username(self, username):
        """enters username"""
        self.username_field().send_keys(username)

    def enter_email(self, email):
        """enters email"""
        self.email_field().send_keys(email)

    def enter_password(self, password):
        """enters password"""
        self.password_field().send_keys(password)

    def enter_confirm_password(self, confirm_password):
        """enters confirmation password"""
        self.confirm_password_field().send_keys(confirm_password)

    def i_agree_click(self):
        """clicking on 'i agree' checkbox"""
        self.wait.until(EC.visibility_of(self.i_agree()))
        self.i_agree().click()

    def register_button_click(self):
        """clicking on register button"""
        self.wait.until(EC.element_to_be_clickable(self.register_button()))
        self.register_button().click()

    def create_new_account(self, username, email, password):
        """creating new account process"""
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.wait.until(EC.visibility_of(self.i_agree()))
        sleep(2)
        self.i_agree_click()
        self.wait.until(EC.element_to_be_clickable(self.register_button()))
        sleep(2)
        self.register_button_click()