import json
from dataclasses import dataclass
from typing import Any


@dataclass
class User:
    id: int
    name: str
    email: str | None = None
    age: int = 0

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "User":
        """Проверяет словарь и создаёт объект User."""

        # Проверяем наличие обязательных полей
        for field_name in ("id", "name"):
            if field_name not in data:
                raise ValueError(
                    f"Отсутствует обязательное поле '{field_name}'"
                )

        # Проверяем типы значений
        if type(data["id"]) is not int:
            raise TypeError("Поле 'id' должно быть целым числом")

        if not isinstance(data["name"], str):
            raise TypeError("Поле 'name' должно быть строкой")

        if data.get("email") is not None and not isinstance(data["email"], str):
            raise TypeError("Поле 'email' должно быть строкой или None")

        if "age" in data and type(data["age"]) is not int:
            raise TypeError("Поле 'age' должно быть целым числом")

        return cls(
            id=data["id"],
            name=data["name"],
            email=data.get("email"),
            age=data.get("age", 0),
        )

    @classmethod
    def from_json(cls, json_string: str) -> "User":
        """Загружает пользователя из JSON-строки."""

        data = json.loads(json_string)

        if not isinstance(data, dict):
            raise TypeError("JSON должен содержать объект")

        return cls.from_dict(data)


# JSON-данные в виде строки

json_data_string = '''
{
    "id": 123,
    "name": "Алиса в Стране чудес",
    "email": "alice@example.com"
}
'''


# Данные в виде словаря Python

json_data_dict = {
    "id": 456,
    "name": "Боб Строитель"
}


# 1. Загрузка пользователя из JSON-строки

try:
    user_from_string = User.from_json(json_data_string)
    print(f"Пользователь из JSON-строки: {user_from_string}")
except (ValueError, TypeError, json.JSONDecodeError) as error:
    print(f"Ошибка при загрузке из JSON-строки: {error}")


# 2. Загрузка пользователя из словаря

try:
    user_from_dict = User.from_dict(json_data_dict)
    print(f"Пользователь из словаря: {user_from_dict}")
except (ValueError, TypeError) as error:
    print(f"Ошибка при загрузке из словаря: {error}")


# Пример с отсутствующим обязательным полем id

invalid_json_string = '''
{
    "name": "Чарли"
}
'''

try:
    User.from_json(invalid_json_string)
except (ValueError, TypeError, json.JSONDecodeError) as error:
    print(f"\nОшибка валидации: {error}")