from dataclasses import dataclass, field
from typing import Optional

import marshmallow_dataclass
from marshmallow import ValidationError, validate
from marshmallow_dataclass.typing import Email


@dataclass
class User:
    id: int
    name: str
    email: Optional[Email] = None
    age: int = field(
        default=0,
        metadata={
            "validate": validate.Range(min=0)
        },
    )


# Автоматически создаём Marshmallow-схему из dataclass

user_schema = marshmallow_dataclass.class_schema(User)()


# JSON-данные в виде строки

json_data_string = '''
{
    "id": 123,
    "name": "Алиса",
    "email": "alice@example.com",
    "age": 30
}
'''


# Данные в виде словаря

json_data_dict = {
    "id": 456,
    "name": "Боб"
}


# 1. Загрузка из JSON-строки

try:
    user_from_string = user_schema.loads(json_data_string)
    print(f"Пользователь из JSON-строки: {user_from_string}")
except ValidationError as error:
    print(f"Ошибка валидации: {error.messages}")


# 2. Загрузка из словаря

try:
    user_from_dict = user_schema.load(json_data_dict)
    print(f"Пользователь из словаря: {user_from_dict}")
except ValidationError as error:
    print(f"Ошибка валидации: {error.messages}")


# 3. Пример с отсутствующим обязательным полем id

invalid_json_string = '''
{
    "name": "Чарли"
}
'''

try:
    user_schema.loads(invalid_json_string)
except ValidationError as error:
    print(f"\nОшибка валидации: {error.messages}")


# 4. Обратная сериализация объекта в JSON

user = User(
    id=789,
    name="Давид",
    email="david@example.com",
    age=28,
)

json_result = user_schema.dumps(user, ensure_ascii=False)
print(f"\nРезультат сериализации: {json_result}")