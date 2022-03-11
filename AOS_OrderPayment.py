from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AOS_OrderPayment:
    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def user_name_field(self):
        """returns the element of username field in OrderPayment page"""
        return self.driver.find_element(By.CSS_SELECTOR, "[name='usernameInOrderPayment']")

    def send_user_to_user_name_field_(self, username):
        """enters username"""
        self.user_name_field().send_keys(username)

    def password_field(self):
        """returns the element of password field in OrderPayment page"""
        return self.driver.find_element(By.CSS_SELECTOR, "[name='passwordInOrderPayment']")

    def send_password_to_password_field_(self, password):
        """enters password"""
        self.password_field().send_keys(password)

    def login_button(self):
        """returns the element of login button in OrderPayment page"""
        return self.driver.find_element(By.ID, "login_btnundefined")

    def login_button_click(self):
        """clicking on login button"""
        self.login_button().click()

    def register(self):
        """returns the element of register button in OrderPayment page"""
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def register_button_click(self):
        """clicking on register button in OrderPayment page"""
        self.register().click()

    def next_button(self):
        """returns the element of next button"""
        return self.driver.find_element(By.ID, "next_btn")

    def next_button_click(self):
        """clicking on next button"""
        self.next_button().click()

    def safepay_username(self):
        """returns the element of safepay username field"""
        return self.driver.find_element(By.NAME, "safepay_username")

    def safepay_password(self):
        """returns the element of safepay password field"""
        return self.driver.find_element(By.NAME, "safepay_password")

    def credit_card_payment(self):
        """finds and clicks credit card checkbox"""
        credit_card = self.driver.find_element(By.NAME, "masterCredit")
        credit_card.click()

    def card_number_field(self):
        """returns card number field"""
        return self.driver.find_element(By.NAME, "card_number")

    def cvv_number_field(self):
        """returns cvv number field"""
        return self.driver.find_element(By.NAME, "cvv_number")

    def expiration_month_field(self):
        """returns expiration month field"""
        return self.driver.find_element(By.NAME, "mmListbox")

    def expiration_year_field(self):
        """returns expiration year field"""
        return self.driver.find_element(By.NAME, "yyyyListbox")

    def holder_name_field(self):
        """returns holder name field"""
        return self.driver.find_element(By.NAME, "cardholder_name")

    def pay_now(self):
        """returns the element of pay now button"""
        return self.driver.find_element(By.ID, "payNowSPDrtv")

    def pay_now_button_click(self):
        """clicking on pay now button"""
        self.pay_now().click()

    def thank_you_page(self):
        """"returns the text 'Thank You For Shopping' after placing an order"""
        thank_you_label = self.driver.find_element(By.ID, "orderPaymentSuccess")
        return thank_you_label.find_element(By.CSS_SELECTOR, "span").get_attribute("translate")

    def order_number(self):
        """returns the order number from after that appears placing an order"""
        self.wait.until(EC.visibility_of(self.driver.find_element(By.ID,"orderNumberLabel")))
        return self.driver.find_element(By.ID,"orderNumberLabel").text

    def enter_safepay_username(self, safepay_username):
        """enters safepay username"""
        self.safepay_username().send_keys(safepay_username)

    def enter_safepay_password(self, safepay_password):
        """enters safepay password"""
        self.safepay_password().send_keys(safepay_password)

    def safepay_payment(self, username, password):
        """Payment by SafePay process"""
        self.enter_safepay_username(username)
        self.enter_safepay_password(password)
        self.pay_now_button_click()
        sleep(3)

    def enter_card_number(self, card_number):
        """enters card number"""
        self.card_number_field().send_keys(card_number)

    def enter_cvv(self, cvv_number):
        """enters cvv number"""
        self.cvv_number_field().send_keys(cvv_number)

    def enter_expiration_month(self, mmListbox):
        """enters expiration month"""
        self.expiration_month_field().send_keys(mmListbox)

    def enter_expiration_year(self, yyyyListbox):
        """enters expiration year"""
        self.expiration_year_field().send_keys(yyyyListbox)

    def enter_holder_name(self, cardholder_name):
        """enters holder name"""
        self.holder_name_field().send_keys(cardholder_name)

    def pay_with_card(self):
        """enters expiration month"""
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment").click()

    def pay_with_creditcard(self, card_number, mmListbox, yyyyListbox, cvv_number,cardholder_name):
        """Payment with CreditCard process"""
        self.credit_card_payment()
        self.enter_card_number(card_number)
        self.enter_expiration_month(mmListbox)
        self.enter_expiration_year(yyyyListbox)
        self.enter_cvv(cvv_number)
        self.enter_holder_name(cardholder_name)
        self.pay_with_card()

    def login_existing_user(self, username, password):
        """login process from OrderPayment page"""
        self.send_user_to_user_name_field_(username)
        self.send_password_to_password_field_(password)
        self.login_button_click()