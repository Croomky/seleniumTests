import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectDualListBox import PageObjectDualListBox
from WebDriverFactory import WebDriverFactory

class DualListBoxTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_check_all_and_throw_right(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectDualListBox(driver)

            page_objects.leftList.check_all()
            right_list_items_quantity = page_objects.rightList.get_items_quantity()
            left_list_items_quantity = page_objects.leftList.get_items_quantity()
            page_objects.throwRightBtn.click()

            self.assertEqual(right_list_items_quantity
                            + left_list_items_quantity,
                            page_objects.rightList.get_items_quantity())
            
    def test_check_some_and_throw_left(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectDualListBox(driver)
            items_to_check = [1, 3]

            right_list_items_quantity = page_objects.rightList.get_items_quantity()
            left_list_items_quantity = page_objects.leftList.get_items_quantity()
            page_objects.rightList.check_items(items_to_check)

            page_objects.throwLeftBtn.click()

            self.assertEqual(right_list_items_quantity - 2,
                            page_objects.rightList.get_items_quantity())
            
            self.assertEqual(left_list_items_quantity + 2,
                            page_objects.leftList.get_items_quantity())

    def test_search_bar(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            page_objects = PageObjectDualListBox(driver)

            page_objects.leftList.search_for_phrase('b')
            self.assertEqual(4, page_objects.leftList.get_number_of_active_items())

            page_objects.leftList.search_for_phrase('o')
            self.assertEqual(1, page_objects.leftList.get_number_of_active_items())

            page_objects.rightList.search_for_phrase('c')
            self.assertEqual(3, page_objects.rightList.get_number_of_active_items())

            page_objects.rightList.search_for_phrase('r')
            self.assertEqual(1, page_objects.rightList.get_number_of_active_items())
