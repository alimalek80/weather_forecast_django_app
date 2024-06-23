from django.shortcuts import render
import requests


def index(request):
    API_KEY = open("API_KEY", "r").read()
    current_weather_url = "http://api.weatherapi.com/v1/current.json?key={}&q={}"
    forecast_url = "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=7"

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url,
                                                                         forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
            "weather_data2": weather_data2,
            "daily_forecasts2": daily_forecasts2
        }
        return render(request, 'weather_forecast_app/index.html', context=context)
    else:
        return render(request, 'weather_forecast_app/index.html')


def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(api_key, city)).json()
    forecast_response = requests.get(forecast_url.format(api_key, city)).json()
    weather_data = {
        "city": response["location"]["name"],
        "temperature": response['current']['temp_c'],
        "humidity": response['current']['humidity'],
        "description": response['current']['condition']['text'],
        "icon": response['current']['condition']['icon']
    }

    daily_forecasts = []
    for daily_data in forecast_response['forecast']['forecastday'][:7]:
        daily_forecasts.append({
            "day": daily_data['date'],
            "min_temp": daily_data['day']['mintemp_c'],
            "max_temp": daily_data['day']['maxtemp_c'],
            "humidity": daily_data['day']['avghumidity'],
            "description": daily_data['day']['condition']['text'],
            "icon": daily_data['day']['condition']['icon']
        })

    return weather_data, daily_forecasts
