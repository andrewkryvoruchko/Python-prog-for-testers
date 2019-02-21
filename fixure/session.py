


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

