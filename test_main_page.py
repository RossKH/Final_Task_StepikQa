from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    try:
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert button is not None, "Кнопка не найдена на странице"
    except NoSuchElementException:
        assert False, "Кнопка не найдена на странице"