from django.http import JsonResponse
from urllib.parse import parse_qs
from .maps_client import get_coords, are_valid_coords
from .mappers import make_temp_request
from .temperature import get_averages

def get_filters(params):
    default_filters = ['noaa', 'accuweather', 'weatherdotcom']

    filters = [filter for filter in params.get(
        'filters', default_filters) if filter in default_filters]

    if len(filters) > 0:
        return filters
    else:
        return default_filters

def get_param_safe(params, param):
    return params.get(param, [None])[0]

def get_average_temp(request):
    params = parse_qs(request.GET.urlencode())

    longitude, latitude = get_param_safe(params, 'longitude'), get_param_safe(params, 'latitude')
    zip_code = get_param_safe(params, 'zip_code')

    if (zip_code): 
        try:
            coords = get_coords(zip_code)
            longitude, latitude = coords['longitude'], coords['latitude']
        except:
            return JsonResponse({'message': 'Valid zip_code required'}, status=400)


    if (not longitude or not latitude):
        return JsonResponse({'message': 'latitude and longitude or valid zip_code required'}, status=400)
    if (not are_valid_coords(longitude, latitude)): return JsonResponse({'message': 'latitude and longitude must be valid coordinates'}, status=400)
    
    filters = get_filters(params)
    try:
        temps = [make_temp_request(destination, latitude, longitude)
                for destination in filters]
        return JsonResponse(get_averages(temps), safe=False)
    except: return JsonResponse({'message': 'Downstream service not responding'}, status=503)

