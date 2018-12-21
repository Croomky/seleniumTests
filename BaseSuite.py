
from WebDriverFactory import WebDriverFactory

class BaseSuite:
    
    def __init__(self, browser: WebDriverFactory.E_browser):
        self._webdriver_factory = WebDriverFactory()
        self.webdriver = self._webdriver_factory.create_driver(WebDriverFactory.E_browser.Firefox)

    def __enter__(self):
        return self.webdriver

    def __exit__(self, exception_type, exception_value, traceback):
        self.webdriver.close()
        self.webdriver.quit()