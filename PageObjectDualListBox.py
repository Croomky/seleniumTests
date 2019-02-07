from selenium import webdriver
from BootstrapList import BootstrapList

class PageObjectDualListBox:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/bootstrap-dual-list-box-demo.html')

        self.leftList = BootstrapList()
        self.leftList.initialize_left_list(driver)
        self.rightList = BootstrapList()
        self.rightList.initialize_right_list(driver)

        self.throwRightBtn = self.driver.find_element_by_class_name('move-right')
        self.throwLeftBtn = self.driver.find_element_by_class_name('move-left')
