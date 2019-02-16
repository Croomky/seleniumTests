from selenium import webdriver

class PageObjectBootstrapModal:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/bootstrap-modal-demo.html')

        self.singleModalBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a')
        self.multipleModalBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/a')

        self.singleModalSaveChangesBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[4]/a[2]')
        self.singleModalCloseBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[4]/a[1]')

        self.multipleModalSaveChangesBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[4]/a[2]')
        self.multipleModalCloseBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[4]/a[1]')
        self.multipleModalLaunchModalBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[3]/a')

        self.smallModalSaveChangesBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[6]/a[2]')
        self.smallModalCloseBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[6]/a[1]')
    
        self.singleModal = self.driver.find_element_by_id('myModal0')
        self.multipleModal = self.driver.find_element_by_id('myModal')
        self.smallModal = self.driver.find_element_by_id('myModal2')

    def refresh(self):
        self.__init__(self.driver)