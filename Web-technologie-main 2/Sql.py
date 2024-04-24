with open('create_table_users.sql', 'w') as sql_file:
    # Записываем запрос для создания таблицы в файл
    sql_file.write("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT
        );
    """)