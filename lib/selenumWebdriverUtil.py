import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class WebDriver(webdriver.Chrome):
    """
    Inherit WebDriver
    """

    def __init__(self, **kwargs):
        super(WebDriver, self).__init__(**kwargs)

    @staticmethod
    def get_locator(locator):
        """ Take in element locators as string and parse it to it's by object """
        try:
            locator_type, locator_value = locator
        except AttributeError as e:
            raise NoSuchElementException(e)
        except ValueError as e:
            raise NoSuchElementException(e)

        locator_type = getattr(By, locator_type.upper())
        return locator_type, locator_value

    def visibility_of_element(self, driver, locator, wait):
        """ Check if an element is visible """

        locator_type, locator_value = self.get_locator(locator)
        try:
            element = WebDriverWait(driver, wait).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException as e:
            raise NoSuchElementException(e)

    def find_element_by_locator(self, locator):
        """ Find an element by the passed BY locator """

        locator_type, locator_value = self.get_locator(locator)
        try:
            is_element_clickable = WebDriverWait(self, 20).until(EC.element_to_be_clickable((locator_type, locator_value)))
            if is_element_clickable:
                element = self.find_element(locator_type, locator_value)
        except AttributeError:
            raise NoSuchElementException('Invalid locator: {0}'.format(locator_type))
        return element

    def find_elements_by_locator(self, locator):
        """ Find elements by the passed BY locator """

        locator_type, locator_value = self.get_locator(locator)
        try:
            elements = self.find_elements(locator_type, locator_value)
        except AttributeError:
            raise NoSuchElementException('Invalid locator: {0}'.format(locator_type))
        return [element for element in elements]

    def select_by_text(self, locator, text):
        """ Select a value from a drop down list from the given text """

        select = Select(self.find_element_by_locator(locator))
        return select.select_by_visible_text(text)

    def is_element_present(self, locator):
        """ Verify if an element is present """

        try:
            self.find_element_by_locator(locator)
            return True
        except NoSuchElementException:
            return False



    def click_element(self, locator):
        self.find_element_by_locator(locator).click()

    def enter_text(self, locator, value):
        self.find_element_by_locator(locator).send_keys(value)

    def is_element_displayed(self, locator):
        return self.find_element_by_locator(locator).is_displayed()
