
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_contact_list(self):
        self.app.address.verify_page_with_addresses()
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for row in wd.find_elements_by_xpath("//div[@class='col-xs-12 col-sm-6 address']/ul"):
               # cells = row.find_elements_by_tag_name("li")
               # print('***', len(cells))
               # print('index [1]', (cells[1]).text)
                id = row.find_element_by_css_selector("li .page-subheading").text
                first_name = row.find_element_by_xpath('(li/span[@class="address_name"])[1]').text
                last_name = row.find_element_by_xpath('(li/span[@class="address_name"])[2]').text
                home_phone =  row.find_element_by_css_selector("li .address_phone").text
                mobile_phone = row.find_element_by_css_selector("li .address_phone_mobile").text
                all_phones = home_phone + mobile_phone
                self.contact_cache.append(Contact(id= id, first_name=first_name, last_name=last_name,
                                                  home_phone=home_phone, mobile_phone=mobile_phone,
                                                  all_phones=all_phones))
        return list(self.contact_cache)

    def open_address_to_edit_page_by_index(self, index):
        wd = self.app.wd
        self.app.address.verify_page_with_addresses()
        wd.find_elements_by_xpath("//div[@id='center_column']//a[@title='Update']")[index].click()


    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_address_to_edit_page_by_index(index)
        self.app.address.submit_address()
        id = wd.find_element_by_id("alias").get_attribute("value")
        first_name = wd.find_element_by_id("firstname").get_attribute("value")
        last_name = wd.find_element_by_id("lastname").get_attribute("value")
        home_phone = wd.find_element_by_id("phone").get_attribute("value")
        mobile_phone = wd.find_element_by_id("phone_mobile").get_attribute("value")
        all_phones = home_phone + mobile_phone
        return Contact(id=id, first_name=first_name, last_name=last_name,
                       home_phone=home_phone, mobile_phone=mobile_phone, all_phones=all_phones)
