from flask import Flask, render_template
import requests
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    query = "Winnipeg,CA"
    unit = "metric"
    api_key = os.environ.get("API_VAL")

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)

    data = requests.get(url=url)  # GET request to the OpenWeatherMap API

    return render_template("index.html", data=data.json())


if __name__ == '__main__':
    app.run()
