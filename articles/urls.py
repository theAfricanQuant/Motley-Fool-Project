from django.urls import path

from .views import HomePageView, ArticlesPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('articles/', ArticlesPageView.as_view(), name='articles_page'),
]
