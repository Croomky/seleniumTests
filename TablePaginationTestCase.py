import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectTablePagination import PageObjectTablePagination
from WebDriverFactory import WebDriverFactory

class SimpleFormTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_single_form(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectTablePagination(driver)

            self.assertNotEqual(-1, page_objects.previous_page_btn.get_attribute('style').find('display: none;'))
            self.assertEqual('', page_objects.next_page_btn.get_attribute('style'))

            page_objects.pages_btn[-1].click()

            self.assertNotEqual(-1, page_objects.previous_page_btn.get_attribute('style').find('display: block;'))
            self.assertNotEqual(-1, page_objects.next_page_btn.get_attribute('style').find('display: none;'))

            for i in page_objects.pages_btn:
                i.click()
                self.assertLessEqual(page_objects.get_visible_rows_amount(), page_objects.max_records_per_page)

            self.assertEqual(page_objects.supposed_records_amt, page_objects.get_all_rows_amount())
