from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from AOS_Category import AOS_Category
from AOS_Cart import AOS_Cart
from AOS_Product import AOS_Product
from AOS_Toolbar import AOS_Toolbar
from AOS_OrderPayment import AOS_OrderPayment
from AOS_CreateAccount import AOS_CreateAccount
from AOS_MyOrders import AOS_MyOrders
from AOS_LoginPopUp import AOS_LoginPopUp
from random import randint
from selenium.webdriver.common.by import By


class AOS_UnitTests(TestCase):
    def setUp(self):
        """Setting Up the webdriver at the AOS's url.
        Defining all relevant page objects for the tests."""
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")
        # service_firefox = Service(r"C:\selenium1\geckodriver.exe")

        # Setting up the webdriver and browser:
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("http://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        # In case an element is not found on the page, will try again for 10 seconds
        # before we get an error message
        self.driver.implicitly_wait(20)
        # Raffle of random numbers for the products in tests:
        self.random_product1 = randint(1,10)
        self.random_category1 = randint(1,5)
        self.random_product2 = randint(1,10)
        self.random_category2 = randint(1,5)
        self.random_product3 = randint(1,10)
        self.random_category3 = randint(1,5)
        # Defining page objects:
        self.category_page = AOS_Category(self.driver)
        self.cart_page = AOS_Cart(self.driver)
        self.product_page = AOS_Product(self.driver)
        self.toolbar = AOS_Toolbar(self.driver)
        self.order_payment = AOS_OrderPayment(self.driver)
        self.create_account = AOS_CreateAccount(self.driver)
        self.my_orders = AOS_MyOrders(self.driver)
        self.login_popup = AOS_LoginPopUp(self.driver)

    def test_1(self):
        """This test is checking that the amount in cart icon is correct"""
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1,self.random_product1)
        self.product_page.add_quantity()
        product1_quantity = self.product_page.product_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category2)
        self.category_page.open_product_page(self.random_category2,self.random_product2)
        for i in range(2):
            self.product_page.add_quantity()
        product2_quantity = self.product_page.product_quantity()
        self.product_page.add_to_cart_click()

        self.assertEqual(self.cart_page.cart_num_text(), product1_quantity + product2_quantity)

    def test_2(self):
        """This test verifies that the product details in the cart window matched the product details"""
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1,self.random_product1)
        self.product_page.add_quantity()
        product1_quantity = self.product_page.product_quantity()
        product1_price = self.product_page.product_price()
        product1_color = self.product_page.product_color()
        product1_name = self.product_page.product_name()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category2)
        self.category_page.open_product_page(self.random_category2,self.random_product2)
        for i in range(2):
            self.product_page.add_quantity()
        product2_quantity = self.product_page.product_quantity()
        product2_price = self.product_page.product_price()
        product2_color = self.product_page.product_color()
        product2_name = self.product_page.product_name()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category3)
        self.category_page.open_product_page(self.random_category3,self.random_product3)
        for i in range(3):
            self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        product3_quantity = self.product_page.product_quantity()
        product3_price = self.product_page.product_price()
        product3_color = self.product_page.product_color()
        product3_name = self.product_page.product_name()
        self.toolbar.home_page_click()


        self.cart_page.cart_window()
        # Test for the first product
        first_product = self.cart_page.list_product_in_cart(-1)
        self.assertEqual(self.cart_page.product_in_cart_name(first_product), product1_name)
        self.assertEqual(self.cart_page.product_in_cart_quantity(first_product), product1_quantity)
        self.assertEqual(self.cart_page.product_in_cart_color(first_product), product1_color)
        self.assertEqual(self.cart_page.product_in_cart_price(first_product), (self.product_page.calculation_price(product1_price,product1_quantity)))

        # Test for the second product
        second_product = self.cart_page.list_product_in_cart(-2)
        self.assertEqual(self.cart_page.product_in_cart_name(second_product), product2_name)
        self.assertEqual(self.cart_page.product_in_cart_quantity(second_product), product2_quantity)
        self.assertEqual(self.cart_page.product_in_cart_color(second_product), product2_color)
        self.assertEqual(self.cart_page.product_in_cart_price(second_product), (self.product_page.calculation_price(product2_price,product2_quantity)))

        # # Test for the Third product
        third_product = self.cart_page.list_product_in_cart(-3)
        self.assertEqual(self.cart_page.product_in_cart_name(third_product), product3_name)
        self.assertEqual(self.cart_page.product_in_cart_quantity(third_product), product3_quantity)
        self.assertEqual(self.cart_page.product_in_cart_color(third_product), product3_color)
        self.assertEqual(self.cart_page.product_in_cart_price(third_product), (self.product_page.calculation_price(product3_price,product3_quantity)))


    def test_3(self):
        """This test verifies deleting product from the cart window"""
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1,self.random_product1)
        self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category2)
        self.category_page.open_product_page(self.random_category2,self.random_product2)
        for i in range(2):
            self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.cart_page.cart_window()
        # Check that there is two products in cart
        self.assertEqual(self.cart_page.num_of_products_in_cart(),2)
        # Delete the last product
        self.cart_page.delete_product()
        # Check that now there is one product in cart
        self.assertEqual(self.cart_page.num_of_products_in_cart(),1)

    def test_4(self):
        """This test makes sure that after clicking on the 'Cart' icon,
         the page redirected to the 'Shopping Cart' page"""
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1,self.random_product1)
        self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.open_cart_page()

        self.assertEqual(self.cart_page.check_cart_page(),"SHOPPING CART")

    def test_5(self):
        """This test checks that the total order price is the sum of all the products
        which are in the cart - according to the actual products' price as shown
        when ordering them """
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1, self.random_product1)
        self.product_page.add_quantity()
        product1_quantity = self.product_page.product_quantity()
        product1_price = self.product_page.product_price()
        self.product_page.add_to_cart_click()
        self.product_page.product_details()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category2)
        self.category_page.open_product_page(self.random_category2, self.random_product2)
        for i in range(2):
            self.product_page.add_quantity()
        product2_quantity = self.product_page.product_quantity()
        product2_price = self.product_page.product_price()
        self.product_page.add_to_cart_click()
        self.product_page.product_details()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category3)
        self.category_page.open_product_page(self.random_category3, self.random_product3)
        for i in range(3):
            self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        product3_quantity = self.product_page.product_quantity()
        product3_price = self.product_page.product_price()
        self.product_page.product_details()
        self.toolbar.open_cart_page()

        self.assertEqual(self.cart_page.total_price(),self.product_page.product_total_price(product1_price,product1_quantity,product2_price,product2_quantity,product3_price,product3_quantity))


    def test_6(self):
        """BUG! This test checks the edit feature that after edit product quantity,the quantity will update on the cart page.
        The test fails to success cause the edit button always edit the first product quantity"""
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1,self.random_product1)
        self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category2)
        self.category_page.open_product_page(self.random_category2,self.random_product2)
        for i in range(2):
            self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category3)
        self.category_page.open_product_page(self.random_category3, self.random_product3)
        for i in range(3):
            self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.open_cart_page()
        # Increase quantity for the last product in one
        self.cart_page.edit_button(3)
        self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.open_cart_page()
        self.cart_page.edit_button(2)
        # Increase quantity for the second product in one
        self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.open_cart_page()

        second_product = self.cart_page.list_quantity(-2)
        third_product = self.cart_page.list_quantity(-3)

        self.assertEqual(self.cart_page.quantity_in_cart_page(second_product),4)
        self.assertEqual(self.cart_page.quantity_in_cart_page(third_product),5)

    def test_7(self):
        """This test checks the transition between pages using the navigation bar"""
        self.category_page.open_category_page(3)
        self.category_page.open_product_page(3,1)
        self.product_page.return_to_category_button_click()
        self.assertEqual(self.category_page.category_title(), "TABLETS")
        self.toolbar.home_page_click()
        self.assertTrue(self.toolbar.checking_home_page())


    def test_8(self):
        """This test checks an E2E process of order placement using SafePay method for
        a new user"""
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1,self.random_product1)
        self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category2)
        self.category_page.open_product_page(self.random_category2,self.random_product2)
        for i in range(2):
            self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.open_cart_page()
        self.cart_page.go_to_checkout()
        self.order_payment.register_button_click()
        self.create_account.create_new_account("joker124","joker@gmail.com","fazug4nJVG6r")
        self.create_account.register_button_click()
        self.order_payment.next_button_click()
        self.order_payment.safepay_payment("SafePay12", "Tc10")
        self.assertTrue(self.order_payment.thank_you_page())
        OP_order_number = self.order_payment.order_number()
        self.toolbar.open_cart_page()
        self.assertTrue(self.cart_page.check_empty_cart())
        self.toolbar.user_menu_button_click()
        self.toolbar.my_orders_page_click()
        self.assertEqual(self.my_orders.order_number(),OP_order_number)

    def test_9(self):
        """This test checks an E2E process of order placement using CreditCard for
        an existing user"""
        self.category_page.open_category_page(self.random_category1)
        self.category_page.open_product_page(self.random_category1,self.random_product1)
        self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.home_page_click()
        self.category_page.open_category_page(self.random_category2)
        self.category_page.open_product_page(self.random_category2,self.random_product2)
        for i in range(2):
            self.product_page.add_quantity()
        self.product_page.add_to_cart_click()
        self.toolbar.open_cart_page()
        self.cart_page.go_to_checkout()
        self.order_payment.login_existing_user("Tester7","Tes321")
        self.order_payment.next_button_click()
        self.order_payment.pay_with_creditcard("448833993897","11","2026","4561","Mikael")
        self.assertTrue(self.order_payment.thank_you_page())
        OP_order_number = self.order_payment.order_number()
        self.toolbar.open_cart_page()
        self.assertTrue(self.cart_page.check_empty_cart())
        self.toolbar.user_menu_button_click()
        self.toolbar.my_orders_page_click()
        self.assertEqual(self.my_orders.order_number(), OP_order_number)

    def test_10(self):
        """This test checks an E2E process of login and logout"""
        self.toolbar.user_menu_button_click()
        self.login_popup.sign_in("Kumin1", "Kumin1", "no")
        self.assertEqual(self.toolbar.check_user_is_connected(),"Kumin1")
        self.toolbar.user_menu_button_click()
        self.toolbar.sign_out_button_click()
        self.toolbar.user_menu_button_click()
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR,".facebook"))

    def tearDown(self):
        self.driver.close()
