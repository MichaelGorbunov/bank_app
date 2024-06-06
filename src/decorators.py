from typing import Any, Callable


def mprint(text: str, filename: str | None, cons: bool = True) -> None:
    """вспомогательная функция которая , в зависимости от переданных параметров выводит
    текст в консоль или в файл"""
    if cons is True:
        print(text)
    else:
        with open(filename, "w", encoding="UTF-8") as file:
            print(text, file=file)  # вызываем функцию print, вывод которой должен записаться в файл
            file.close()


def log(filename: str | None = None) -> Callable:
    """Декоратор log принимает один необязательный аргумент
    filename, который определяет путь к файлу, в который будут записываться логи. Если
    filename не задан, то логи будут выводиться в консоль. Если вызов функции закончился ошибкой,
     то записывается сообщение об ошибке и входные параметры функции."""

    def my_decorator(func: Any) -> Callable:
        # @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if filename is None:
                out_console = True
            else:
                out_console = False
            # print(f"Аргументы декоратора: {filename}")
            try:

                result = func(*args, **kwargs)
                mprint(f"{func.__name__} ok", filename, out_console)

                return result

            except Exception as e:
                mprint(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}", filename, out_console)

            # print("После выполнения функции")

        return wrapper

    return my_decorator
