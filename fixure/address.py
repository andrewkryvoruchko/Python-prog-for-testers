import time

class AddressHelper:

    def __init__(self, app): # app принимает объект self класса Application
        self.app = app

    def information(self, address):
        wd = self.app.wd
        wd.find_element_by_id("firstname").send_keys(address.first_name)
        wd.find_element_by_id("lastname").send_keys(address.last_name)
        wd.find_element_by_id("company").send_keys(address.company)
        wd.find_element_by_id("address1").send_keys(address.address)
        wd.find_element_by_id("postcode").send_keys(address.zipcode)
        wd.find_element_by_id("city").send_keys(address.city)
        wd.find_element_by_id("id_country").send_keys(address.country)
        wd.find_element_by_id("phone").send_keys(address.home_phone)
        wd.find_element_by_id("phone_mobile").send_keys(address.mobile_phone)
        wd.find_element_by_id("id_state").send_keys(address.state)
        wd.find_element_by_id("alias").send_keys(address.assign)
        wd.find_element_by_id("submitAddress").click()

    def add(self, address):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Add my first address']").click()
        self.information(address)

    def add_new(self, address):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Addresses']").click()
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Add an address']").click()
        self.information(address)

    def delete_first_address(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Addresses']").click()
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Delete']").click()
        time.sleep(2)
        alert = wd.switch_to_alert()
        alert.accept()


