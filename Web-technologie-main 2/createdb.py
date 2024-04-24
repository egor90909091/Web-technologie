import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect("database.db")

# Создание курсора
c = conn.cursor()

# Создание таблицы Users
c.execute(
    """CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name TEXT,
             last_name TEXT,
             email TEXT,
             phone TEXT)"""
)

# Применение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()
