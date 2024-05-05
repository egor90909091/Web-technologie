from flask import Flask, jsonify, render_template, request
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect("database.db")
c = conn.cursor()


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


@app.route("/submit_form", methods=["POST"])
def submit_form():
    # Получение данных из формы
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)",
        (first_name, last_name, email, phone),
    )
    # # Применение изменений и закрытие соединения
    conn.commit()
    conn.close()

    # Вывод полученных данных в консоль сервера
    print("Полученные данные:")
    print("Имя:", first_name)
    print("Фамилия:", last_name)
    print("Email:", email)
    print("Телефон:", phone)

    # Возвращаем JSON с сообщением об успешной обработке данных
    response = {"message": "Данные успешно получены и обработаны"}
    return jsonify(response)
