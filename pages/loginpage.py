from testdata.data import *
from pages.webgeneric import WebGeneric

class LoginPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self,driver)
        #self.driver = driver
        self.un = "username"
        self.pwd = "pwd"
        self.login = "//*[text()='Login ']"
        global wb
        wb=WebGeneric(driver)

    def enter_un(self):
        # self.driver.find_element_by_name(self.un).send_keys(UN)
       wb.enter(self.un, UN)

    def enter_pwd(self):
        # self.driver.find_element_by_name(self.pwd).send_keys(PWD)
        wb.enter(self.pwd, PWD)

    def click_login(self):
        # self.driver.find_element_by_xpath("//*[text()='Login ']").click()
        wb.click(self.login)
