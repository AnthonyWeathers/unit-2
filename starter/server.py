from flask import Flask, render_template, url_for, redirect
from cupcakes import delete_cupcake_dictionary, get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("display.csv"))

@app.route("/cupcake/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("display.csv", name)

    if cupcake:
        return render_template("cupcake.html", cupcake = find_cupcake("display.csv", name))
    else:
        return "Sorry cupcake not found."

@app.route("/order")
def order():
    return render_template("order.html", cupcakes = get_cupcakes("curr_order.csv"))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("display.csv", name)

    if cupcake:
        add_cupcake_dictionary("curr_order.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."
    
@app.route("/delete-cupcake/<name>")
def delete_cupcake(name):
    cupcake = find_cupcake("curr_order.csv", name)

    delete_cupcake_dictionary("curr_order.csv", cupcake)
    return redirect(url_for("order"))

if __name__ == "__main__":
    app.debug = "development"

    app.run(debug = True, port = 9001, host = "localhost")