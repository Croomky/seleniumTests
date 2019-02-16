import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectDynamicData import PageObjectDynamicData
from WebDriverFactory import WebDriverFactory

class DynamicDataTestCase(unittest.TestCase):

    def test_load_user(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectDynamicData(driver)

            page_objects.getUserBtn.click()
            page_objects.wait_until_loaded()
            page_objects.is_name_loaded()
            self.assertEqual(page_objects.is_picture_loaded(), True)
            self.assertEqual(page_objects.is_name_loaded(), True)