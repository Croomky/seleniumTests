from behave import *
from BaseSuite import BaseSuite
from PageObjectDynamicData import PageObjectDynamicData
from WebDriverFactory import WebDriverFactory

driver = None
page_objects = None

@given('user is on the dynamic data loading testing page')
def step_impl(context):
    global driver
    driver = BaseSuite(WebDriverFactory.E_browser.Firefox).get_webdriver()
    global page_objects
    page_objects = PageObjectDynamicData(driver)

@when('user clicks get new user button')
def step_impl(context):
    page_objects.getUserBtn.click()
    page_objects.wait_until_loaded()
    page_objects.is_name_loaded()

@then('new user is loaded')
def step_impl(context):
    assert page_objects.is_picture_loaded() == True
    assert page_objects.is_name_loaded() == True
    driver.close()
    driver.quit()
