import warnings
warnings.simplefilter("ignore")

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '638e7bc2198602666c9eb8d5ead695e6'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = None

    if request.method == 'POST':
        city = request.form.get('city')
        response = requests.get(BASE_URL.format(city, API_KEY))
        print(response.text)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }

    return render_template('index.html', weather_data=weather_data, city=city)


if __name__ == "__main__":
    app.run(debug=True)




