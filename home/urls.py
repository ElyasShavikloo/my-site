from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='main'),
    path('about', views.about, name='about'),
    path('contact', views.ContactUsView.as_view(), name='contact')
]
