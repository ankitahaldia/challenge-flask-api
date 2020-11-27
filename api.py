from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route("/status")
def status():
    return "Alive!"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template(
            "login.html", title="MadCompany", heading1="MadCompany prediction model"
        )
    else:
        if request.json:
            user_name = request.json["username"]
            pwd_len = len(request.json["password"])
        elif request.form:
            user_name = request.form["username"]
            pwd_len = len(request.form["password"])
        return f"Login success for user {user_name} with password of length: {pwd_len}!"


@app.route("/predict/<int:seller_avaible>/<month>/<int:customer_visiting_website>")
def predict(seller_avaible, month, customer_visiting_website):
    random.seed(str(seller_avaible) + month + str(customer_visiting_website))
    return str(random.randint(2000, 5000))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
