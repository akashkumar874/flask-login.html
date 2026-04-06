from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "akash" and password == "1234":
            return render_template("dashboard.html", user=username)
        else:
            return "<h3 style='color:red'>Login Failed ❌</h3>"

    return render_template("login.html")


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
