from LMAS_weather import lmas_weather
from flask import Flask,request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/weatherapi',methods=['GET'])
def weatehrapi():
    lat=request.args.get('lat')
    lon=request.args.get('lon')
    mac_id=request.args.get('mac_id')

    weather_prediction = lmas_weather(lat, lon,mac_id)

    print(weather_prediction)

    return json.dumps(weather_prediction)


if __name__ == "__main__":
    app.debug = True
    app.run()