# -*- coding: utf-8 -*-
from selenium import webdriver
from fixure.session import SessionHelper
from fixure.address import AddressHelper

class Application:

    def __init__(self): # фикстура вызывая класс запускает конструктор инициализирующий браузер
        self.wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-maximized"]}})
        #self.wd = webdriver.Firefox()
        #self.wd.maximize_window()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self) # помошнику передается объект класса Application
        self.address = AddressHelper(self) # помошнику передается объект класса Application

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
        wd.get("http://prestashop.qatestlab.com.ua/ru/")
        # баг в Firefoxe заходит в английскую версию сайта не смотря на указание /ru/

