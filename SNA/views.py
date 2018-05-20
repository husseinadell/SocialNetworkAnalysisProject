from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse

from django.shortcuts import redirect

from django.template import loader
from .models import User
from .models import Post,Comment,Like
from .models import friendShip
from .models import groupMembers
from .forms import PostForm, CommentForm

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


def addPost(request):
	user = request.user
	newPost = Post(user=user,)
	
	

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
		my_friendships = friendShip.objects.filter(user1=user)
		my_friends = [user]
		for friendship in my_friendships:
			my_friends.append(friendship.user2)
		my_friends.pop(0)
		mutual = [user]
		for friend in my_friends:
			friend_friendships = friendShip.objects.filter(user1 = friend)
			for f in friend_friendships:
				if f.user2 not in mutual:
					mutual.append(f.user2)
		
		for f in range (len(mutual)):
			if mutual[f] in my_friends:
				del mutual[f]	
		suggestionList1 = my_friends
		suggestionList2 = mutual
		mutual.pop(0)
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
	return HttpResponse(template.render({'user':user,'list':list,'suggestionList1':suggestionList1,'suggestionList2':suggestionList2},request))

def home2(request,email):
	#process and redirect to homepage
	template = loader.get_template('SNA/homepage.html')
		
	if  request.method == "GET" or request.method == "POST":
		user = User.objects.get(Email = email)
		
		list = Post.objects.order_by('scope')
		my_friendships = friendShip.objects.filter(user1=user)
		my_friends = [user]
		for friendship in my_friendships:
			my_friends.append(friendship.user2)
		my_friends.pop(0)
		mutual = [user]
		for friend in my_friends:
			friend_friendships = friendShip.objects.filter(user1 = friend)
			for f in friend_friendships:
				if f.user2 not in mutual:
					mutual.append(f.user2)
		mutual.pop(0)
		x = len(mutual)
		mutual1 = [user]
		for friend in my_friends:
	#		print(mutual[f])
	#		print("-------")
		#print(my_friends)
			
			if friend in mutual or mutual1:
				continue
			else: 
				mutual1.append(friend)	
		mutual1.pop(0)
		suggestionList1 = my_friends
		suggestionList2 = mutual1
		
	else :
		print(email)
		template = loader.get_template('SNA/login.html')
		return HttpResponse(template.render({},request)) 
	return HttpResponse(template.render({'user':user,'list':list,'suggestionList1':suggestionList1,'suggestionList2':suggestionList2},request))

def visitgroup(request,id):
	#process and redirect to homepage
	template = loader.get_template('SNA/group.html')
	list = Post.objects.order_by('scope')
	suggestionList = friendShip.objects.exclude(user1 = user).exclude(user2 = user)
	return HttpResponse(template.render({'id':id,'list':list,'suggestionList':suggestionList},request))



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
		newFriendShip1 = friendShip(user1=friend1,user2=friend2)
		newFriendShip2 = friendShip(user1=friend2,user2=friend1)
		newFriendShip1.save()
		newFriendShip2.save()
		list = Post.objects.order_by('scope')
		suggestionList = friendShip.objects.exclude(user1 = friend1).exclude(user2 = friend1)
		print(email1)
		return redirect ('../../home/'+email1)
		
	else :
		return HttpResponse(request)

def empty(request):
	return HttpResponse('empty path   )~: ')


def create_post(request, pk):
	user = User.objects.get(id=pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = user
			post.scope = Post.TIMELINE
			post.save()
			return redirect ('../../SNA/home/'+user.Email)
	else:
		form = PostForm()
	template = loader.get_template("SNA/create_post.html")

	return HttpResponse(template.render({'form': form},request))

def delete_post(request, pk):
	post = Post.objects.get(id=pk)
	post.delete()
	return HttpResponseRedirect(reverse('home'))

def delete_comment(request, pk,post_pk):
	comment = Comment.objects.get(id=pk)
	comment.delete()
	return redirect ('../../post/'+str(post_pk))

def create_comment(request, post_pk, user_pk):
	post = Post.objects.get(id=post_pk)
	user = User.objects.get(id=user_pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit="False")
			comment.post = post
			comment.user = user
			comment.save()
			return redirect ('../../post/'+str(post_pk))
	else:
		form = CommentForm()
	
	
	template = loader.get_template("SNA/create_comment.html")

	return HttpResponse(template.render({'form': form},request))


def create_like(request, post_pk,user_pk):
	post = Post.objects.get(id=post_pk)
	user = User.objects.get(id=user_pk)
	email = user.Email
	if len(Like.objects.filter(user=user,post=post)) == 0:
		Like.objects.create(user=user,post=post,scope=Like.POST)
 	
	return redirect ('../../post/'+str(post_pk))

def delete_like(request, post_pk, pk):
	user = User.objects.get(id=pk)
	post = Post.objects.get(id=post_pk)
	if not len(Like.objects.filter(user=user,post=post)) == 0:
		like = Like.objects.get(user=user,post=post)
		like.delete()
	return redirect ('../../post/'+str(post_pk))

def visit_post(request,pk):
	post = Post.objects.get(id=pk)
	commentList = Comment.objects.filter(post=post)
	likeList = Like.objects.filter(post=post)
	template = loader.get_template("SNA/post.html")

	return HttpResponse(template.render({'post': post,'likeList': likeList,'commentList': commentList},request))

def visitprofile(request,pk,user_pk):
	user = User.objects.get(id=pk)
	main_user = User.objects.get(id=user_pk)
	post_list = Post.objects.filter(user=user)
	my_friendships = friendShip.objects.filter(user1=user)
	my_friends = [user]
	for friendship in my_friendships:
		my_friends.append(friendship.user2)
	my_friends.pop(0)
	template = loader.get_template("SNA/visitprofile.html")
	
	return HttpResponse(template.render({'user': user,'post_list':post_list,'my_friends':my_friends,'main_user':main_user},request))
	
	

