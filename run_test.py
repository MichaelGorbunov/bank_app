from src.addit_func import scan_dirs
from src.masks import get_masked_nums

my_select_path = r"C:\Windows\Temp"
print(scan_dirs(my_select_path, True))

test_list = [7000792289606361, 73654108430135874305]
for item in test_list:
    print(get_masked_nums(item))
