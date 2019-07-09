from django.shortcuts import render
from django.http import HttpResponse
from .models import Forecast
from datetime import datetime as dt
import datetime
import pytz

# Create your views here.
def index(request):
	if request.method == 'POST':
		startdate = dt.now(pytz.timezone('Europe/Kiev'))
		enddate = startdate + datetime.timedelta(days=7)
		city = request.POST.get('city', '')
		forecasts = list(Forecast.objects.order_by('pub_date').filter(
			place=city, pub_date__range=[startdate, enddate]))[-8:]
		cities = list(Forecast.objects.values('place').distinct())
		context = {
			'forecast' : forecasts,
			'cities' : [{'city' : i, 'selected' : i['place'] == city} for i in cities]
		}
		print(context['cities'])
		return render(request, "index.html", context)
	else:
		startdate = dt.now()
		enddate = startdate + datetime.timedelta(days=7)
		forecasts = list(Forecast.objects.order_by('pub_date').filter(
			place="London", pub_date__range=[startdate, enddate]))[-8:]
		cities = list(Forecast.objects.values('place').distinct())
		context = {
			'forecast' : forecasts,
			'cities' : [{'city' : i, 'selected' : i['place'] == "London"} for i in cities]
		}
		return render(request, "index.html", context)

def visual(request):
	return render(request, "contact.html")