from selenium.webdriver.common.action_chains import ActionChains

class Slider:
    def __init__(self, driver, sliderDiv):
        self.driver = driver
        self.sliderDiv = self.driver.find_element_by_xpath(sliderDiv)
        self.defaultValue = 0
        self.output = self.sliderDiv.find_element_by_xpath('.//div/output')
        self.input = self.sliderDiv.find_element_by_xpath('.//div/input')

    def set_input_to(self, value):
        if not (value >= 1 and value <= 100):
            print("input value has to be between 1 and 100")
            return

        # value /= 100
        xOffset = (self.input.size["width"] - 6) / 100 * value# - self.input.size["width"] / 2
        print(round(xOffset, 0))
        print(self.input.size)
        action = ActionChains(self.driver)
        action.perform()

        action.move_to_element_with_offset(self.input, int(xOffset), 0)
        action.perform()

        # action.move_by_offset(10, int(yOffset))
        # action.move_by_offset()
        # action.perform()

        action.click()
        action.perform()
        
    def get_output_value(self):
        self.output = self.sliderDiv.find_element_by_xpath('.//div/output')
        return int(self.output.text)

    def initialize_default_value(self):
        print(self.driver.find_element_by_xpath('.//h4').text)
        # print(self.defaultValue)