import json

FILENAME = "tasks.json"
USERS = "users.json"

def load_results():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)  # BU YERDA INDEMTATSIYANI TEKSHIRING!
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_results(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=2)      


def user_results():
    try:
        with open(USERS, "r") as f:
            return json.load(f)  # BU YERDA INDEMTATSIYANI TEKSHIRING!
    except (FileNotFoundError, json.JSONDecodeError):
        return []
