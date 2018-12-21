from selenium import webdriver

class PageObjectSimpleForm:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

        # single input form
        self.single_input_message_field = self.driver.find_element_by_xpath('//*[@id="user-message"]')
        self.show_message_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
        self.message_span = self.driver.find_element_by_xpath('//*[@id="display"]')

        # two input form
        self.two_input_a_field = self.driver.find_element_by_xpath('//*[@id="sum1"]')
        self.two_input_b_field = self.driver.find_element_by_xpath('//*[@id="sum2"]')
        self.get_total_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
        self.total_span = self.driver.find_element_by_xpath('//*[@id="displayvalue"]')
    