import allure
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _wait_and_get(self, locator, condition, action_name: str):
        logger.info("Ожидание '%s' для локатора: %s", action_name, locator)
        try:
            return self.wait.until(condition(locator))
        except TimeoutException:
            msg = f"Таймаут: не удалось {action_name} по локатору {locator}"
            logger.error(msg)
            raise AssertionError(msg)

    def wait_for_clickable(self, locator):
        with allure.step("Дождаться кликабельности"):
            return self._wait_and_get(locator, EC.element_to_be_clickable, action_name="ожидание кликабельности")

    def click_element(self, locator):
        with allure.step("Кликнуть на элемент"):
            logger.info("Выполнение клика по элементу: %s", locator)
            self.wait_for_clickable(locator).click()

    def wait_for_in_viewport(self, locator, timeout=10) -> bool:
        with allure.step("Дождаться появления элемента во вьюпорте"):
            logger.info("Ожидание появления элемента во вьюпорте: %s", locator)
            try:
                element = self.driver.find_element(*locator)
                WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script("""
                    const rect = arguments[0].getBoundingClientRect();
                    return (
                        rect.top >= 0 &&
                        rect.left >= 0 &&
                        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                    );
                """, element))
                return True
            except (TimeoutException, NoSuchElementException):
                return False

    def wait_for_invisible(self, locator):
        with allure.step("Дождаться исчезновения элемента"):
            logger.info("Ожидание исчезновения элемента: %s", locator)
            self._wait_and_get(locator, EC.invisibility_of_element_located, "исчезновение")

    def get_current_url(self) -> str:
        with allure.step("Получить текущий url"):
            return self.driver.current_url

    def assert_url(self, actual, expected, msg: str = ""):
        with allure.step("Сравнить url"):
            logger.info("Проверка: ожидается url '%s'", expected)
            if actual != expected:
                error_msg = f"{msg}\nОжидаемый url: '{expected}'\nФактический url: '{actual}'"
                logger.error(error_msg)
                raise AssertionError(error_msg)
            logger.info("Проверка успешна: '%s'", actual)

    def assert_visible_in_viewport(self, locator, msg: str = "Элемент не виден в текущем вьюпорте"):
        with allure.step("Проверить наличие элемента во вьюпорте"):
            logger.info("Проверка видимости элемента во вьюпорте: %s", locator)
            result = self.wait_for_in_viewport(locator)
            if not result:
                logger.error(msg)
                raise AssertionError(msg)
            logger.info("Элемент виден во вьюпорте: %s", locator)

    def assert_text_contains(self, locator, expected_text: str):
        with allure.step("Проверить наличие текста"):
            logger.info("Проверка наличия текста '%s' в элементе: %s", expected_text, locator)
            actual_text = self.driver.find_element(*locator).get_attribute("innerText")
            if expected_text not in actual_text:
                msg = f"Текст '{expected_text}' не найден. Фактический текст: '{actual_text}'"
                logger.error(msg)
                raise AssertionError(msg)
            logger.info("Текст '%s' найден успешно", expected_text)

    def switch_to_new_window(self):
        with allure.step("Перейти в соседнюю вкладку"):
            logger.info("Переключение на новое окно")
            self.wait.until(lambda d: len(d.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[-1])