from django.shortcuts import render
import requests
import json
def home(request):
    myapi = "" # put your api key here <-
    city = "birmingham"
    city = request.GET.get('city','birmingham')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={myapi}"
    data = requests.get(url).json()
    payload = {
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kelvin__temprature':data['main']['temp'],
        'celcius_temprature':int(data['main']['temp'] - 273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description':data['weather'][0]['description']
        }
    context = {'data':payload}
    print(context)
    return render(request, 'home.html',context)
