from django.urls import path

from . import views

urlpatterns = [
	path('get_all_issues/', views.get_all_issues, name='get_all_issues'),
    path('', views.home, name='home'),
]
