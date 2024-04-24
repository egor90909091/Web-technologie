from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("database.db")
c = conn.cursor()


# #  наша корневая страиницу лендинга
# @app.route("/")
# def home():
#     # Загрузка и отображение главной страницы (landing page)
#     return render_template(
#         "index.html", linkabout="/about", linkservice="/service", linkcontact="/contact"
#     )


# @app.route("/about")
# def about():
#     # Загрузка и отображение страницы "О нас" (about page)
#     return render_template("about.html")


# @app.route("/service")
# def service():
#     # Загрузка и отображение страницы "Услуги" (service page)
#     return render_template("service.html")


# @app.route("/contact")
# def contact():
#     # Загрузка и отображение страницы "Контакты" (contact page)
#     return render_template("contact.html")


# @app.route("/submit_form", methods=["POST"])
# def submit_form():
#     # Получение данных из формы
#     first_name = request.form["first_name"]
#     last_name = request.form["last_name"]
#     email = request.form["email"]
#     phone = request.form["phone"]

#     # Создание или подключение к базе данных
#     conn = sqlite3.connect("database.db")
#     c = conn.cursor()

#     # Вставка данных в таблицу Users
#     c.execute(
#         "INSERT INTO users (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)",
#         (first_name, last_name, email, phone),
#     )

#     # Применение изменений и закрытие соединения
#     conn.commit()
#     conn.close()

#     # Вывод полученных данных в консоль сервера
#     print("Полученные данные:")
#     print("Имя:", first_name)
#     print("Фамилия:", last_name)
#     print("Email:", email)
#     print("Телефон:", phone)

#     # Возвращаем сообщение об успешной обработке данных
#     return "Данные успешно получены и обработаны"


# if __name__ == "__main__":
#     app.run(debug=True, port=5001)


# Функция для выполнения SELECT-запроса без фильтрации
def select_all_users():
    c.execute("SELECT * FROM users")
    return c.fetchall()


# Функция для выполнения SELECT-запроса с фильтрацией по ID пользователя
def select_user_by_id(user_id):
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    return c.fetchone()


# Функция для выполнения INSERT-запроса
def insert_user(first_name, last_name, email, phone):
    c.execute(
        "INSERT INTO users (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)",
        (first_name, last_name, email, phone),
    )
    conn.commit()


# Функция для выполнения UPDATE-запроса
def update_user(user_id, first_name, last_name, email, phone):
    c.execute(
        "UPDATE users SET first_name=?, last_name=?, email=?, phone=? WHERE id=?",
        (first_name, last_name, email, phone, user_id),
    )
    conn.commit()


# Функция для выполнения DELETE-запроса
def delete_user(user_id):
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()


# Закрытие соединения с базой данных
def close_connection():
    conn.close()


# Наши маршруты Flask


@app.route("/")
def home():
    return render_template(
        "index.html", linkabout="/about", linkservice="/service", linkcontact="/contact"
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/submit_form", methods=["POST"])
def submit_form():
    # Получение данных из формы
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    # Создание или подключение к базе данных
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Вставка данных в таблицу Users
    c.execute(
        "INSERT INTO users (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)",
        (first_name, last_name, email, phone),
    )

    # Применение изменений и закрытие соединения
    conn.commit()
    conn.close()

    # Вывод полученных данных в консоль сервера
    print("Полученные данные:")
    print("Имя:", first_name)
    print("Фамилия:", last_name)
    print("Email:", email)
    print("Телефон:", phone)

    # Возвращаем сообщение об успешной обработке данных
    return "Данные успешно получены и обработаны"


@app.route("/users")
def get_users():
    users = select_all_users()
    return jsonify(users)


@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = select_user_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404


@app.route("/update_user/<int:user_id>", methods=["PUT"])
def update_user_route(user_id):
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    phone = data.get("phone")

    update_user(user_id, first_name, last_name, email, phone)

    return f"User with ID {user_id} successfully updated"


@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    delete_user(user_id)
    return f"User with ID {user_id} successfully deleted"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
