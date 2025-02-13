import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello CPS3500!"

@app.route("/new_page")
def new_page():
    return "This is a New Page!"

@app.route("/user/<username>")
def greet_user(username: str):
    return flask.render_template("index.html", username = username.upper())

if __name__ == "__main__":
    app.run(debug = True)