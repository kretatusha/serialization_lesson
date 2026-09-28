import pickle

# Сохранение словаря Сериализация
with open('my_dict.pkl', 'wb') as file:
    pickle.dump({'key': 'value'}, file)  # Работаем с данными.

# Загрузка словаря обратно Десериализация
with open('my_dict.pkl', 'rb') as file:
    data = pickle.load(file)  # Читаем данные!
    print(data)

