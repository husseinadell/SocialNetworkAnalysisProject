from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	#load start page
	template = loader.get_template('SNA/index.html')
	return HttpResponse(template.render({},request))

def signup1(request):
	#load signup page
	template = loader.get_template('SNA/signup.html')
	return HttpResponse(template.render({},request))

def signup(request):
	#process and redirect to login page if new email else redirect to sinup again
	template = loader.get_template('SNA/signup.html')
	if request.method == "POST" :
		email = request.POST.get("email")
		if register(email ) == True:
			template = loader.get_template('SNA/login.html')
		else :
			
			return HttpResponse(template.render({},request))
	else :
		template = loader.get_template('SNA/signup.html')
	return HttpResponse(template.render({},request))

def register(Email):
	#check if email existed or not
	if Email == 'a@a.com':
		return False
	else :
		return True

def login(request):
	#load login page
	template = loader.get_template('SNA/login.html')
	return HttpResponse(template.render({},request))

def home(request):
	#process and redirect to homepage
	template = loader.get_template('SNA/homepage.html')
		
	if request.method == "POST":
		name = request.POST.get("email")
		password = request.POST.get("password")
	else :
		template = loader.get_template('SNA/login.html')
		return HttpResponse(template.render({},request)) 
	return HttpResponse(template.render({'name':name,'password':password},request))

def empty(request):
	return HttpResponse('empty path   )~: ')

