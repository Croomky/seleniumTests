from selenium import webdriver

class PageObjectTablePagination:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/table-pagination-demo.html')

        # table page objects
        self.supposed_records_amt = 15
        self.max_records_per_page = 5

        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[2]/a')
        /html/body/div[2]/div/div[2]/div/ul/li[3]/a
        /html/body/div[2]/div/div[2]/div/ul/li[4]/a

    def _get_array_of_pages(self):
