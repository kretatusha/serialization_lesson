import json
import logging
from datetime import datetime, timezone

from pythonjsonlogger.json import JsonFormatter

# Создаём JSON-форматтер

json_formatter = JsonFormatter(
    "%(asctime)s %(levelname)s %(message)s %(user_id)s %(action)s"
)

# Вывод в консоль

console_handler = logging.StreamHandler()
console_handler.setFormatter(json_formatter)

# Запись в файл

file_handler = logging.FileHandler(
    "user_activity.log",
    mode="a",
    encoding="utf-8",
)
file_handler.setFormatter(json_formatter)

# Общая настройка логирования

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        console_handler,
        file_handler,
    ],
)


def log_user_action(user_id: int, action: str) -> None:
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_id": user_id,
        "action": action,
    }

    # Преобразуем словарь в JSON и отправляем в лог
    logging.info(json.dumps(log_entry, ensure_ascii=False))


log_user_action(42, "login")
log_user_action(105, "view_product_12")
log_user_action(42, "logout")
