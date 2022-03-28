from flask import Blueprint, render_template, request
from functions import load
import logging

main = Blueprint("main", __name__)
logging.basicConfig(level=logging.INFO)


@main.route("/")
def main_page():
    return render_template("index.html")


@main.route("/search")
def search():
    try:
        s = request.args["s"]
        posts = [x for x in load() if s.lower() in x["content"].lower()]
        logging.info(f"Слово для поиска:{s}")
    except FileNotFoundError:
        return "Файл не найден"
    else:
        return render_template("post_list.html", s=s, posts=posts)
