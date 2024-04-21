from flask import Flask, render_template, redirect, url_for, request

# Flask - библиотека для запуска нашего приложения Flask - app
# render_template - нужен для то чтобы ваша страница html отобразилась корреткно
# redirect - нам понадобится для обработки запросы формы где мы перенаприм пользователя на страницу админ панели
# url_for - вспомогательна библиотека для того чтобы сделать правильный переход по ссылке в нашем случеш мы будем ссылаться на adm_panel
# request - обработчик запросов GET/POST и дргуих

app = Flask(__name__)


#  наша корневая страиницу лендинда
@app.route("/")
def home():
    # Загрузка и отображение главной страницы (landing page)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
