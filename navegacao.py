from flask import render_template
from app import app

@app.route("/")
def homepage():
    imagens = ["download.png", "download.png"]
    return render_template("main.html", imagens=imagens)

@app.route("/download/<nome_imagem>")
def download_page(nome_imagem):
    imagens = ["download.png", "download.png"]
    return render_template("dowloads_page.html", imagem=nome_imagem, imagens=imagens)