from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class AOS_Cart:
    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver

    def cart_num(self):
        """returns the element for the items in cart"""
        return self.driver.find_element(By.CSS_SELECTOR, "#shoppingCartLink>span")

    def cart_num_text(self):
        """returns the number for the items in cart and convert to 'int'"""
        return int(self.cart_num().text)

    def cart_status(self):
        """returns the element for the cart window"""
        return self.driver.find_element(By.ID, "menuCart")

    def cart_window(self):
        """opens the cart small window without click on it"""
        hover = ActionChains(self.driver).move_to_element(self.cart_status())
        hover.perform()

    def product_in_cart(self):
        """returns the elements for products in cart window"""
        return self.driver.find_elements(By.ID, "product")

    def list_product_in_cart(self,num:int):
        """creating a list of all the products in cart window"""
        list1 = self.product_in_cart()
        return list1[num]

    def num_of_products_in_cart(self):
        """returns how many products are in the cart window"""
        list1 = self.product_in_cart()
        return len(list1)

    def product_in_cart_color(self,product):
        """returns the color of a product in cart window"""
        color = product.find_element(By.CSS_SELECTOR, "a>label>span.ng-binding").text
        return color

    def product_in_cart_quantity(self,product):
        """returns the quantity of a product in cart window without the 'QTY:' text in 'int' type"""
        qty = product.find_element(By.CSS_SELECTOR, "a>label.ng-binding").text
        new_quantity = qty[5:]
        return int(new_quantity)

    def product_in_cart_price(self,product):
        """returns the price of a product in cart window without '$' symbol, also for price above thousand"""
        price = product.find_element(By.CSS_SELECTOR, "[class='price roboto-regular ng-binding']").text
        if len(price)==9:
            new_product_price = price[1:]
            correct_num = float(new_product_price[0:1]+new_product_price[2:])
            return correct_num
        else:
            new_product_price = price[1:]
            return float(new_product_price)

    def product_in_cart_name(self,product):
        """returns the name of a product in cart window"""
        name = product.find_element(By.CSS_SELECTOR, "a>h3.ng-binding").text
        return name[:27]

    def delete_product(self):
        """returns the element to delete a product from the cart window"""
        return self.driver.find_element(By.CSS_SELECTOR,"div>.removeProduct").click()

    def check_cart_page(self):
        """returns the text 'SHOPPING CART' from cart page"""
        return self.driver.find_element(By.CSS_SELECTOR,"[class='select  ng-binding']").text

    def total_price(self):
        """returns the total price for the products in cart page"""
        t_price = self.driver.find_element(By.CSS_SELECTOR, "table.fixedTableEdgeCompatibility>tfoot>tr>td[colspan='2']>span.roboto-medium").text
        if len(t_price)==9:
            new_product_price = t_price[1:]
            correct_num = float(new_product_price[0:1]+new_product_price[2:])
            right_format = "{:.2f}".format(correct_num)
            return right_format
        else:
            new_product_price = t_price[1:]
            correct_num = float(new_product_price)
            right_format = "{:.2f}".format(correct_num)
            return right_format

    def edit_button(self,num:int):
        """clicking the 'edit' element for the first and the second product's in cart page"""
        while True:
            try:
                edit = self.driver.find_elements(By.CSS_SELECTOR, ".edit")
                first_p = edit[0]
                second_p = edit[1]
                if num == 3:
                    return first_p.click()
                if num == 2:
                    return second_p.click()
                break
            except:
                pass

    def list_quantity(self,num:int):
        """returns a list of the quantity elements in cart page"""
        product_table = self.driver.find_element(By.CSS_SELECTOR, ".fixedTableEdgeCompatibility")
        list_tr = product_table.find_elements(By.CSS_SELECTOR, "tr.ng-scope")
        return list_tr[num]

    def quantity_in_cart_page(self,product):
        """returns the quantity of product im cart page"""
        product_details = product.find_elements(By.CSS_SELECTOR, "td")
        quantity = product_details[4].find_element(By.CSS_SELECTOR, "label.ng-binding").text
        return int(quantity)

    def go_to_checkout(self):
        """finding and clicking checkout element"""
        sleep(2)
        checkout_button = self.driver.find_element(By.ID, "checkOutButton")
        checkout_button.click()

    def cart_empty_label(self):
        """returns the element of 'CONTINUE SHOPPING'"""
        return self.driver.find_element(By.LINK_TEXT, "CONTINUE SHOPPING")

    def check_empty_cart(self):
        """"checks the cart is empty by comparing the expected text and see if appears"""
        return self.cart_empty_label().text == "CONTINUE SHOPPING"