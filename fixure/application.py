# -*- coding: utf-8 -*-
from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def distroy(self):
        self.driver.quit()

    def open_home_page(self):
        self.driver.get("http://prestashop.qatestlab.com.ua/ru/")

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element_by_css_selector(".header_user_info a").click()
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("passwd").send_keys(password)
        self.driver.find_element_by_name("SubmitLogin").click()

    def information(self, address):
        self.driver.find_element_by_id("firstname").send_keys(address.first_name)
        self.driver.find_element_by_id("lastname").send_keys(address.last_name)
        self.driver.find_element_by_id("company").send_keys(address.company)
        self.driver.find_element_by_id("address1").send_keys(address.address)
        self.driver.find_element_by_id("postcode").send_keys(address.zipcode)
        self.driver.find_element_by_id("city").send_keys(address.city)
        self.driver.find_element_by_id("id_country").send_keys(address.country)
        self.driver.find_element_by_id("phone").send_keys(address.home_phone)
        self.driver.find_element_by_id("phone_mobile").send_keys(address.mobile_phone)
        self.driver.find_element_by_id("id_state").send_keys(address.state)
        self.driver.find_element_by_id("alias").send_keys(address.assign)
        self.driver.find_element_by_id("submitAddress").click()

    def add_address(self, address):
        self.driver.find_element_by_xpath("//div[@id='center_column']//a[@title='Add my first address']").click()
        self.information(address)

    def add_new_address(self, address):
        self.driver.find_element_by_xpath("//div[@id='center_column']//a[@title='Addresses']").click()
        self.driver.find_element_by_xpath("//div[@id='center_column']//a[@title='Add an address']").click()
        self.information(address)

    def logout(self):
        self.driver.find_element_by_xpath("//div[@class='row']//a[text()='Выйти']").click()
