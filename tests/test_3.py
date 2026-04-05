import allure
from allure_commons.types import Severity
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "timofeevaao")
@allure.story("Проверка кнопки 'Все вакансии Lamoda' в блоке 'Команды и вакансии'")
def test_3(driver):
    page = MainPage(driver)
    page.open()
    page.click_teams_and_vacancies()
    page.assert_visible_in_viewport(page.ALL_VACANCIES)
    page.click_all_vacancies()
    page.switch_to_new_window()
    page.assert_url(page.get_current_url(), "https://job.lamoda.ru/vacancies?city=none", "Неверный URL")
