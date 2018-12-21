from webdriver import WebDriverFactory

driver = WebDriverFactory().create_driver(WebDriverFactory.E_browser.Firefox)
driver.get('https://www.google.pl')