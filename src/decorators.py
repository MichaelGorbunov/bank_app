import os
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


def decorator_with_args(filename: str | None = None) -> None:
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Аргументы декоратора: {filename}")
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e: print(e)

            print("После выполнения функции")

        return wrapper
    return my_decorator


@decorator_with_args(filename="myfile.txt")
def my_function2(x, y):
    print(f"Выполнение функции с аргументами {x} и {y}")
    print(x/y)

my_function2(10, 2)

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