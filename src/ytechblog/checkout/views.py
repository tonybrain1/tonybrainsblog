from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import Checkout

# Create your views here.
def checkout(request):
	title = 'Checkout'
	form = Checkout(request.POST or None)
	confirm_message = None

	if form.is_valid():
		firstname = form.cleaned_data['firstname']
		lastname = form.cleaned_data['lastname']
		address = form.cleaned_data['address']
		country = form.cleaned_data['country']
		zipcode = form.cleaned_data['zipcode']
		card = form.cleaned_data['card']
		nameOfCard = form.cleaned_data['nameOfCard']
		creditCardnumber = form.cleaned_data['creditCardnumber']
		expiryDate = form.cleaned_data['expiryDate']
		CCV = form.cleaned_data['CCV']

		
  
		
		subject = 'message from my checkout MYSITE.COM'
		message = '%s %s %s %s %s %s %s %s %s %s' %(firstname, lastname, country, address, zipcode, card, nameOfCard, creditCardnumber, expiryDate, CCV)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
		title = 'Thanks'
		confirm_message = 'Purchase Successful'
		form = None

	context = {'title': title, 'form': form, 'confirm_message': confirm_message,}
	template = 'checkout.html'
	return render(request,template,context)