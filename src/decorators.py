import os

# from functools import wraps


# def log(filename: str | None = None) -> None:
#     if filename is None:
#         print("hi")
#     else:
#         if os.path.isfile(filename):
#             def wrapper(*args,**kwargs):
#                 result=func
#                 with open(filename, 'w',encoding="UTF-8") as file:
#                     file.write('Hello, Python!')
#                     file.close()
#                 return result
#             return wrapper
#             print("Файл существует")
#         else:
#             print("Файл не существует")
def mprint(text, cons: bool = True):
    if cons is True:
        print(text)
    else:
        with open("myfile.txt", "w", encoding="UTF-8") as file:
            print(text, file=file)  # вызываем функцию print, вывод которой должен записаться в файл
            file.close()


def decorator_with_args(filename: str | None = None) -> None:

    def my_decorator(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            # print(f"Аргументы декоратора: {filename}")
            try:
                result = func(*args, **kwargs)
                mprint(f"{func.__name__} ok", False)
                return result

            except Exception as e:
                mprint(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}", False)

            # print("После выполнения функции")

        return wrapper

    return my_decorator


@decorator_with_args(filename="myfile.txt")
def my_function1(x, y):
    # print(f"Выполнение функции с аргументами {x} и {y}")
    return x / y


print(my_function1(10, 0))

# @log(filename="myfile.txt")
# def my_function(x, y):
#     return x + y
#
# print(my_function(1, 2))
# try:
#     for i in range(3):
#         print(3/i)
# except:
#     print("Деление на 0")
#     print("Исключение было обработано")


# mprint(f"qweq{1+1}eqweq",False)#

# import os создать файл если его не существует
# if not os.path.exists('file'):
#     open('file', 'w').close()