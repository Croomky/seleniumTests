from behave import *
from BaseSuite import BaseSuite
from PageObjectBasicCheckbox import PageObjectBasicCheckbox
from WebDriverFactory import WebDriverFactory

driver = None
page_objects = None

@given('user is on the basic checkbox testing page')
def step_impl(context):
    global driver
    driver = BaseSuite(WebDriverFactory.E_browser.Firefox).get_webdriver()
    global page_objects
    page_objects = PageObjectBasicCheckbox(driver)

@when('user selects and unselects single checkbox')
def step_impl(context):
    if not page_objects.click_on_this_checkbox.is_selected():
        page_objects.click_on_this_checkbox.click()
            
    assert page_objects.success_message.is_displayed() == True
    page_objects.click_on_this_checkbox.click()
    assert -1 != page_objects.success_message.get_attribute('style').find('none')

@then('success message appears and disappears')
def step_impl(context):
    assert -1 != page_objects.success_message.get_attribute('style').find('none')
    driver.close()
    driver.quit()

@when('user clicks on multiple checkboxes and unchecks them all')
def step_impl(context):
    for i in page_objects.option_checkboxes:
        assert page_objects.check_btn.get_attribute('value') == 'Check All'
        i.click()

@then('checkboxes are checked and unchecked')
def step_impl(context):
    assert page_objects.check_btn.get_attribute('value') == 'Uncheck All'
    driver.close()
    driver.quit()