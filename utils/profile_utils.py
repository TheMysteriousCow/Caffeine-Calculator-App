import json
import os


def get_profile_path(username):
    os.makedirs("profiles", exist_ok=True)
    return f"profiles/{username}.json"


def load_profile(username):
    path = get_profile_path(username)

    if not os.path.exists(path):
        return {
            "name": "",
            "first_name": "",
            "gender": "Female",
            "weight": 60,
            "height": 1.70
        }

    with open(path, "r") as f:
        return json.load(f)


def save_profile(username, profile_data):
    path = get_profile_path(username)

    with open(path, "w") as f:
        json.dump(profile_data, f)