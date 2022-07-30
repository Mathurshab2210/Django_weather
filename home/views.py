from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url=f'https://api.openweathermap.org/data/2.5/weather?lat=26.4521&lon=74.6387&appid=ea37ede9347738b126e0301d0638eb25'
    data=requests.get(url).json()
    # print(data)
    payload={
        'city':data['name'],
    'weather':data['weather'][0]['main'], 
    'icon':data['weather'][0]['icon'],
    'k_temperature':data['main']['temp'],
    'c_temperature':data['main']['temp']-273,
    'pressure':data['main']['pressure'],
    'humidity':data['main']['humidity'],
    'description':data['weather'][0]['description']
    }
    context={
        'data':payload
    }
    print(context)
    return render(request,'index.html',context)