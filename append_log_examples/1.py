import json
import logging
from datetime import datetime, timezone


# Настраиваем вывод логов в консоль и файл

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            "user_activity.log",
            mode="a",
            encoding="utf-8",
        ),
    ],
)


def log_user_action(user_id: int, action: str) -> None:
    # Создаём запись в виде словаря
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_id": user_id,
        "action": action,
    }

    # Преобразуем словарь в JSON и отправляем в лог
    logging.info(json.dumps(log_entry, ensure_ascii=False))


# Добавляем несколько записей

log_user_action(42, "login")
log_user_action(105, "view_product_12")
log_user_action(42, "logout")