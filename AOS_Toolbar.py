from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AOS_Toolbar:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def checking_home_page(self):
        """checks if the current page is homepage"""
        return self.driver.current_url == "http://www.advantageonlineshopping.com/#/"

    def home_page_click(self):
        """opens the homepage from the logo"""
        self.loading_wait()
        self.driver.find_element(By.CSS_SELECTOR, ".logo").click()

    def loading_wait(self):
        """waiting until the loading page icon disappear"""
        self.wait.until(EC.invisibility_of_element(self.driver.find_element(By.CLASS_NAME, "loader")))

    def cart_page(self):
        """returns the element of cart icon"""
        return self.driver.find_element(By.ID, "shoppingCartLink")

    def open_cart_page(self):
        """opens the cart page from the cart icon"""
        self.cart_page().click()

    def empty_cart_hover_table(self):
        """returns the element of empty cart"""
        return self.driver.find_element(By.CLASS_NAME, "emptyCart")

    def user_menu_button(self):
        """returns the element of user icon from the toolbar"""
        self.wait.until(EC.visibility_of(self.driver.find_element(By.ID, "menuUserLink")))
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.ID, "menuUserLink")))
        return self.driver.find_element(By.ID, "menuUserLink")

    def user_menu_button_click(self):
        """clicking on user icon"""
        sleep(3)
        self.user_menu_button().click()

    def my_orders_page_button(self):
        """returns the element of MyOrders button from the user options"""
        return self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle>.option")[1]

    def my_orders_page_click(self):
        """clicking on MyOrders button from the user options"""
        self.wait.until(EC.invisibility_of_element(self.empty_cart_hover_table()))
        self.my_orders_page_button().click()

    def my_account_page_button(self):
        """returns the element of MyAccount button from the user options"""
        return self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle>.option")[0]

    def my_account_page_button_click(self):
        """clicking on MyAccount button from the user options"""
        self.wait.until(EC.invisibility_of_element(self.empty_cart_hover_table()))
        self.my_account_page_button().click()

    def sign_out_button(self):
        """returns the element of SignOut button from the user options"""
        return self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle>.option")[2]

    def sign_out_button_click(self):
        """clicking on sign out button"""
        self.sign_out_button().click()

    def check_user_is_connected(self):
        """returns the username from the toolbar that applies after login"""
        return self.driver.find_element(By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']").text
