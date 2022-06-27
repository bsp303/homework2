from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_1(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button, 'Отсутствует кнопка добавления в корзину на странице'