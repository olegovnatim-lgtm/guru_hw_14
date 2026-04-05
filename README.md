# Автотесты для сайта latech.ru

## Технологии

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.41-green)
![Pytest](https://img.shields.io/badge/Pytest-9.0-orange)
![Allure](https://img.shields.io/badge/Allure-2.15-yellow)
![Selenoid](https://img.shields.io/badge/Selenoid-remote-lightgrey)

## Структура проекта

```
├── pages/
│   ├── base_page.py      # базовые методы (клики, ожидания, assert'ы)
│   └── main_page.py      # локаторы и методы главной страницы
├── tests/
│   ├── test_1.py         # прокрутка к блоку "Наши проекты"
│   ├── test_2.py         # переход на страницу "О компании"
│   ├── test_3.py         # кнопка "Все вакансии Lamoda"
│   ├── test_4.py         # клик на логотип latech
│   └── test_5.py         # реквизиты компании в футере
├── logs/                 # логи тестов
├── attach.py             # аттачменты для Allure
├── conftest.py           # фикстуры и конфигурация
└── requirements.txt      # зависимости
```

## Тест-кейсы

| Тест | Описание | Severity |
|------|----------|----------|
| test_1 | Проверка автоматической прокрутки к соответствующему блоку после нажатия на кнопку "Наши проекты" | Critical |
| test_2 | Переход к странице "О компании" и проверка URL | Critical |
| test_3 | Проверка кнопки "Все вакансии Lamoda" и переход на job.lamoda.ru | Critical |
| test_4 | Клик на логотип latech возвращает на главную страницу | Normal |
| test_5 | Проверка наличия реквизитов компании в футере страницы | Normal |

## Установка и запуск

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск всех тестов
```bash
pytest
```
> Параметры `--alluredir` и `--clean-alluredir` заданы в `pytest.ini` и применяются автоматически.

### Запуск конкретного теста

```bash
pytest tests/test_1.py 
```

### Просмотр Allure отчёта

```bash
allure serve allure-results
```

## Запуск в CI/CD

Тесты запускаются автоматически через **Jenkins**.  
Браузер поднимается удалённо через **Selenoid** с включённой записью видео и VNC.

## Allure отчёт

Каждый тест содержит следующие аттачменты:
- 📸 Скриншот
  ![Скриншот теста](images_md/img.png)
- 📄 Исходный код страницы
- 📋 Логи браузера
- 🎥 Запись видео выполнения теста
  ![Запись теста](images_md/video.gif)
