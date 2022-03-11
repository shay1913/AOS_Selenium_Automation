from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AOS_Product:
    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def quantity(self):
        """"returns the element to increase the quantity in 1"""
        return self.driver.find_element(By.CSS_SELECTOR,".plus")

    def calculation_price(self,price,quantity):
        """calculating the product price and returns in right format"""
        canculation = price*quantity
        right_format = "{:.2f}".format(canculation)
        return float(right_format)

    def add_quantity(self):
        """clicking the element"""
        self.quantity().click()

    def add_to_cart(self):
        """"returns the element to click 'add to cart'"""
        return self.driver.find_element(By.NAME,"save_to_cart")

    def add_to_cart_click(self):
        """clicking the element"""
        self.add_to_cart().click()

    def product_name(self):
        """returns the name of product without 3 dots"""
        name = self.driver.find_element(By.XPATH,"//*[@class='roboto-regular screen768 ng-binding']").text
        return name[:27]

    def product_price_with_symbol(self):
        """returns the product's price with $ symbol"""
        return self.driver.find_element(By.CSS_SELECTOR,"section>article>div>div>h2.roboto-thin").text

    def product_price(self):
        """returns the product's price in float also for product that costs more than thousand"""
        price_with_symbol = self.driver.find_element(By.CSS_SELECTOR,"section>article>div>div>h2.roboto-thin").text
        if len(price_with_symbol)==9:
            new_product_price = price_with_symbol[1:]
            correct_num = float(new_product_price[0:1]+new_product_price[2:])
            return correct_num
        else:
            new_product_price = price_with_symbol[1:]
            return float(new_product_price)

    def list_of_colors(self):
        """returns a list of each color in the products color pallet"""
        return self.driver.find_elements(By.XPATH, '//div[@class=""]/span')

    def product_color(self):
        """returns the default color in product's page"""
        return self.list_of_colors()[0].get_attribute('title')

    def product_quantity(self):
        """returns the chosen quantity for product in type 'int'"""
        quantity = self.driver.find_element(By.XPATH,"//*[@name='quantity']").get_attribute('value')
        return int(quantity)

    def product_total_price(self,price1,quantity1,price2,quantity2,price3,quantity3):
        """returns the sum of chosen product's according to each product price and quantity in the desired format"""
        total = float(price1*quantity1+price2*quantity2+price3*quantity3)
        right_format = "{:.2f}".format(total)
        return right_format

    def product_details(self):
        """printing each product details"""
        print(f"Product Name: {self.product_name()}\nQuantity: {self.product_quantity()}\nPrice: {self.product_price_with_symbol()}\n====================================")

    def return_to_category_button(self):
        """the element for navigating back to the category page"""
        return self.driver.find_elements(By.CSS_SELECTOR, "a.ng-binding")[0]

    def return_to_category_button_click(self):
        """clicking the navigating back element"""
        self.wait.until(EC.element_to_be_clickable(self.return_to_category_button()))
        self.return_to_category_button().click()
