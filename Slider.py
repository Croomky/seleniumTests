from selenium.webdriver.common.action_chains import ActionChains

class Slider:
    def __init__(self, driver, sliderDiv):
        self.driver = driver
        self.sliderDiv = self.driver.find_element_by_xpath(sliderDiv)
        self.defaultValue = 0
        self.output = self.sliderDiv.find_element_by_xpath('.//div/output')
        self.input = self.sliderDiv.find_element_by_xpath('.//div/input')
        self.initialize_default_value()
        
    def get_output_value(self):
        self.output = self.sliderDiv.find_element_by_xpath('.//div/output')
        return int(self.output.text)

    def initialize_default_value(self):
        # print(self.sliderDiv.find_element_by_xpath('.//h4').text.split(' ')[2])
        self.defaultValue = int(self.sliderDiv.find_element_by_xpath('.//h4').text.split(' ')[2])
