class WebGeneric:
    def __init__(self,driver):
        self.driver=driver

    def enter(self,locator,input_val):
        #self.driver.find_element_by_name(locator).send_keys(input_val)
        ele.send_keys(input_val)
    def click(self,locator):
        self.driver.find_element_by_xpath(locator).click()