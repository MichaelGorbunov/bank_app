# from src.decorators import log, mprint
#
#
# # mprint(text: str, filename: str | None, cons: bool = True) -> None:
# def test_mprint_out_console(capsys):
#     mprint("123456", None, True)
#     out, err = capsys.readouterr()
#
#     assert out == "123456\n"
#
#
# def test_mprint_out_file():
#     mprint("123456", "myfile.txt", False)
#     with open("myfile.txt", "r") as file:
#         log_content = file.read()
#     assert "123456" in log_content
#     # assert "test_func ok" in log_conten
#
#
# @log(filename="myfile.txt")
# def my_function(x, y):
#     return x + y
#
#
# def test_log_file():
#     my_function(1, 1)
#     with open("myfile.txt", "r") as file:
#         log_content = file.read()
#     assert "my_function ok" in log_content
#
#
# @log()
# def my_function3(x, y):
#     return x + y
#
#
# def test_log_console(capsys):
#     my_function3(1, 1)
#     captured = capsys.readouterr()
#     assert captured.out == "my_function3 ok\n"
#
#
# my_function3(1, 1)
#
#
# @log("myfile.txt")
# def my_function1(x, y):
#     return x / y
#
#
# def test_log_file_err():
#     my_function1(1, 0)
#     with open("myfile.txt", "r") as file:
#         log_content = file.read()
#     assert "my_function1 error: division by zero. Inputs: (1, 0), {}" in log_content
#
#
# @log()
# def my_function2(x, y):
#     return x / y
#
#
# def test_log_console_err2(capsys):
#     my_function2(1, 0)
#     captured = capsys.readouterr()
#     assert captured.out == "my_function2 error: division by zero. Inputs: (1, 0), {}\n"
#
#
# my_function2(1, 0)
#
#
# def test_output(capsys):
#     print("hello")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
import os

import pytest

# from src.decorators import log, retry, unstable_function
from src.decorators import log

# from unittest.mock import call, patch


def test_log_to_file():
    @log(filename="testlog.txt")
    def sample_function(x, y):
        return x + y

    result = sample_function(1, 2)
    assert result == 3

    with open("testlog.txt", "r") as file:
        lines = file.readlines()

    assert len(lines) == 1
    assert "sample_function ok" in lines[0]

    os.remove("testlog.txt")


def test_log_error_to_file():
    @log(filename="errorlog.txt")
    def error_function(x, y):
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        error_function(1, 2)

    with open("errorlog.txt", "r") as file:
        lines = file.readlines()

    assert len(lines) == 1
    assert "error_function error: ValueError. Inputs: (1, 2), {}" in lines[0]

    os.remove("errorlog.txt")


def test_log_to_console(capsys):
    @log()
    def console_function(x, y):
        return x * y

    result = console_function(2, 3)
    assert result == 6

    captured = capsys.readouterr()
    assert "console_function ok" in captured.out


def test_log_error_to_console(capsys):
    @log()
    def console_error_function(x, y):
        raise IndexError("Console test error")

    with pytest.raises(IndexError, match="Console test error"):
        console_error_function(2, 3)

    captured = capsys.readouterr()
    assert "console_error_function error: IndexError. Inputs: (2, 3), {}" in captured.out


# @pytest.fixture
# def decorated_unstable_function():
#     return retry(max_attempts=5)


# def test_retry_success_after_failures(decorated_unstable_function):
#     with patch(
#         "decorators.unstable_function", side_effect=[ConnectionError, ConnectionError, "Success!"]
#     ) as mock_func:
#         decorated_func = decorated_unstable_function(mock_func)
#         result = decorated_func()
#         assert result == "Success!"
#         assert mock_func.call_count == 3


# def test_retry_exceeds_max_retries(decorated_unstable_function):
#     with patch("decorators.unstable_function", side_effect=ConnectionError) as mock_func:
#         decorated_func = decorated_unstable_function(mock_func)
#         with pytest.raises(ConnectionError):
#             decorated_func()
#         assert mock_func.call_count == 5


# def test_retry_waits_between_attempts(decorated_unstable_function):
#     with patch("decorators.unstable_function", side_effect=ConnectionError) as mock_func, patch(
#         "time.sleep", return_value=None
#     ) as sleep_mock:
#         decorated_func = decorated_unstable_function(mock_func)
#         with pytest.raises(ConnectionError):
#             decorated_func()
#         assert mock_func.call_count == 5
#         assert sleep_mock.call_count == 5
#         sleep_mock.assert_has_calls([call(1), call(1), call(1), call(1)])
