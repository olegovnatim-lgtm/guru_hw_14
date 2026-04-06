import logging
import allure
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

BASE_URL = "https://latech.ru/"


class MainPage(BasePage):
    # локаторы
    LOADER = ("xpath", "//div[contains(@class, 'nl_reploader_father')]")
    OUR_PROJECTS = ("xpath", "(//span[text()='Наши проекты'])[2]")
    EXPERTS_BLOCK = ("xpath", "//div[contains(text(), 'экспертов разрабатывают digital')]")
    ABOUT_COMPANY = ("xpath", "(//span[text()='О компании'])[2]")
    TEAMS_AND_VACANCIES = ("xpath", "(//span[text()='Команды и вакансии'])[2]")
    ALL_VACANCIES = ("xpath", "//span[text()='Все вакансии Lamoda']")
    HOME = ("xpath", "//a[@href='#main']")
    FOOTER_REQUISITES = ("xpath", "//div[@field='tn_text_1692867274653']")

    def open(self):
        with allure.step("Открыть главную страницу"):
            logger.info("Открытие главной страницы")
            self.driver.get(BASE_URL)
            self.wait_for_invisible(self.LOADER)
            return self

    def click_our_projects(self):
        with allure.step("В верхнем меню кликнуть на кнопку 'Наши проекты'"):
            self.click_element(self.OUR_PROJECTS)

    def click_about_company(self):
        with allure.step("В верхнем меню кликнуть на кнопку 'О компании'"):
            self.click_element(self.ABOUT_COMPANY)

    def click_all_vacancies(self):
        with allure.step("Кликнуть на кнопку 'Все вакансии Lamoda'"):
            self.click_element(self.ALL_VACANCIES)

    def click_home(self):
        with allure.step("Кликнуть на логотип 'latech' в левом верхнем углу"):
            self.click_element(self.HOME)

    def scroll_to_footer(self):
        with allure.step("Проскроллить страницу вниз до футера"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")