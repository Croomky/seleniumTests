from selenium import webdriver

class PageObjectTablePagination:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.get('https://www.seleniumeasy.com/test/table-pagination-demo.html')

        # table page objects
        self.supposed_records_amt = 15
        self.max_records_per_page = 5

        self.previous_page_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[1]/a')
        self.next_page_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[5]/a')
        self.pages_btn = [
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[' + str(i) + ']/a')
            for i in range(2, 5)
        ]

    def get_visible_rows_amount(self):
        return len(self.driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/section/div/table/tbody/tr[contains(@style, \'display: table-row\')]'))

    def get_all_rows_amount(self):
        return len(self.driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/section/div/table/tbody/tr'))