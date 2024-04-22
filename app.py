from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True)
