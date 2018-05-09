from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import Post

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
		name = request.POST.get("name")
		user_age = request.POST.get("age")
		user_org = request.POST.get("organization")
		user_phone = request.POST.get("phone_num")
		user_address = request.POST.get("address")
		user_birth_date = request.POST.get("birth_date")
		
		if register(email ) == True:
			template = loader.get_template('SNA/login.html')
			new_user = User(user_name = name,Email = email,age = user_age,works_at= 			user_org,phone_num = user_phone,address = user_address,birth_date = 				user_birth_date)
			new_user.save()
		else :
			
			return HttpResponse(template.render({},request))
	else :
		template = loader.get_template('SNA/signup.html')
	return HttpResponse(template.render({},request))

def register(email):
	#check if email existed or not
	if User.objects.filter(Email = email):
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
		email = request.POST.get("email")
		password = request.POST.get("password")
		user = User.objects.get(Email = email)
		list = Post.objects.order_by('scope')
		if user:
			if user.password != password:
				template = loader.get_template('SNA/login.html')
				return HttpResponse(template.render({},request))
		else :
			template = loader.get_template('SNA/login.html')
			return HttpResponse(template.render({},request))  
	else :
		template = loader.get_template('SNA/login.html')
		return HttpResponse(template.render({},request)) 
	return HttpResponse(template.render({'user':user,'list':list},request))

def profile(request):
	#load signup page
	template = loader.get_template('SNA/profile.html')
	return HttpResponse(template.render({},request))

def empty(request):
	return HttpResponse('empty path   )~: ')

