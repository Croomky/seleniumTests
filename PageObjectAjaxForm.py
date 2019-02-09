from selenium import webdriver

class PageObjectAjaxForm:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/ajax-form-submit-demo.html')

        self.nameInput = self.driver.find_element_by_xpath('//*[@id="title"]')
        self.commentInput = self.driver.find_element_by_xpath('//*[@id="description"]')
        self.submitBtn = self.driver.find_element_by_xpath('//*[@id="btn-submit"]')
        self.submitControlDiv = self.driver.find_element_by_xpath('//*[@id="submit-control"]')

        