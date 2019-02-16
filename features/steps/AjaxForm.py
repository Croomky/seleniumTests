from behave import *
from BaseSuite import BaseSuite
from PageObjectAjaxForm import PageObjectAjaxForm
from WebDriverFactory import WebDriverFactory

driver = None
page_objects = None

@given('user is on the ajax form testing page')
def step_impl(context):
    global driver
    driver = BaseSuite(WebDriverFactory.E_browser.Firefox).get_webdriver()
    global page_objects
    page_objects = PageObjectAjaxForm(driver)

@when('user enters nothing and clicks submit')
def step_impl(context):
    page_objects.commentInput.send_keys('Lorem ipsum...')
    page_objects.submitBtn.click()

@then('name field has red outline')
def step_impl(context):
    assert -1 != page_objects.nameInput.get_attribute('style').find('rgb(255, 0, 0)')
    driver.close()
    driver.quit()

@when('user enters data and clicks submit')
def step_impl(context):
    page_objects.nameInput.send_keys('Joe')
    page_objects.commentInput.send_keys('Lorem ipsum...')
    page_objects.submitBtn.click()

@then('ajax is processing info')
def step_impl(context):
    assert -1 != page_objects.submitControlDiv.text.find('Ajax Request is Processing!')
    driver.close()
    driver.quit()