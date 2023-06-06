from django import template

register = template.Library()


@register.simple_tag
def quotes_tag(quote):
    return quote["description"].upper()
