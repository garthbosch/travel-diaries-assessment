from json import load
import pytest
from lib.selenumWebdriverUtil import WebDriver
import chromedriver_autoinstaller
import os


@pytest.fixture(scope="module")
def env_setup(data_setup):
    global driver
    chromedriver_autoinstaller.install()
    driver = WebDriver()
    url = data.get("url")
    driver.maximize_window()
    driver.get(url)
    yield
    driver.close()


@pytest.fixture(scope="module")
def data_setup():
    global data
    global locators
    global path

    path = os.getcwd()

    with open(file=path + "/env/environment.json") as f:
        data = load(f)

    with open(file=path + "/page_objects/shared_page_objects.json") as f:
        locators = load(f)


def test_send_contact_form(env_setup, data_setup):
    """ Navigate to contact us page """
    home_locators = locators.get("home")
    driver.click_element(locator=home_locators.get("contact_us_link"))

    # Verify Customer service heading on contact us page
    contact_us_locators = locators.get("contact_us")
    result = driver.is_element_displayed(locator=contact_us_locators.get("contact_box"))
    assert result is True
    image_location = data.get("reports")
    driver.save_screenshot(path + image_location + "navigate_contact_us.png")

    # Enter contact us details
    driver.enter_text(locator=contact_us_locators.get("name_textbox"), value="Charles  Pitautel")
    driver.enter_text(locator=contact_us_locators.get("email_textbox"), value="CharlesPitautel@test.com")
    driver.enter_text(locator=contact_us_locators.get("message_textbox"), value="Automation Test using Python and Selenium")
    driver.click_element(locator=contact_us_locators.get("send_message_button"))
    driver.save_screenshot(path + image_location + "contact_us_completed.png")
