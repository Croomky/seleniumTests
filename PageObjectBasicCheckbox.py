from selenium import webdriver

class PageObjectBasicCheckbox:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

        self.click_on_this_checkbox = self.driver.find_element_by_id('isAgeSelected')
        self.success_message = self.driver.find_element_by_xpath('//*[@id="txtAge"]')

        self.option_checkboxes = self.driver.find_elements_by_class_name('cb1-element')
        self.check_btn = self.driver.find_element_by_id('check1')