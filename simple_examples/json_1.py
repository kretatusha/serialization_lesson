import json

# Сохранение словаря
with open('my_dict.json', 'w') as file:
    json.dump({'key': 'value'}, file)  # Ключи и значения значимы!

# Загрузка словаря
with open('my_dict.json', 'r') as file:
    data = json.load(file)  # Загрузка данных!
    print(data)

