from django.shortcuts import render
import requests

def index(request):
	city = request.POST.get('city')
	if city==None:
		city = "Delhi"
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=df67bfd429ce5299ab02416c0bf38601'
	r = requests.get(url.format(city)).json();
	if r['cod'] == '404':
		city_weather = {
			'city': 'NOT FOUND',
			'icon':	'https://i84.photobucket.com/albums/k17/Flizia/Icons/Skulls/Skull-Rose-Color-01-50x50.jpg',
			'description': 'None',
			'temperature': '(Not Available)',
			'humidity': 'Not Available',
			'wspeed': 'Not Available',
		}
	else:
		print(r);
		city_weather = {
			'city': city,
			'icon':	'http://openweathermap.org/img/w/'+r['weather'][0]['icon']+'.png',
			'description': r['weather'][0]['description'],
			'temperature': r['main']['temp'],
			'humidity': r['main']['humidity'],
			'wspeed': r['wind']['speed'],
		}
	context = {'city_weather': city_weather}
	return render(request, 'weather/weather.html', context)