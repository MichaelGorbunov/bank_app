import re

# Поиск всех цен в строке

text = "The price of the product is $100.50"

numbers = re.findall(r"\d+\.\d+", text)

print(numbers)
