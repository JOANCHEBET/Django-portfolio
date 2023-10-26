from django .urls import path,include
from . import views

app_name = "Joan"
urlpatterns = [
    path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('languages/', views.languages, name='languages'),
path('services/', views.services, name='services'),
path('contacts/', views.contacts, name='contacts')
]
