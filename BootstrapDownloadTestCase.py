import unittest

from BaseSuite import BaseSuite
from PageObjectBootstrapDownload import PageObjectBootstrapDownload
from WebDriverFactory import WebDriverFactory

class BootstrapDownloadTestCase(unittest.TestCase):
    
    def test_download_bar(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectBootstrapDownload(driver)

            page_objects.downloadBtn.click()
            self.assertEqual(True, page_objects.is_ascending())