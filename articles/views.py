# from django.shortcuts import render
from django.views.generic import TemplateView

from .utils import (
    find_headline_article,
    find_random_three_articles,
    fetch_single_article,
    find_three_random_quotes,
)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_article = find_headline_article()
        extra_articles = find_random_three_articles()
        context["main_article"] = main_article
        context["random_articles"] = extra_articles
        return context


class ArticleDetailPage(TemplateView):
    template_name = "article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uuid = self.kwargs["article_uuid"]
        article = fetch_single_article(str(uuid))
        context["article"] = article
        quotes = find_three_random_quotes()
        context["quotes"] = quotes
        return context
