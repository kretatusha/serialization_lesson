import jsonschema
from jsonschema import validate

# 1. Определяем JSON-схему

schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Имя пользователя"
        },
        "age": {
            "type": "integer",
            "minimum": 0,
            "description": "Возраст пользователя"
        },
        "email": {
            "type": "string",
            "format": "email",
            "description": "Адрес электронной почты пользователя"
        },
        "is_active": {
            "type": "boolean",
            "default": True,
            "description": "Активна ли учётная запись пользователя"
        },
        "tags": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
            "uniqueItems": True,
            "description": "Список тегов, связанных с пользователем"
        }
    },
    "required": ["name", "age", "email"],  # Указываем обязательные свойства
    "additionalProperties": False  # Запрещаем свойства, не определённые в схеме
}

# 2. Подготавливаем JSON-данные для проверки

valid_data = {
    "name": "Алиса",
    "age": 30,
    "email": "alice@example.com",
    "is_active": True,
    "tags": ["разработчик", "python"]
}

invalid_data_type = {
    "name": "Боб",
    "age": "двадцать пять",  # Недопустимый тип данных для возраста
    "email": "bob@example.com"
}

invalid_data_missing_required = {
    "name": "Чарли",
    "age": 40,
    # Отсутствует обязательное поле "email"
}

invalid_data_additional_property = {
    "name": "Дэвид",
    "age": 28,
    "email": "david@example.com",
    "extra_field": "некоторое значение"  # Не разрешено параметром additionalProperties: False
}

# 3. Выполняем проверку данных

print("--- Проверка valid_data ---")
try:
    validate(instance=valid_data, schema=schema)
    print("JSON-данные корректны.")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON-данные некорректны: {e.message}")

print("\n--- Проверка invalid_data_type ---")
try:
    validate(instance=invalid_data_type, schema=schema)
    print("JSON-данные корректны.")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON-данные некорректны: {e.message}")

print("\n--- Проверка invalid_data_missing_required ---")
try:
    validate(instance=invalid_data_missing_required, schema=schema)
    print("JSON-данные корректны.")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON-данные некорректны: {e.message}")

print("\n--- Проверка invalid_data_additional_property ---")
try:
    validate(instance=invalid_data_additional_property, schema=schema)
    print("JSON-данные корректны.")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON-данные некорректны: {e.message}")