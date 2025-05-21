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
            
        # Mapping weather conditions to Font Awesome icons - EXPANDED
        condition_icons = {
            # Clear conditions
            "clear sky": "fas fa-sun",
            
            # Cloud conditions
            "few clouds": "fas fa-cloud-sun",
            "scattered clouds": "fas fa-cloud",
            "broken clouds": "fas fa-cloud",
            "overcast clouds": "fas fa-cloud",
            
            # Rain conditions
            "light rain": "fas fa-cloud-rain",
            "moderate rain": "fas fa-cloud-rain",
            "heavy intensity rain": "fas fa-cloud-showers-heavy",
            "very heavy rain": "fas fa-cloud-showers-heavy",
            "extreme rain": "fas fa-cloud-showers-heavy",
            "freezing rain": "fas fa-icicles",
            "shower rain": "fas fa-cloud-showers-heavy",
            "light intensity shower rain": "fas fa-cloud-rain",
            "heavy intensity shower rain": "fas fa-cloud-showers-heavy",
            "ragged shower rain": "fas fa-cloud-showers-heavy",
            
            # Drizzle conditions
            "drizzle": "fas fa-cloud-rain",
            "light intensity drizzle": "fas fa-cloud-rain",
            "heavy intensity drizzle": "fas fa-cloud-rain",
            "drizzle rain": "fas fa-cloud-rain",
            "heavy intensity drizzle rain": "fas fa-cloud-rain",
            "shower rain and drizzle": "fas fa-cloud-showers-heavy",
            "heavy shower rain and drizzle": "fas fa-cloud-showers-heavy",
            "shower drizzle": "fas fa-cloud-rain",
            
            # Thunderstorm conditions
            "thunderstorm": "fas fa-bolt",
            "thunderstorm with light rain": "fas fa-bolt",
            "thunderstorm with rain": "fas fa-bolt",
            "thunderstorm with heavy rain": "fas fa-bolt",
            "light thunderstorm": "fas fa-bolt",
            "heavy thunderstorm": "fas fa-bolt",
            "ragged thunderstorm": "fas fa-bolt",
            "thunderstorm with light drizzle": "fas fa-bolt",
            "thunderstorm with drizzle": "fas fa-bolt",
            "thunderstorm with heavy drizzle": "fas fa-bolt",
            
            # Snow conditions
            "snow": "fas fa-snowflake",
            "light snow": "fas fa-snowflake",
            "heavy snow": "fas fa-snowflake",
            "sleet": "fas fa-snowflake",
            "light shower sleet": "fas fa-snowflake",
            "shower sleet": "fas fa-snowflake",
            "light rain and snow": "fas fa-snowflake",
            "rain and snow": "fas fa-snowflake",
            "light shower snow": "fas fa-snowflake",
            "shower snow": "fas fa-snowflake",
            "heavy shower snow": "fas fa-snowflake",
            
            # Atmosphere conditions
            "mist": "fas fa-smog",
            "smoke": "fas fa-smog",
            "haze": "fas fa-smog",
            "sand/dust whirls": "fas fa-wind",
            "fog": "fas fa-smog",
            "sand": "fas fa-wind",
            "dust": "fas fa-wind",
            "volcanic ash": "fas fa-volcano",
            "squalls": "fas fa-wind",
            "tornado": "fas fa-tornado",
            
            # Extreme conditions
            "hurricane": "fas fa-hurricane",
            "tropical storm": "fas fa-cloud-showers-heavy",
            "cold": "fas fa-temperature-low",
            "hot": "fas fa-temperature-high",
            "windy": "fas fa-wind",
            "hail": "fas fa-cloud-meatball",
        }
        
        condition = str(list_of_data['weather'][0]['description']).lower()
        weather_icon = condition_icons.get(condition, "fas fa-cloud-question")  # Updated default icon
        
        # Also add a main condition class for the template to use
        main_condition = str(list_of_data['weather'][0]['main']).lower()
        condition_class = "sunny"  # Default class
        
        # Map the main condition to a CSS class
        if "clear" in main_condition:
            condition_class = "sunny"
        elif "cloud" in main_condition:
            condition_class = "cloudy"
        elif "rain" in main_condition or "drizzle" in main_condition:
            condition_class = "rainy"
        elif "snow" in main_condition or "sleet" in main_condition:
            condition_class = "snowy"
        elif "mist" in main_condition or "fog" in main_condition or "haze" in main_condition:
            condition_class = "misty"
        elif "thunder" in main_condition:
            condition_class = "stormy"

        weather_data = {
            'city': str(list_of_data['name']),
            'country': str(list_of_data['sys']['country']),
            'temp': round(list_of_data['main']['temp'] - 273.15, 2),
            'pressure': round(list_of_data['main']['pressure']),
            'humidity': round(list_of_data['main']['humidity']),
            'description': condition,
            'main': main_condition,
            'icon': weather_icon,
            'condition_class': condition_class,
            'coord': str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            'found': True
        }
    else:
        weather_data = {}
    return render(request, 'weather.html', {'weather_data': weather_data})