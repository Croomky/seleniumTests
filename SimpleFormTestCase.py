import unittest
from time import sleep

from BaseSuite import BaseSuite
from PageObjectSimpleForm import PageObjectSimpleForm
from WebDriverFactory import WebDriverFactory

class SimpleFormTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_single_form(self):
        with BaseSuite(WebDriverFactory.E_browser.Firefox) as driver:
            po_simple_form = PageObjectSimpleForm(driver)

            message = 'Humpty Dumpty sat on a wall...'
            po_simple_form.single_input_message_field.send_keys(message)
            po_simple_form.show_message_btn.click()

            self.assertEqual(message, po_simple_form.message_span.text)

            a, b = 2, 3
            po_simple_form.two_input_a_field.send_keys(str(a))
            po_simple_form.two_input_b_field.send_keys(str(b))

            po_simple_form.get_total_btn.click()

            self.assertEqual(str(a + b), po_simple_form.total_span.text)
