import configparser
import json
import os
import requests

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    config = dict(config.items("Uploader"))
    base_url = config["site"]
    res = requests.post(base_url + "/user/login", {
        "username": config["username"],
        "password": config["password"]
    })
    token = json.loads(res.text)["token"]
    path = config["dir"]
    for file in os.listdir(path):
        u_file = [
            ("image", (file, open(path + file, "rb")))
        ]
        t = requests.post(base_url + "/pics", {
            "name": file.replace(".jpg", "").replace(".png", ""),
            "description": file.replace(".jpg", "").replace(".png", "")
        }, files=u_file, headers={
            "Authorization": "Bearer " + token
        })
        print(t.text)
