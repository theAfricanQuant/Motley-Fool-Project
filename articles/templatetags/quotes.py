from django import template

register = template.Library()


@register.simple_tag
def quotes_tag(quote):
    new_desc = quote["description"].upper()
    return new_desc
