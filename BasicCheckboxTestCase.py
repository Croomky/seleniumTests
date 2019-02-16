import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectBasicCheckbox import PageObjectBasicCheckbox
from WebDriverFactory import WebDriverFactory

class BasicCheckboxTestCase(unittest.TestCase):
    def test_single_checkbox(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBasicCheckbox(driver)

            if not page_objects.click_on_this_checkbox.is_selected():
                page_objects.click_on_this_checkbox.click()
            
            self.assertTrue(page_objects.success_message.is_displayed())
            page_objects.click_on_this_checkbox.click()
            self.assertNotEqual(-1, page_objects.success_message.get_attribute('style').find('none'))

    def test_multiple_checkboxes(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBasicCheckbox(driver)

            for i in page_objects.option_checkboxes:
                self.assertEqual(page_objects.check_btn.get_attribute('value'), 'Check All')
                i.click()
            
            self.assertEqual(page_objects.check_btn.get_attribute('value'), 'Uncheck All')
