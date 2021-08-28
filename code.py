"""Модуль с тестируемым кодом."""
import re


def valid_email(email: str) -> bool:
    """
    Check is email correct.

    :param email:
    :return: bool
    """
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def log(file_name: str, text: str) -> None:
    """
    Write log to file.

    :param file_name:
    :param text:
    """
    with open(file_name, "a+") as f_obj:
        f_obj.write(text)
