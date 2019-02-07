class BootstrapList:

    def __init__(self):
        self.items = []

    def initialize_left_list(self, driver):
        self.driver = driver
        # self.items = []
        self.items_xpath = '/html/body/div[2]/div/div[2]/div/div[1]/div/ul/li'
        self.checkAllBtn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/a')
        self.searchBar = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/input')

    def initialize_right_list(self, driver):
        self.driver = driver
        self.items_xpath = '/html/body/div[2]/div/div[2]/div/div[3]/div/ul/li'
        self.checkAllBtn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div/a')
        self.searchBar = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/input')

    def refresh_items(self):
        self.items = self.driver.find_elements_by_xpath(self.items_xpath)

    def get_items_quantity(self):
        self.refresh_items()
        return len(self.items)

    def check_items(self, indexesOfItemsToCheck):
        length = self.get_items_quantity()
        for i in indexesOfItemsToCheck:
            if i >= 0 and i < length:
                self.items[i].click()

    def check_all(self):
        self.checkAllBtn.click()

    def search_for_phrase(self, phrase):
        self.searchBar.send_keys(phrase)

    def get_number_of_active_items(self):
        self.refresh_items()
        activeItemsNumber = 0
        for i in self.items:
            if i.get_attribute('style').find('display: none;') == -1:
                activeItemsNumber += 1

        return activeItemsNumber