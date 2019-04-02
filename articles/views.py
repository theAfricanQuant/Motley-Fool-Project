# from django.shortcuts import render
from django.views.generic import TemplateView

from .utils import find_headline_article


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_article = find_headline_article()
        context['main-article'] = main_article
        return context


class ArticlesPageView(TemplateView):
    template_name = 'articles.html'
