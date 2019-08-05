import os
import json
from flask import Flask, request, make_response, jsonify
from requests import get, status_codes

app = Flask(__name__)


KEY = os.environ['MAPS_KEY']
BASE_URL = 'https://maps.googleapis.com/maps/api'

@app.route('/coords', methods=['GET'])
def get_coordinates():
    zip_code_param = 'zip_code'
    try:        
        zip_code = request.args.get(zip_code_param)
        coords = get(
            f'{BASE_URL}/geocode/json?address={zip_code}&key={KEY}').json()['results'][0]['geometry']['location']
        
        lat, lng = float(coords['lat']), float(coords['lng'])
        return jsonify({"latitude": lat, "longitude" : lng})
    except:
        return make_response('zip_code is a required query parameter', 400)


@app.route('/coords/validate', methods=['GET'])
def validate_coords():
    latitude_param, longitude_param = 'latitude', 'longitude'
    try:
        latitude, longitude = float(request.args.get(latitude_param)), float(request.args.get(longitude_param))
    except:
        return make_response('Must provide the "{:s}" and "{:s}" query params as float values\n'.format(latitude_param, longitude_param), 400)    
    res = get(
        f'{BASE_URL}/timezone/json?location={latitude},{longitude}&timestamp=1458000000&key={KEY}')
    if (res.status_code == 200): return make_response('Valid coordinates', 200)
    else: return make_response('Invalid coordinates', 400)

app.run(debug=True, host='0.0.0.0', port=int(os.environ['PORT']))
