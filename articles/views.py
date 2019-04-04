# from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

from .models import Comment
from .forms import CommentForm
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


class ArticleDetailPage(FormView):
    template_name = "article.html"
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("homepage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uuid = self.kwargs["article_uuid"]

        article = fetch_single_article(str(uuid))
        context["article"] = article

        quotes = find_three_random_quotes()
        context["quotes"] = quotes

        return context

    def form_valid(self, form):
        comment = form.cleaned_data["comment"]
        uuid = form.cleaned_data["article_uuid"]

        new_comment = Comment(comment=comment, article_uuid=uuid)
        new_comment.save()

        return HttpResponseRedirect(self.get_success_url())
