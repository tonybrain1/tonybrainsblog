from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def signup_view(request):
	if request.method == "POST":
	    form = UserCreationForm(request.POST)
	    if form.is_valid():
	    	user = form.save()
	    	login(request, user)

	    	return HttpResponseRedirect(reverse("users:article_list"))
	    	#return redirect("users:home")
	else:
		form = UserCreationForm()
		
	return render(request, "accounts/signup.html", {"form":form})

def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
			    return HttpResponseRedirect(reverse("users:article_list"))


	else:
		form = AuthenticationForm()
	return render(request, "accounts/login.html", {"form":form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:article_list"))
