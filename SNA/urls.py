from django.urls import path

from . import views

urlpatterns = [
        path('p', views.index, name = "index"),
	path('',views.empty, name = "empty"),
]
