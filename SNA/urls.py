from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name = 'index'),
	path('registeration/',views.signup1,name= 'signup1'),
	path('processing/',views.signup,name= 'signup'),
	path('login/',views.login,name= 'login'),
	path('home/',views.home,name= 'home'),
]
