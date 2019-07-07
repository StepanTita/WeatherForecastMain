from django.shortcuts import render
from django.http import HttpResponse
from .models import Forecast
from datetime import datetime as dt
import datetime

# Create your views here.
def index(request):
	if request.method == 'POST':
		startdate = dt.now()
		enddate = startdate + datetime.timedelta(days=7)
		city = request.POST.get('city', '')
		forecasts = list(Forecast.objects.order_by('pub_date').filter(
			place=city, pub_date__range=[startdate, enddate]))[-8:]
		context = {'forecast' : forecasts}
		return render(request, "index.html", context)
	else:
		startdate = dt.now()
		enddate = startdate + datetime.timedelta(days=7)
		forecasts = list(Forecast.objects.order_by('pub_date').filter(
			place="London", pub_date__range=[startdate, enddate]))[-8:]
		context = {'forecast' : forecasts}
		return render(request, "index.html", context)

def visual(request):
	return render(request, "contact.html")