from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    imagens = [
        "download.png",
        "download.png",

    ]
    return render_template("main.html", imagens=imagens)

if __name__ == "__main__":
    app.run(debug=True)
