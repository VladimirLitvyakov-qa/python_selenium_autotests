import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.mark.xfail(reason='primer: nomer bug-reporta')
# каждый тест должен начинаться с test_
def test_check_faq(browser):
    """
    Test case WERT-2
    """
    # определяем адрес страницы для теста и переходим на неё
    url = "https://testqastudio.me/"
    browser.get(url=url)

    # ищем по селектору элемент
    element = browser.find_element(by=By.CSS_SELECTOR, value = '#menu-top [class*="menu-item-11088"]')
    # кликаем по нему
    element.click()

    assert browser.current_url == 'https://testqastudio.me/faq/', 'Unexpecte url'

    faq_menu2 = browser.find_element(by=By.XPATH, value = '//*[contains(text(), "Можно ли поставить доп.фурнитуру?")]')
    faq_menu2.click()

    assert True, ''

def test_product_view_sku(browser):
    """
    Test case WERT-2 
    """
    url = "https://testqastudio.me/"
    browser.get(url=url)
		# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    # чтобы просмотреть детали
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'BFB9ZOK210', "Unexpected sku"