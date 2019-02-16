from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class PageObjectBasicDropdown:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')

        self.daySelect = self.driver.find_element_by_xpath('//*[@id="select-demo"]')
        self.daysOptionsXpath = '/html/body/div[2]/div/div[2]/div[1]/div[2]/select/option'
        self.choosenDayXpath = '/html/body/div[2]/div/div[2]/div[1]/div[2]/p[2]'
        self.daysOfWeek = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]

        self.multiSelectXpath = '//*[@id="multi-select"]'
        self.selectFirstBtn = self.driver.find_element_by_xpath('//*[@id="printMe"]')
        self.getAllBtn = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    
    def select_day(self, day):
        if not (day >= 1 and day <= 7):
            print('day has to be number between 1 and 7')
            return

        self.daySelect.click()
        self.driver.find_element_by_xpath(self.daysOptionsXpath + "[text()='" + self.daysOfWeek[day-1] + "']").click()

    def get_choosen_day(self):
        return self.driver.find_element_by_xpath(self.choosenDayXpath).text.split(' ')[-1]

    def select_cities(self, citiesArray):
        actionChain = ActionChains(self.driver)
        actionChain.key_down(Keys.CONTROL).perform()
        for city in citiesArray:
            if not (city >= 0 and city <= 7):
                print('City index has to be a number between 0 and 7')
                break

            self.driver.find_element_by_xpath(self.multiSelectXpath + '/option[' + str(city) + ']').click()
        
        actionChain.key_up(Keys.CONTROL).perform()

    def get_selection_from_multi_select(self):
        selectionString = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/p[2]').text
        print('selectionString: ' + selectionString)
        return selectionString.split(' ')[-1].split(',')

    def get_city_name(self, index):
        if not (index >= 0 and index <= 7):
            print('City index has to be a number between 0 and 7')
            return
        
        return self.driver.find_element_by_xpath(self.multiSelectXpath + '/option[' + index + ']').text