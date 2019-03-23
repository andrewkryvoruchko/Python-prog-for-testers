from selenium.common.exceptions import NoSuchElementException


class SessionHelper:

    session_name = None

    def __init__(self, app):  # app принимает объект self класса Application
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(".header_user_info a").click()
        wd.find_element_by_id("email").send_keys(username)
        wd.find_element_by_id("passwd").send_keys(password)
        wd.find_element_by_name("SubmitLogin").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='row']//a[@class='logout']").click()

    def is_logged_in(self):
        wd = self.app.wd
        wd.implicitly_wait(1)
        return len(wd.find_elements_by_xpath("//div[@class='row']//a[@class='logout']")) > 0

    def is_logged_in_as(self, s_name):
        wd = self.app.wd
        return wd.find_element_by_css_selector(".header_user_info a.account span").text == ""+s_name+""
        # выполняется проверка на соответствие имен

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):  # урок 13
        wd = self.app.wd
        global session_name
        if self.is_logged_in():
            if self.is_logged_in_as(session_name):
                wd.implicitly_wait(20)
                return
            else:
                self.logout()
        wd.implicitly_wait(20)
        self.login(username, password)
        session_name =  wd.find_element_by_css_selector(".header_user_info a.account span").text


