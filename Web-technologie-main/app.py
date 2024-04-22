from flask import Flask, render_template, request

app = Flask(__name__)


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
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]

    # Пример обработки данных: выводим их в консоль сервера
    print("Полученные данные:")
    print("Имя:", name)
    print("Email:", email)
    print("Телефон:", phone)

    # Здесь вы можете выполнить какие-то действия с полученными данными, например, сохранить их в базе данных

    # Возвращаем сообщение об успешной обработке данных
    return "Данные успешно получены и обработаны!"


if __name__ == "__main__":
    app.run(debug=True)
