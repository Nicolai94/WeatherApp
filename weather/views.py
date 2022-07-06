from django.shortcuts import render
import requests
from .forms import CityForm

from .models import City


def index(request):
    appid = '79a53350a68c7ea12db3223614bf7120'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()

    allcities = []
    for city in cities:
        res = requests.get(url.format(city)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        allcities.append(city_info)
    context = {
        'allinfo': allcities,
        'form': form
    }
    return render(request, 'weather/index.html',context)
