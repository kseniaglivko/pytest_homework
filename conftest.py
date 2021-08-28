"""Модуль с параметрами конфигурации для тестов."""

import pytest


def pytest_addoption(parser):  # type: ignore
    """Добавление конфигурации логгирования."""
    parser.addoption(
        "--log", action="store", default="log.txt", help="Logging of tests."
    )


@pytest.fixture(scope="session")
def logger(request):  # type: ignore
    """Функция, позволяющая задать имя файла для записи логов."""
    return request.config.getoption("--log")
