from flask import Flask, request
from faker import Faker
import requests

app = Flask(__name__)


@app.get("/")
def hello_world():
    return {"project_name": "Hillel Flask Homework"}


@app.get("/requirements/")
def show_requirements():

    with open("./requirements.txt", "r") as f:
        requirements = dict(line.strip().split("==") for line in f if not (line.startswith("#") or len(line.strip()) == 0))
        return requirements


@app.get("/generate-users/")
def generate_users():
    count = int(request.args.get("count", 100))
    fake = Faker()

    users = list()
    for _ in range(count):
        users.append({"name": fake.first_name(), "email": fake.email()})

    return users


@app.get("/mean/")
def calculate_mean():
    pass


@app.get("/space/")
def get_astronauts_count():
    r = requests.get("http://api.open-notify.org/astros.json")
    astronauts_count = r.json()["number"]

    return {"Astronauts count": astronauts_count}
