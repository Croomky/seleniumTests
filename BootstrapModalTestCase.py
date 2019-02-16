import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectBootstrapModal import PageObjectBootstrapModal
from WebDriverFactory import WebDriverFactory

class BootstrapModalTestCase(unittest.TestCase):

    def test_open_save_single_modal(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBootstrapModal(driver)

            page_objects.singleModalBtn.click()
            self.assertNotEqual(-1, page_objects.singleModal.get_attribute('class').find('in'))

            page_objects.singleModalSaveChangesBtn.click()
            page_objects.refresh()
            self.assertEqual(-1, page_objects.singleModal.get_attribute('class').find('in'))

    def test_open_close_single_modal(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBootstrapModal(driver)

            page_objects.singleModalBtn.click()
            self.assertNotEqual(-1, page_objects.singleModal.get_attribute('class').find('in'))

            page_objects.singleModalCloseBtn.click()
            self.assertEqual(-1, page_objects.singleModal.get_attribute('class').find('in'))

    def test_open_save_multiple_modal(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBootstrapModal(driver)

            page_objects.multipleModalBtn.click()
            self.assertNotEqual(-1, page_objects.multipleModal.get_attribute('class').find('in'))

            page_objects.multipleModalSaveChangesBtn.click()
            page_objects.refresh()
            self.assertEqual(-1, page_objects.multipleModal.get_attribute('class').find('in'))

    def test_open_close_multiple_modal(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBootstrapModal(driver)

            page_objects.multipleModalBtn.click()
            self.assertNotEqual(-1, page_objects.multipleModal.get_attribute('class').find('in'))

            page_objects.multipleModalCloseBtn.click()
            self.assertEqual(-1, page_objects.multipleModal.get_attribute('class').find('in'))

    def test_open_save_small_modal(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBootstrapModal(driver)

            page_objects.multipleModalBtn.click()
            page_objects.multipleModalLaunchModalBtn.click()
            self.assertNotEqual(-1, page_objects.smallModal.get_attribute('class').find('in'))
            
            page_objects.smallModalSaveChangesBtn.click()
            page_objects.refresh()
            self.assertEqual(-1, page_objects.smallModal.get_attribute('class').find('in'))

    def test_open_close_small_modal(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBootstrapModal(driver)

            page_objects.multipleModalBtn.click()
            page_objects.multipleModalLaunchModalBtn.click()
            self.assertNotEqual(-1, page_objects.smallModal.get_attribute('class').find('in'))
            
            page_objects.smallModalCloseBtn.click()
            self.assertEqual(-1, page_objects.smallModal.get_attribute('class').find('in'))

            while not page_objects.multipleModalCloseBtn.is_displayed():
                pass
            page_objects.multipleModalCloseBtn.click()
            self.assertEqual(-1, page_objects.multipleModal.get_attribute('class').find('in'))
