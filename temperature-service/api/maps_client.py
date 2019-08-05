import os
import requests

PROTOCOL = 'http'
BASE_URL = f'{PROTOCOL}://{os.environ["MAPS_SERVICE_URL"]}'

def get_coords(zip_code):
    url = f'{BASE_URL}/coords?zip_code={zip_code}'
    res = requests.get(url)
    if res.status_code == 200: return res.json()
    return 

def are_valid_coords(longitude, latitude):
    url = f'{BASE_URL}/coords/validate?longitude={longitude}&latitude={latitude}'
    return requests.get(url).status_code == 200