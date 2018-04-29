from django.shortcuts import render, redirect
from django.views import generic
from .forms import ContactForm

from .models import Zoo, Exhibit, Animal

# Create your views here.

def index(request):
	temporaryData = "Bill"
	return render(
		request,
		"index.html",
		context = { 'temporaryData' : temporaryData },
	)

def aboutus(request):
	return render(
		request,
		"zoo/aboutus.html",
		context = {},
	)

def contactus(request):
	if request.method == 'GET':
		form = ContactForm()
		return render(request, "zoo/contactus.html", {'form': form})
	return redirect('/zoo')


class ZooListView(generic.ListView):
    model = Zoo

class ZooDetailView(generic.DetailView):
    model = Zoo

class ExhibitDetailView(generic.DetailView):
    model = Exhibit

class AnimalDetailView(generic.DetailView):
    model = Animal
