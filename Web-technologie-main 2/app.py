from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("database.db")
c = conn.cursor()


#  наша корневая страиницу лендинга
@app.route("/")
def home():
    # Загрузка и отображение главной страницы (landing page)
    return render_template(
        "index.html", linkabout="/about", linkservice="/service", linkcontact="/contact"
    )


@app.route("/about")
def about():
    # Загрузка и отображение страницы "О нас" (about page)
    return render_template("about.html")


@app.route("/service")
def service():
    # Загрузка и отображение страницы "Услуги" (service page)
    return render_template("service.html")


@app.route("/contact")
def contact():
    # Загрузка и отображение страницы "Контакты" (contact page)
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


if __name__ == "__main__":
    app.run(debug=True, port=5001)
