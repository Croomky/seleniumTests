from selenium import webdriver
from Slider import Slider

class PageObjectRangeSliders:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/drag-drop-range-sliders-demo.html')

        self.sliders = [ Slider(self.driver, '//*[@id="slider' + str(i) + '"]') for i in range(1, 7) ]
    
    def is_default(self):
        for s in self.sliders:
            if s.defaultValue != s.get_output_value():
                return False

        return True
