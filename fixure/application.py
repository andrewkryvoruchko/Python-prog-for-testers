# -*- coding: utf-8 -*-
from selenium import webdriver
from fixure.session import SessionHelper
from fixure.address import AddressHelper
from fixure.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url): # фикстура вызывая класс запускает конструктор инициализирующий браузер
        if browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.maximize_window()
            self.wd.implicitly_wait(20)
        elif browser == "chrome":
            self.wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-maximized"]}})
            self.wd.implicitly_wait(20)
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.address = AddressHelper(self)  # помошнику передается объект self класса Application
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:                    # блок с перехватом исключений
            self.wd.current_url # перехватываем исключение
            return True
        except:                 # прописывается обработчик
            return False

    def distroy(self):
        wd = self.wd
        wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        # Firefoxe заходит в английскую версию сайта не смотря на указание /ru/

