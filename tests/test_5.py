import allure
from allure_commons.types import Severity
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "timofeevaao")
@allure.story("Реквизиты компании в футере страницы")
def test_5(driver):
    page = MainPage(driver)
    page.open()
    page.scroll_to_footer()
    page.assert_visible_in_viewport(page.FOOTER_REQUISITES)
    page.assert_text_contains(page.FOOTER_REQUISITES, 'ООО "Ламода Тех"')
    page.assert_text_contains(page.FOOTER_REQUISITES, "ОГРН - 1227700637471")
    page.assert_text_contains(page.FOOTER_REQUISITES, "ИНН - 7734461512")
