import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectBasicDropdown import PageObjectBasicDropdown
from WebDriverFactory import WebDriverFactory

class BasicDropdownTestCase(unittest.TestCase):

    # def test_choose_day(self):
    #     with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
    #         page_objects = PageObjectBasicDropdown(driver)

    #         daysToChoose = [7, 1, 4, 2, 1, 7]
    #         for day in daysToChoose:
    #             page_objects.select_day(day)
    #             # sleep(2)
    #             self.assertEqual(page_objects.daysOfWeek[day - 1], page_objects.get_choosen_day())
            
    def test_multi_selection(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBasicDropdown(driver)

            citiesToChoose = [1, 3, 5, 7, 3]
            page_objects.select_cities(citiesToChoose)
            # page_objects.selectFirstBtn.click()
            sleep(2)
            print(page_objects.get_selection_from_multi_select())

            # # print(page_objects.get_selection_from_multi_select())
            # page_objects.getAllBtn.click()
            # sleep(4)
            # self.assertEqual(len(citiesToChoose)-1, len(page_objects.get_selection_from_multi_select()))

            # choosenCities = page_objects.get_selection_from_multi_select()
            # for cityIndex in citiesToChoose:
            #     self.assertTrue(page_objects.get_city_name(cityIndex) in choosenCities)