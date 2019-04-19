from testdata.data import *
from pages.webgeneric import WebGeneric


class LoginPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        # self.driver = driver
        self.un = "j_username"
        self.pwd = "j_password"
        self.login = "//*[text()='Login ']"
        global wb
        wb = WebGeneric(driver)

    def enter_un(self):
        # self.driver.find_element_by_name(self.un).send_keys(UN)
        # wb.enter(self.un, UN)
        wb.enter('id', self.un, 'admin')

    def enter_pwd(self):
        # self.driver.find_element_by_name(self.pwd).send_keys(PWD)
        # wb.enter(self.pwd, PWD)
        wb.enter('name', self.pwd, 'manager')

    def click_login(self):
        # self.driver.find_element_by_xpath("//*[text()='Login ']").click()
        # wb.click(self.login)
        wb.click('id', self.login)
