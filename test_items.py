import time
from selenium.webdriver.common.by import By

def test_button_add_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

    assert len(button_add_to_basket) > 0, "The 'add to basket' button is not exists"

    time.sleep(3)
