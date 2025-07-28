import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_dir: str = "logs",
                  log_file: str = "bot.log",
                  level: int = logging.INFO,
                  max_bytes: int = 5 * 1024 * 1024,
                  backup_count: int = 3
                  ) -> logging.Logger:
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("nightreign_bot")
    logger.setLevel(level)

    if logger.handlers:
        return logger
    
    formatter = logging.Formatter("{asctime} | {name} | {levelname} | {message}", style = "{", datefmt= "%Y-%m-%d %H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    
    file_path = os.path.join(log_dir, log_file)
    file_handler = RotatingFileHandler(
        filename=file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )

    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger