from django.urls import path

from .views import HomePageView, ArticleDetailPage


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('article/<uuid:article_uuid>', ArticleDetailPage.as_view(), name='article_page'),
]
