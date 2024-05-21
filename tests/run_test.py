# from src.addit_func import scan_dirs
# from src.masks import get_masked_nums
from src.addit_func import find_adv_string, search_max_div, sort_dict_list
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

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"},
]

# print(sort_dict_list(products, "veggie"))
print(sort_dict_list(products, None))
