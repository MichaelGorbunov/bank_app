import os

from config import DATA_DIR
from src.masks import get_masked_nums
from src.processing import filter_operations, sorted_operation
from src.utils import get_transaction_from_csv_file, get_transaction_from_file, get_transaction_from_xlsx_file
from src.widget import date_from_string


def main():
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user_file_choice = input().strip()
        if user_file_choice == "1":
            print("Для обработки выбран JSON-файл.")
            list_transactions = get_transaction_from_file(os.path.join(DATA_DIR, "operations.json"))
            break
        elif user_file_choice == "2":
            print("Для обработки выбран CSV-файл.")
            list_transactions = get_transaction_from_csv_file(os.path.join(DATA_DIR, "transactions.csv"))
            break
        elif user_file_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            list_transactions = get_transaction_from_xlsx_file(os.path.join(DATA_DIR, "transactions_excel.xlsx"))
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    filters = []
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        ).upper()
        if status in ["CANCELED", "PENDING", "EXECUTED"]:
            filters.append(("status", status))
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        sort_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if sort_date == "да":
            sorting_order = input(
                """Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n""").lower()
            if sorting_order == "по возрастанию":
                filters.append(("date", False))
                break
            else:
                filters.append(("date", True))
                break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        sort_code = str(input("Выводить только рублевые тразакции? Да/Нет\n")).lower()
        if sort_code == "да":
            filters.append(("currency", "RUB"))
            break
        elif sort_code == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search = input("Видите слово для поиска: ")
            filters.append(("description", search))
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    transactions = list_transactions
    for filter_type, filter_value in filters:
        if filter_type == "status":
            transactions = filter_operations(transactions, filter_value)
        elif filter_type == "date":
            transactions = sorted_operation(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [
                txn for txn in transactions if txn.get("operationAmount")["currency"]["code"] == filter_value
            ]
        # elif filter_type == "description":
        #     transactions = list_transactions_sort_search(transactions, filter_value)
    print("Распечатываю итоговый список транзакций...")
    print(transactions)

    print(f"Всего банковских операций в выборке: {len(transactions)}")


if __name__ == "__main__":
    main()
