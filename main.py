from src.decorators import log


@log()
def my_function1(x, y):
    return x / y


my_function1(1, 0)
