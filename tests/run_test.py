# from src.addit_func import scan_dirs
# from src.masks import get_masked_nums
from src.addit_func import find_adv_string, search_max_div
from src.widget import mask_bank_data

# my_select_path = r"C:\Windows\Temp"
# print(scan_dirs(my_select_path, True))

# test_list = [7000792289606361, 73654108430135874305]
# for item in test_list:
#     print(get_masked_nums(item))

test_list2 = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
    "Счет Err 108430135874305",
    "Счет Err 736541084301358743058",
    "Visa Gold Err 59994142284З6353",
]

for i in test_list2:
    print(mask_bank_data(i))


test_list3 = [["hello", "world", "apple", "pear", "banana", "pop"], ["", "madam", "racecar", "noon", "level", ""], []]
for i3 in test_list3:
    print(find_adv_string(i3))

test_list4 = [
    [-3, 8, 10, -10, 20, 0, 25, 25],
    [-5, -7, -9, -13],
    [2, 3, 5, 7, 11],
    [1, 2],
    [4],
]
for i4 in test_list4:
    print(search_max_div(i4))
