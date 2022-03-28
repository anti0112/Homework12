import json

POST_PATH = "posts.json"


def load():
    with open(POST_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def upload(posts):
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)