from behave import *
from BaseSuite import BaseSuite
from PageObjectBootstrapDownload import PageObjectBootstrapDownload
from WebDriverFactory import WebDriverFactory

driver = None
page_objects = None

@given('we\'re on the bootstrap download testing page')
def step_impl(context):
    global driver
    driver = BaseSuite(WebDriverFactory.E_browser.Firefox).get_webdriver()
    global page_objects
    page_objects = PageObjectBootstrapDownload(driver)

@when('we click on download button')
def step_impl(context):
    page_objects.downloadBtn.click()

@then('percents are incrementing')
def step_impl(context):
    assert page_objects.is_ascending() is True
    driver.close()
    driver.quit()