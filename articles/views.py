# from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy, reverse
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

        # Returns the hightlighed article at the top of the homepage
        main_article = find_headline_article()
        context["main_article"] = main_article

        # Returns 3 random articles to populate the rest of the homepage
        extra_articles = find_random_three_articles()
        context["random_articles"] = extra_articles

        # Return all context
        return context


class ArticleDetailPage(FormView):
    template_name = "article.html"
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("homepage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Captures the articles UUID from the url
        uuid = self.kwargs["article_uuid"]

        # Returns the selected article content for context
        article = fetch_single_article(str(uuid))
        context["article"] = article

        # Returns random articles for the sidebar
        extra_articles = find_random_three_articles()
        context["random_articles"] = extra_articles

        # Returns the 3 random quotes for the sidebar for context
        quotes = find_three_random_quotes()
        context["quotes"] = quotes

        # Return the comments for current article.
        # Displays in reverse datetime order
        comments = Comment.objects.filter(article_uuid=uuid).order_by('-datetime')
        context["comments"] = comments

        # Return ALL THE THINGS!
        return context

    def form_valid(self, form):
        # Collect and clean form data
        comment = form.cleaned_data["comment"]
        uuid = form.cleaned_data["article_uuid"]

        # Create new Comment object and Save to DB
        new_comment = Comment(comment=comment, article_uuid=uuid)
        new_comment.save()

        # Return the user to the current article page
        return HttpResponseRedirect(reverse('article_page', kwargs={'article_uuid': uuid}))
