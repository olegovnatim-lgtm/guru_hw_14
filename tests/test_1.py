import allure
from allure_commons.types import Severity
from pages.main_page import MainPage


@allure.tag("latech")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "timofeevaao")
@allure.story("Проверка на автоматическую прокрутку к соответствующему блоку после нажатия на кнопку 'Наши проекты'")
def test_1(driver):
    page = MainPage(driver)
    page.open()
    page.click_our_projects()
    page.assert_visible_in_viewport(page.EXPERTS_BLOCK)
