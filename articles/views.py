# from django.shortcuts import render
from django.views.generic import TemplateView

from .utils import find_headline_article, find_random_three_articles


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_article = find_headline_article()
        extra_articles = find_random_three_articles()
        context['main_article'] = main_article
        context['random_articles'] = extra_articles
        return context


class ArticlesPageView(TemplateView):
    template_name = 'articles.html'
