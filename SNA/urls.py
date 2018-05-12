from django.urls import path

from .models import User
from . import views

urlpatterns = [
        path('', views.index, name = 'index'),
	path('registeration/',views.signup1,name= 'signup1'),
	path('processing/',views.signup,name= 'signup'),
	path('login/',views.login,name= 'login'),
	path('home/',views.home,name= 'home'),
	path('home/<str:email>',views.home2,name= 'home2'),
	path('profile/',views.profile,name= 'profile'),
	path('addfriend/<str:email1>/<str:email2>',views.addFriend,name= 'addFriend'),
]
