import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect("database.db")

# Создание курсора
c = conn.cursor()



# Применение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()
