import time

import allure
from allure_commons.types import Severity
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "timofeevaao")
@allure.story("Клик на логотип 'latech' в левом верхнем углу")
def test_4(driver):
    page = MainPage(driver)
    page.open()
    page.click_our_projects()
    page.click_home()
    page.assert_url(page.get_current_url(), 'https://latech.ru/#main', 'Неверный URL')

