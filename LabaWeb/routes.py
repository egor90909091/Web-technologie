from flask import (
    Flask,
    render_template,
    request,
    Response,
    jsonify,
    json,
)

from _init_ import (
    app,
    c,
    conn,
    delete_user,
    select_all_users,
    select_user_by_id,
    update_user,
)


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


# insert_user(first_name,last_name,email,phone)
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
