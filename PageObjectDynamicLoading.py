from selenium import webdriver

class PageObjectBootstrapModal:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/bootstrap-modal-demo.html')

        self.getNewUser = self.driver.find_element_by_id('save')
        self.userDiv = self.driver.find_element_by_id('loading')

        