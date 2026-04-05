import time

import allure
from allure_commons.types import Severity
from pages.main_page import MainPage


@allure.tag("latech")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "timofeevaao")
@allure.story("Переход к странице 'О компании'")
def test_2(driver):
    page = MainPage(driver)
    page.open()
    page.click_about_company()
    page.assert_url(page.get_current_url(), "https://latech.ru/about", "Неверный URL")
    time.sleep(5)
