from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AOS_Toolbar import AOS_Toolbar


class AOS_Category:
    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.toolbar = AOS_Toolbar(self.driver)

    def category_title(self):
        """returns the element for category"""
        return self.driver.find_element(By.CLASS_NAME, "categoryTitle").text

    def categories_id(self):
        """creating a dictionary for all the categories"""
        return {1: 'speakersImg', 2: 'laptopsImg', 3: 'tabletsImg', 4: 'miceImg', 5: 'headphonesImg'}

    def speakers_products_id(self):
        """creating a list of all the id's in speakers category"""
        speakers_list =  ["19","20","21","22","23","24","25"]
        return speakers_list

    def laptops_products_id(self):
        """Creating a list of all the id's in laptops category"""
        laptops_list = ["1","2","3","4","5","6","7","8","9","10","11"]
        return laptops_list

    def tablets_products_id(self):
        """creating a list of all the id's in tablets category"""
        teblets_list = ["16","17","18"]
        return teblets_list

    def mice_products_id(self):
        """creating a list of all the id's in mices category"""
        mices_list = ["26","27","28","29","30","31","32","33","34"]
        return mices_list

    def headphones_products_id(self):
        """creating a list of all the id's in headphones category"""
        headphones_list = ["12","14","15"]
        return headphones_list

    def open_category_page(self,category_num):
        """getting a number that defining the key for the categories dictionary than open the category"""
        self.toolbar.loading_wait()
        dict1 = self.categories_id()
        if category_num == 5:
            self.wait.until(EC.invisibility_of_element(self.driver.find_element(By.ID,"toolTipCart")))
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.ID,dict1[category_num])))
        return self.driver.find_element(By.ID,dict1[category_num]).click()

    def open_product_page(self,category_num,num_of_product):
        """according to the product's category number, getting one number than choosing one product from the list.
        if the number is bigger than the product's list, the first product will be selected"""
        self.toolbar.loading_wait()
        if category_num == 1:
            if num_of_product<=6:
                return self.driver.find_element(By.ID, self.speakers_products_id()[num_of_product]).click()
            else:
                return self.driver.find_element(By.ID, self.speakers_products_id()[1]).click()
        if category_num == 2:
            if num_of_product<=10:
                return self.driver.find_element(By.ID, self.laptops_products_id()[num_of_product]).click()
            else:
                return self.driver.find_element(By.ID, self.laptops_products_id()[1]).click()
        if category_num == 3:
            if num_of_product<=2:
                return self.driver.find_element(By.ID, self.tablets_products_id()[num_of_product]).click()
            else:
                return self.driver.find_element(By.ID, self.tablets_products_id()[1]).click()
        if category_num == 4:
            if num_of_product<=8:
                return self.driver.find_element(By.ID, self.mice_products_id()[num_of_product]).click()
            else:
                return self.driver.find_element(By.ID, self.mice_products_id()[1]).click()
        if category_num == 5:
            if num_of_product<=2:
                return self.driver.find_element(By.ID, self.headphones_products_id()[num_of_product]).click()
            else:
                return self.driver.find_element(By.ID, self.headphones_products_id()[1]).click()