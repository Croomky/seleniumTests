from selenium import webdriver

class PageObjectBootstrapDownload:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/bootstrap-download-progress-demo.html')

        self.downloadBtn = self.driver.find_element_by_xpath('//*[@id="cricle-btn"]')
        self.percent = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]')
    
    def is_ascending(self):
        isAscending = True
        oldPercent = 0

        while oldPercent != 100:
            self.percent = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]')
            percent = int(self.percent.text.strip('%'))
            if percent >= oldPercent:
                oldPercent = int(self.percent.text.strip('%'))
            else:
                isAscending = False
                return isAscending

        return isAscending