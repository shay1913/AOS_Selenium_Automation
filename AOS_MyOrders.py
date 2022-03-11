from selenium import webdriver
from selenium.webdriver.common.by import By


class AOS_MyOrders:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def order_number(self):
        """returns the order number from MyOrders page"""
        return self.driver.find_element(By.XPATH,"//table/tbody/tr/td/label[@class='ng-binding']").text
