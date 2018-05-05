from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('SNA/index.html')
	return HttpResponse(template.render({},request))

def signup1(request):
	template = template = loader.get_template('SNA/signup.html')
	return HttpResponse(template.render({},"registeration finised log in now"))

def signup(request):
	if request.method == "POST" :
		email = request.POST.get("email")
		if register(email) :
			template = loader.get_template('SNA/login.html')
		else :
			return Httpresponse("Email's already been used try another one")
	else :
		template = template = loader.get_template('SNA/signup.html')
	return HttpResponse(template.render({},"registeration finised log in now"))

def register(Email):
	if Email == "a@a.com" :
		return false
	else :
		return True

def login(request):
	template = loader.get_template('SNA/login.html')
	return HttpResponse(template.render({},request))

def home(request):
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

