import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectRangeSliders import PageObjectRangeSliders
from WebDriverFactory import WebDriverFactory

class RangeSlidersTestCase(unittest.TestCase):

    def test_(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectRangeSliders(driver)

            page_objects.sliders[0].set_input_to(3)
            print(page_objects.sliders[0].get_output_value())
            sleep(1)
