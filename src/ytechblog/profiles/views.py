from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Flight

# Create your views here.
#def index(request):
	#context = {
	    #"flights": Flight.objects.all()
	#}
	#return render(request, "index.html", context)

def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)

def flight(request, flight_id):
	try:
		flight = Flight.objects.get(pk=flight_id)
	except Flight.DoesNotExist:
		raise Http404("Flight does not exist.")
	context = {
	"flight": flight,
	"passengers": flight.passengers.all()
	}
	return render(request, "flight.html", context)

def articles(request):


        headers = {
            'Authorization': 'Bearer SECRET_KEY',
            'Content-Type': 'application/json',
        }
        
        data = {"reference": reference, "amount": amount, "email": email}
        
        response = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json=data)
	context = {}
	template = 'articles.html'
	return render(request,template,context)


