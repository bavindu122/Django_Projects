from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        source = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=2525c504ffcd25993bcf3108c4ec16a0"
        
        list_of_data = requests.get(source.format(city)).json()
        if(list_of_data['cod'] == "404"):
            weather_data = {
                'city': city,
                'found': False,
                }
            return render(request, 'weather.html', {'weather_data': weather_data})
        # Mapping weather conditions to Font Awesome icons
        condition_icons = {
            "clear sky": "fas fa-sun",
            "few clouds": "fas fa-cloud-sun",
            "scattered clouds": "fas fa-cloud",
            "broken clouds": "fas fa-cloud",
            "shower rain": "fas fa-cloud-showers-heavy",
            "rain": "fas fa-cloud-rain",
            "thunderstorm": "fas fa-bolt",
            "snow": "fas fa-snowflake",
            "mist": "fas fa-smog",
        }
        condition = str(list_of_data['weather'][0]['description']).lower()
        weather_icon = condition_icons.get(condition, "fas fa-question-circle")  # Default icon if condition not found

        weather_data = {
            'city': str(list_of_data['name']),
            'country': str(list_of_data['sys']['country']),
            'temp': round(list_of_data['main']['temp'] - 273.15, 2),
            'pressure': round(list_of_data['main']['pressure']),
            'humidity': round(list_of_data['main']['humidity']),
            'description': condition,
            'icon': weather_icon,
            'coord': str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            'found':True
        }
    else:
        weather_data = {}
    return render(request, 'weather.html', {'weather_data': weather_data})