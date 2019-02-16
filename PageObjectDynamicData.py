from selenium import webdriver
from time import sleep

class PageObjectDynamicData:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html')

        self.getUserBtn = self.driver.find_element_by_xpath('//*[@id="save"]')
        self.dataDiv = self.driver.find_element_by_xpath('//*[@id="loading"]')

    def is_picture_loaded(self):
        return self.dataDiv.find_element_by_xpath('img').is_displayed()

    def wait_until_loaded(self):
        while self.dataDiv.text.find('loading...') != -1:
            pass

        sleep(1)
        return

    def is_name_loaded(self):
        return len(self.dataDiv.text.split(' ')) == 7
