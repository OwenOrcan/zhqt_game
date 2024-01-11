from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/arif")
def arif():
    return render_template("arif.html")

if __name__ == "__main__":
    app.run(port=5001)