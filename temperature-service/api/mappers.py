import os

import requests

PROTOCOL = 'http'
BASE_URL = f'{PROTOCOL}://{os.environ["WEATHER_SERVICE_URL"]}'


""" 
noaa
 """
""" {"today":
 {"high": {"fahrenheit": "68", "celsius": "20"},
  "low": {"fahrenheit": "50", "celsius": "10"},
  "current": {"fahrenheit": "55", "celsius": "12"}}}
 """




def get_noaa_request(latitude, longitude):
    url = f'{BASE_URL}/noaa?latlon={latitude},{longitude}'
    return { "url": url, "method" : "get" }

def map_noaa_to_current_temp(response):
    return response['today']['current']['fahrenheit']


""" 
 accuweather
 """

"""  { "simpleforecast": 
 { "forecastday": [ 
     { "period": 1,
      "high": { "fahrenheit": "68", "celsius": "20" }, 
      "low": { "fahrenheit": "50", "celsius": "10" }, 
      "current": { "fahrenheit": "55", "celsius": "12" }, 
      "conditions": "Partly Cloudy", "icon": "partlycloudy", 
      "icon_url": "http://icons-ak.wxug.com/i/c/k/partlycloudy.gif", 
      "skyicon": "mostlysunny", 
      "pop": 0, 
      "qpf_allday": { "in": 0.0, "mm": 0.0 } } ] } } """

def get_accuweather_request(latitude, longitude):
    url = f'{BASE_URL}/accuweather?latitude={latitude}&longitude={longitude}'
    return {"url": url, "method" : "get"}


def map_accuweather_to_current_temp(response):
    return response['simpleforecast']['forecastday'][0]['current']['fahrenheit']



""" 
POST: /weatherdotcom
 """
""" 
 {
  "query": {
    "count": 1,
    "created": "2017-09-21T17:00:22Z",
    "lang": "en-US",
    "results": {
      "channel": {
        "units": {
          "temperature": "F"
        },
        "description": "Current Weather",
        "language": "en-us",
        "lastBuildDate": "Thu, 21 Sep 2017 09:00 AM AKDT",
        "ttl": "60",
        "condition": {
          "code": "33",
          "date": "Thu, 21 Sep 2017 08:00 AM AKDT",
          "temp": "37",
          "text": "Mostly Clear"
        },
        "atmosphere": {
          "humidity": "80",
          "pressure": "1014.0",
          "rising": "0",
          "visibility": "16.1"
        },
        "astronomy": {
          "sunrise": "8:42 am",
          "sunset": "9:6 pm"
        },
        "item": {
          "title": "Conditions for Nome, AK, US at 08:00 AM AKDT",
          "lat": "64.499474",
          "long": "-165.405792",
          "pubDate": "Thu, 21 Sep 2017 08:00 AM AKDT",
          "guid": {
            "isPermaLink": "false"
          }
        }
      }
    }
  }
} """

def get_weatherdotcom_request(latitude, longitude):
    url = f'{BASE_URL}/weatherdotcom'
    return {"url" : url, "method" : "post", "data" : {"lat" : float(latitude), "lon" : float(longitude)}}

def map_weatherdotcom_to_current_temp(response):
    return response['query']['results']['channel']['condition']['temp']
    


callers = {
    "noaa" : {
        "request": get_noaa_request,
        "mapper": map_noaa_to_current_temp
    },
    "accuweather" : {
        "request": get_accuweather_request,
        "mapper": map_accuweather_to_current_temp
    },
        "weatherdotcom" : {
        "request": get_weatherdotcom_request,
        "mapper": map_weatherdotcom_to_current_temp
    }
}

def make_temp_request(destination, latitude, longitude):
    call = callers[destination]
    req = call['request'](latitude, longitude)    
    res = requests.request(req['method'], url=req['url'], json=req.get('data'))
    res.raise_for_status()
    return float(call['mapper'](res.json()))

