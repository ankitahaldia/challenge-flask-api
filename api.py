from flask import Flask, request, render_template, make_response, jsonify
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

        def login_answer(un, pwd):
            return f'Login success for user {un} with password of length: {len(pwd)}!'

        if request.json:
            user_name = request.json["username"]
            pwd = request.json["password"]
            return login_answer(user_name, pwd), 200
        elif request.form:
            user_name = request.form["username"]
            pwd = request.form["password"]
            return login_answer(user_name, pwd), 200
        else:
            return "Request should be either JSON or form data", 400


@app.route("/predict/<int:seller_avaible>/<month>/<int:customer_visiting_website>")
def predict(seller_avaible, month, customer_visiting_website):
    """an idempotent prediction taking on the parameters provided in the url path"""
    random.seed(str(seller_avaible) + month + str(customer_visiting_website))
    response_dict = {
        'seller_avaible': seller_avaible,
        'month': month,
        'customer_visiting_website': customer_visiting_website,
        '_prediction': random.randint(2000, 5000)
    }
    res = make_response(jsonify(response_dict), 200)
    return res


if __name__ == "__main__":
    app.run(port=5000, debug=True)
