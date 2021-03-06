from whaaaaat import prompt, print_json
import argparse
import getpass
import json

from ufora_login import get_session


def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument("setup")
    parser.add_argument("--username")
    parser.add_argument("--password")
    args = parser.parse_args()
    username = args.username
    password = args.password
    questions = []
    if not username:
        questions.append({
            "type": "input",
            "message": "Enter your Ufora username",
            "name": "username"
        })
    if not password:
        questions.append({
            "type": "password",
            "message": "Enter your Ufora password",
            "name": "password"
        })

        answers = prompt(questions)

        username = answers["username"]
        password = answers["password"]
    session = get_session(username, password)
    if session is None:
        print("Invalid login credentials")
        return
    with open("credentials.json", "w+") as f:
        f.write(json.dumps({
            "username": username,
            "password": password
        }))
    print("Setup complete!")
