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
	path('profile/<int:pk>',views.visitprofile,name= 'visitprofile'),
	path('addfriend/<str:email1>/<str:email2>',views.addFriend,name= 'addFriend'),
	path('group/<int:id>',views.visitgroup,name= 'visitgorup'),
	path('create_post/<int:pk>',views.create_post,name= 'create_post'),
	path('create_comment/<int:post_pk>/<int:user_pk>',views.create_comment,name= 'create_comment'),
	path('delete_comment/<int:pk>/<int:post_pk>',views.delete_comment,name= 'delete_comment'),
	path('post/<int:pk>',views.visit_post,name= 'visit_post'),
	path('create_like/<int:post_pk>/<int:user_pk>',views.create_like,name= 'create_like'),
	path('delete_like/<int:post_pk>/<int:pk>',views.delete_like,name= 'delete_like'),
	path('visitprofile/<int:pk>/<int:user_pk>',views.visitprofile,name= 'visitprofile'),
]	
