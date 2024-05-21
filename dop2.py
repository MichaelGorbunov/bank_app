from datetime import datetime

# Функция должна возвращать словарь, содержащий информацию о средней стоимости заказа и количестве заказов за каждый месяц. Ключами словаря должны быть год и месяц в формате
# YYYY-MM
# , а значениями — словари, содержащие два поля:
# average_order_value
# — средняя стоимость заказа за месяц,
# order_count
# — количество заказов за месяц.
list1 = [
    {"id": 1, "date": "01.01.2024",
     "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}, {"name": "tovar3", "price": 10.6, "quantity": 1},
               {"name": "tovar5", "price": 10.2, "quantity": 2}]},
    {"id": 2, "date": "01.02.2024",
     "items": [{"name": "tovar2", "price": 10.5, "quantity": 2}, {"name": "tovar8", "price": 10.3, "quantity": 1}]},
    {"id": 3, "date": "01.03.2024", "items": [{"name": "tovar3", "price": 10.6, "quantity": 1}]},
    {"id": 4, "date": "01.04.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 3}]},
    {"id": 5, "date": "01.05.2024", "items": [{"name": "tovar2", "price": 10.7, "quantity": 1}]},
    {"id": 6, "date": "01.06.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
    {"id": 7, "date": "01.07.2024",
     "items": [{"name": "tovar5", "price": 10.2, "quantity": 2}, {"name": "tovar8", "price": 10.3, "quantity": 1}]},
    {"id": 8, "date": "01.08.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
    {"id": 9, "date": "01.09.2024",
     "items": [{"name": "tovar8", "price": 10.3, "quantity": 1}, {"name": "tovar7", "price": 10.5, "quantity": 1},
               {"name": "tovar15", "price": 10.5, "quantity": 2}]},
    {"id": 10, "date": "01.01.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
    {"id": 11, "date": "01.02.2024",
     "items": [{"name": "tovar1", "price": 10.4, "quantity": 2}, {"name": "tovar7", "price": 10.5, "quantity": 1}]},
    {"id": 12, "date": "01.03.2024", "items": [{"name": "tovar7", "price": 10.5, "quantity": 1}]},
    {"id": 13, "date": "01.04.2024",
     "items": [{"name": "tovar1", "price": 10.9, "quantity": 5}, {"name": "tovar15", "price": 10.5, "quantity": 2}]},
    {"id": 14, "date": "01.01.2024", "items": [{"name": "tovar11", "price": 10.8, "quantity": 1}]},
    {"id": 15, "date": "01.09.2024",
     "items": [{"name": "tovar12", "price": 10.5, "quantity": 1}, {"name": "tovar12", "price": 10.5, "quantity": 1}]},
    {"id": 16, "date": "01.11.2024", "items": [{"name": "tovar7", "price": 10.6, "quantity": 5}]},
    {"id": 17, "date": "01.12.2024", "items": [{"name": "tovar18", "price": 10.5, "quantity": 1}]},
    {"id": 18, "date": "01.08.2024", "items": [{"name": "tovar1", "price": 10.7, "quantity": 1}]},
    {"id": 19, "date": "01.07.2024", "items": [{"name": "tovar15", "price": 10.5, "quantity": 2}]},
    {"id": 20, "date": "01.01.2024",
     "items": [{"name": "tovar9", "price": 102, "quantity": 8}, {"name": "tovar12", "price": 10.5, "quantity": 1}]},
    {"id": 21, "date": "01.02.2024", "items": [{"name": "tovar8", "price": 10.1, "quantity": 1}]},
    {"id": 22, "date": "01.03.2024", "items": [{"name": "tovar7", "price": 10.3, "quantity": 1}]},
    {"id": 23, "date": "01.04.2024", "items": [{"name": "tovar11", "price": 10.2, "quantity": 2}]},
]
for item in list1:
    print("*")
    print(item)
    # print(item.get("items"))
    # a = datetime(item.get("date"))).strftime("%Y%m%d")
    # first_strdate = '10.05.2025'
    first_date = datetime.strptime(item["date"], '%d.%m.%Y')
    print(type(first_date))
    date2 = first_date.strftime('%Y-%m')
    print(date2)

    # dt_string = "12/11/2018 09:15:32"
    # dt_sring=first_date
    # # Considering date is in dd/mm/yyyy format
    # dt_object1 = dt.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
    # print("dt_object1 =", dt_object1)

    sum = 0
    for item2 in item.get("items"):
        sum = sum + item2["price"] * item2["quantity"]
        # print(item2["price"]*item2["quantity"])
    print(sum)
