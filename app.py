from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "akash" and password == "1234":
            return "Login success 🔥"
        else:
            return "Login Failed ❌"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
