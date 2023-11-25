from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blogs', views.BlogListView.as_view(), name='blogs'),
    path('article_details/<slug:slug>', views.ArticleDetailsView.as_view(), name='article_details'),
    path('search', views.search, name='result'),
    path('categories/<int:pk>', views.categories, name='categories'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),
]
