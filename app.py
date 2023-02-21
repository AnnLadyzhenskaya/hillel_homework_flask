from flask import Flask, request
from faker import Faker
import requests
import pandas as pd

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
    inches_to_cm = 2.54
    pounds_to_kg = 0.45359237
    df = pd.read_csv("./static/hw.csv")
    df = df.rename(columns=lambda x: x.strip())

    mean_height = df['"Height(Inches)"'].mean() * inches_to_cm
    mean_weight = df['"Weight(Pounds)"'].mean() * pounds_to_kg

    return {"avg_height_cm": round(mean_height, 2), "avg_weight_kg": round(mean_weight, 2)}


@app.get("/space/")
def get_astronauts_count():
    r = requests.get("http://api.open-notify.org/astros.json")
    astronauts_count = r.json()["number"]

    return {"Astronauts count": astronauts_count}
