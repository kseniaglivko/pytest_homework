"""Модуль с тестами."""
from typing import Any

from code import valid_email, log
import pytest


class TestEmail:

    @pytest.mark.parametrize("email", ("test@test.ru", "test@test.", "w@w.com", "w@", "123QWE@mmm.mmm", "@tt"))
    def test_valid_email(self, email: str, logger: Any) -> None:
        if valid_email(email):
            log(logger, email + ": passed test_valid_email.\n")
        else:
            log(logger, email + ": failed test_valid_email.\n")

    @pytest.mark.xfail
    @pytest.mark.parametrize("email", ("test@test.ru", "test@test.", "w@w.com", "w@", "123QWE@mmm.mmm", "@tt"))
    def test_invalid_email(self, email: str, logger: Any) -> None:
        if valid_email(email):
            log(logger, email + ": failed test_invalid_email.\n")
        else:
            log(logger, email + ": passed test_invalid_email.\n")
