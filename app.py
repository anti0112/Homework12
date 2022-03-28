from flask import Flask, request, render_template, send_from_directory
from main.main import main
from loader.loader import loader

UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(loader)


@app.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images", path)


app.run(debug=True)

