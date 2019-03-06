


class SessionHelper:

    def __init__(self, app): # app принимает объект self класса Application
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
        wd.find_element_by_xpath("//div[@class='row']//a[text()='Выйти']").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//div[@class='row']//a[text()='Выйти']")) > 0

    def is_logged_in_as(self, session_name):
        wd = self.app.wd
        return wd.find_element_by_xpath(
            "//header[@id='header']//a[@title='Просмотреть мою учетную запись покупателя']/span"
            ).text == ""+session_name+"" # выполняется проверка на соответствие имен

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            session_name = wd.find_element_by_xpath(
                "//header[@id='header']//a[@title='Просмотреть мою учетную запись покупателя']/span"
                ).text
            if self.is_logged_in_as(session_name):
                return
            else:
                self.logout()
        self.login(username, password)




