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
