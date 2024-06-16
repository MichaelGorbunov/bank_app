# Проект bank_app

## Описание:

Проект bank_app - набор модулей Python для выполнения различных банковских операций.
Создан и разрабатывается в образовательных целях.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/MichaelGorbunov/bank_app.git
```
2. Установите зависимости:
```
poetry install
```
## Реализованные функции:

1. **mask_bank_data**   функция принимает на вход строку с информацией — тип карты/счета и номер карты/счета.

    Возвращает исходную строку с замаскированным номером карты/счета.
2. **filter_operations** функция принимает список словарей с деталями операций и возвращает 
отсортированные по одному из состояний.
3. **sorted_operation** функция сортировки списка словарей по дате.
4. **card_number_generator** генератор номеров банковских карт.
5. **filter_by_currency** функция сортировки банковский операций по типу валюты.
6. **transaction_descriptions** функция вывода описания банковской операции.
7. **декоратор log** логирование результатов функций
8. **currency_conversion** конвертирование валют
9. **get_transaction_from_file** чтение транзакций из файла json
10. **get_transaction_amoun** стоимость транзакции
11. к модулям **utils** и **mask** добавлены функции логирования

## Дополнительно:
Написаны тесты для реализованных функций. Степень покрытия тестами можно посмотреть:
```
 pytest --cov=src --cov-report term-missing
```

## Лицензия:

Этот проект можно использовать безвозмездно для любых, 
не противоречащих законодательству целей.
