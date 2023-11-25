from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='main'),
    path('about', views.about, name='about'),
    path('contact', views.ContactUsView.as_view(), name='contact'),
    path('credentials', views.credentials, name='credentials'),
    path('suggestion', views.suggestion, name='suggestion'),
    path('projects_list', views.ProjectsListView.as_view(), name='projects_list'),
    path('project_details/<slug:slug>', views.ProjectDetailsView.as_view(), name='project_detail'),
]
