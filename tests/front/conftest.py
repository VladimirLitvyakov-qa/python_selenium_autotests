import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    """
    Test case Открываем браузер
    """
	# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
    chrome_options.add_argument("--disable-gpu") # отключение использования графического процессора
    chrome_options.add_argument("--disable-dev-shm-usage") # используется для отключения использования /dev/shm веб-драйвером при работе с браузером

    # устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()