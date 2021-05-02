import requests
from django.shortcuts import render
from .forms import CityForm
import datetime

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6a08e4953c5ffabd9f304c5ae9eb759e'
    city = 'Kathmandu'
    if request.method == 'POST':
        form = CityForm(request.POST)
        print(request.POST['name'])
        city = request.POST['name']
        form.save()
    form = CityForm()
    req = requests.get(url.format(city)).json()
    desc = req['weather'][0]['description']
    bgImg = 'white'
    weatherDict = {
        'cod': req['cod'],
        'bg': bgImg,
        'city': req['name'],
        'country': req['sys']['country'],
        'temp': req['main']['temp'],
        'description': req['weather'][0]['description'],
        'icon': req['weather'][0]['icon'],
        'lon': req['coord']['lat'],
        'lat': req['coord']['lon'],
        'feel': req['main']['feels_like'],
        'min': req['main']['temp_min'],
        'max': req['main']['temp_max'],
        'humidity': req['main']['humidity'],
        'pressure': req['main']['pressure'],
    }
    # print(weatherDict)
    context = {'weatherDict': weatherDict, 'form': form}
    return render(request, 'weather/weather.html', context)
