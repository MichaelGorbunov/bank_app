# from src.addit_func import scan_dirs
# from src.masks import get_masked_nums
from src.addit_func import find_adv_string, search_max_div
from src.processing import filter_operations, sorted_operation
from src.widget import date_from_string, mask_bank_data

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

print(date_from_string("2018-07-11T02:26:18.671407"))

test_dict_list1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
# print(filter_operations(test_dict_list1))
print(filter_operations(test_dict_list1, "CANCELED"))

test_dict_list2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sorted_operation(test_dict_list2, False))
