from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blogs', views.BlogListView.as_view(), name='blogs'),
    path('details/<slug:slug>', views.blog_details, name='details'),
    path('search/', views.search, name='search'),
]
