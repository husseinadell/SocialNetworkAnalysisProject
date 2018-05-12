from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect

from django.template import loader
from .models import User
from .models import Post
from .models import friendShip

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
		suggestionList = friendShip.objects.exclude(user1 = user).exclude(user2 = user)
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
	return HttpResponse(template.render({'user':user,'list':list,'suggestionList':suggestionList},request))

def home2(request,email):
	#process and redirect to homepage
	template = loader.get_template('SNA/homepage.html')
		
	if  request.method == "GET" :
		user = User.objects.get(Email = email)
		list = Post.objects.order_by('scope')
		suggestionList = friendShip.objects.exclude(user1 = user).exclude(user2 = user)
	else :
		template = loader.get_template('SNA/login.html')
		return HttpResponse(template.render({},request)) 
	return HttpResponse(template.render({'user':user,'list':list,'suggestionList':suggestionList},request))


def profile(request):
	#load signup page
	template = loader.get_template('SNA/profile.html')
	return HttpResponse(template.render({},request))

def addFriendCaller(request,email1,email2):
	template = loader.get_template('SNA/homepage.html')
	friend1 = User.objects.get(Email = email1)
	friend2 = User.objects.get(Email = email2)
	list = Post.objects.order_by('scope')
	suggestionList = friendShip.objects.exclude(user1 = friend1).exclude(user2 = friend1)
		
	return HttpResponse(template.render({
'user':friend1,'list':list,'suggestionList':suggestionList},request))

def addFriend(request,email1,email2):
	if request.method == "GET":
		template = loader.get_template('SNA/homepage.html')
		friend1 = User.objects.get(Email = email1)
		friend2 = User.objects.get(Email = email2)
		newFriendShip = friendShip(user1=friend1,user2=friend2)
		newFriendShip.save()
		list = Post.objects.order_by('scope')
		suggestionList = friendShip.objects.exclude(user1 = friend1).exclude(user2 = friend1)
		return redirect ('../../home/'+email1)
		
	else :
		return HttpResponse(request)

def empty(request):
	return HttpResponse('empty path   )~: ')

