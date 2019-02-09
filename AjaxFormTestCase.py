import unittest
# from time import sleep

from BaseSuite import BaseSuite
from PageObjectAjaxForm import PageObjectAjaxForm
from WebDriverFactory import WebDriverFactory

class AjaxFormTestCase(unittest.TestCase):

    def test_empty_name(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectAjaxForm(driver)

            page_objects.commentInput.send_keys('Lorem ipsum...')
            page_objects.submitBtn.click()

            self.assertNotEqual(-1, page_objects.nameInput.get_attribute('style').find('rgb(255, 0, 0)'))

    def test_submit_disappear(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectAjaxForm(driver)

            page_objects.nameInput.send_keys('Joe')
            page_objects.commentInput.send_keys('Lorem ipsum...')
            page_objects.submitBtn.click()

            self.assertNotEqual(-1,
                    page_objects.submitControlDiv.text.find('Ajax Request is Processing!'))