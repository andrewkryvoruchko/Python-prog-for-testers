import time
from selenium.common.exceptions import InvalidElementStateException, NoSuchElementException
from model.address import Address


class AddressHelper:

    def __init__(self, app): # app принимает объект self класса Application
        self.app = app

    def change_field_value(self, id_name, text):
        wd = self.app.wd
        if text is not None:
            try:
                #wd.find_element_by_id(id_name).click() # click на теге <select> вываливает список
                wd.find_element_by_id(id_name).clear()
            except InvalidElementStateException: # clear для тега <select> выдает данное исключение
                pass
            #time.sleep(2)
            wd.find_element_by_id(id_name).send_keys(text)

    def data(self, address):
        self.change_field_value("firstname", address.first_name)
        self.change_field_value("lastname", address.last_name)
        self.change_field_value("company", address.company)
        self.change_field_value("address1", address.address)
        self.change_field_value("postcode", address.zipcode)
        self.change_field_value("city", address.city)
        self.change_field_value("id_country", address.country)
        self.change_field_value("phone", address.home_phone)
        self.change_field_value("phone_mobile", address.mobile_phone)
        self.change_field_value("id_state", address.state)
        self.change_field_value("alias", address.title)

    def submit_address(self):
        wd = self.app.wd
        #time.sleep(2)
        wd.find_element_by_id("submitAddress").click()

    def verify_page_with_addresses(self):
        wd = self.app.wd
        wd.implicitly_wait(1)
        if wd.current_url.endswith("addresses") and \
                wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Add an address']"):
            return  # если условие if выполняется то преждевременно завершаем выполнение метода
            # поток выполнения кода до нижней стороки не дойдет (можно использовать и else или not)
        wd.find_element_by_css_selector("a.account").click()
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Addresses']").click()
        wd.implicitly_wait(20)

    def add_first(self, address):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Add my first address']").click()
        self.data(address)
        self.submit_address()

    def add(self, address):
        wd = self.app.wd
        wd.implicitly_wait(20)
        self.verify_page_with_addresses()
        wd.find_element_by_xpath("//div[@id='center_column']//a[@title='Add an address']").click()
        self.data(address)
        self.submit_address()
        self.address_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.verify_page_with_addresses()
        wd.find_elements_by_xpath("//div[@id='center_column']//a[@title='Delete']")[index].click()
        alert = wd.switch_to_alert()
        alert.accept()
        self.address_cache = None

    def modify_first(self, new_address_data):
        self.modify_by_index(0, new_address_data)

    def modify_by_index(self, index, new_address_data):
        wd = self.app.wd
        self.verify_page_with_addresses()
        wd.find_elements_by_xpath("//div[@id='center_column']//a[@title='Update']")[index].click()
        self.submit_address()
        self.data(new_address_data)
        self.submit_address()
        self.address_cache = None

    def count(self):
        wd = self.app.wd
        self.verify_page_with_addresses()
        wd.implicitly_wait(2)
        return len(wd.find_elements_by_xpath("//div[@id='center_column']//a[@title='Delete']"))

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None or self.address_cache == []:
            wd = self.app.wd
            self.verify_page_with_addresses()
            wd.implicitly_wait(2)
            self.address_cache = []
            for element in wd.find_elements_by_xpath("//div[@class='col-xs-12 col-sm-6 address']"):
                id = element.find_element_by_css_selector("h3.page-subheading").text
                name = element.find_element_by_css_selector("span.address_name").text
                title = element.find_element_by_css_selector("h3.page-subheading").text
                self.address_cache.append(Address(id=id, first_name=name, title=title))  # прикольная штука
            wd.implicitly_wait(20)
        return list(self.address_cache)

