import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib3.util import url
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url

def test_git_hub_web(driver):
    url_git = "https://github.com/"
    driver.get(url_git)
    assert driver.title.startswith("GitHub")
    assert driver.current_url == url_git


def test_Google(driver):
    url_goole = "https://www.google.com/"
    driver.get(url_goole)  # открываем страницу гугл
    assert driver.title.startswith("Goo")  # проверка что заголовка гугл
    assert driver.current_url == url_goole # проверка что адерс совпал
    search_field = driver.find_element(By.CSS_SELECTOR, '[title="Поиск"]')  # находим поле поиска
    search_field.send_keys("qa guru" + Keys.ENTER)
    qa_guru_link = driver.find_element(By.PARTIAL_LINK_TEXT, "qa.guru") # Проверяем что есть ссылка на qa.guru

