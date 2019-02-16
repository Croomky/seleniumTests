from behave import *
from BaseSuite import BaseSuite
from PageObjectSimpleForm import PageObjectSimpleForm
from WebDriverFactory import WebDriverFactory
from time import sleep

driver = None
page_objects = None
message = 'Humpty Dumpty sat on a wall...'

@given('user is on the simple form testing page')
def step_impl(context):
    global driver
    driver = BaseSuite(WebDriverFactory.E_browser.Firefox).get_webdriver()
    global page_objects
    page_objects = PageObjectSimpleForm(driver)

@when('user enters data to the first form and clicks show message')
def step_impl(context):
    page_objects.single_input_message_field.send_keys(message)
    page_objects.show_message_btn.click()

@then('message is showed')
def step_impl(context):
    assert message == page_objects.message_span.text
    driver.close()
    driver.quit()

@when('user enters data to the second form and clicks get total')
def step_impl(context):
    page_objects.single_input_message_field.send_keys(message)
    page_objects.show_message_btn.click()

@then('sum is showed')
def step_impl(context):
    assert message == page_objects.message_span.text
    driver.close()
    driver.quit()