# -*- coding: utf-8 -*-
from selenium import webdriver
from fixure.session import SessionHelper
from fixure.address import AddressHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self) # помошнику передается объект класса Application
        self.address = AddressHelper(self) #

    def distroy(self):
        wd = self.wd
        wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://prestashop.qatestlab.com.ua/ru/")

