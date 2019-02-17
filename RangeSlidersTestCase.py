import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectRangeSliders import PageObjectRangeSliders
from WebDriverFactory import WebDriverFactory

class RangeSlidersTestCase(unittest.TestCase):

    def test_default_values(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectRangeSliders(driver)

            for slider in page_objects.sliders:
                self.assertTrue(page_objects.is_default())
