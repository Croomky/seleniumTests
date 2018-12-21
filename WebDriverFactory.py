from enum import Enum

from selenium import webdriver

class WebDriverFactory:
    E_browser = Enum('E_browser', 'Chrome Firefox IE')

    def __init__(self):
        pass

    def create_driver(self, browser: E_browser):
        if browser == self.E_browser.Chrome:
            #todo return chrome webdriver
            pass
        elif browser == self.E_browser.Firefox:
            #fixme provide proper path
            return webdriver.Firefox(executable_path='C:\\Users\\Konrad\\Documents\\Projects\\VSCode\\seleniumTests\\geckodriver.exe')
        elif browser == self.E_browser.IE:
            #todo return ie webdriver
            pass
        else:
            raise Exception('Unrecognized browser type')#fixme throw proper exception