from pydantic import BaseModel


# Определяем модель Pydantic

class User(BaseModel):
    id: int
    name: str
    email: str | None = None  # Необязательное поле со значением None по умолчанию
    age: int = 0


# JSON-данные в виде строки

json_data_string = '''
{
    "id": 123,
    "name": "Алиса в Стране чудес",
    "email": "alice@example.com"
}
'''


# JSON-данные в виде словаря Python

json_data_dict = {
    "id": 456,
    "name": "Боб Строитель"
}


# 1. Загрузка данных из JSON-строки с помощью model_validate_json

try:
    user_from_string = User.model_validate_json(json_data_string)
    print(f"Пользователь из JSON-строки: {user_from_string}")
except Exception as e:
    print(f"Ошибка при загрузке из JSON-строки: {e}")


# 2. Загрузка данных из словаря Python с помощью конструктора модели

try:
    user_from_dict = User(**json_data_dict)
    print(f"Пользователь из словаря: {user_from_dict}")
except Exception as e:
    print(f"Ошибка при загрузке из словаря: {e}")


# Пример с отсутствующим обязательным полем

invalid_json_string = '''
{
    "name": "Чарли"
}
'''

try:
    User.model_validate_json(invalid_json_string)
except Exception as e:
    print(f"\nОшибка валидации — отсутствует поле 'id': {e}")