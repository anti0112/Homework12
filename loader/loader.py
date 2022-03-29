from flask import Blueprint, render_template, request
from functions import load, upload
import logging

loader = Blueprint("loader", __name__)
logging.basicConfig(level=logging.INFO)


@loader.route("/add")
def add_post():
    return render_template("post_form.html")


@loader.route("/upload/", methods=["GET", "POST"])
def uploads():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        upload(posts)
        file.save(f"uploads/images/{filename}")
        if filename.split()[-1] not in ["jpeg", "jpg", "png"]:
            logging.info("Не подходящее расширение")
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return "Файл не найден"
    else:
        return render_template("post_uploaded.html", posts=posts[-1])
