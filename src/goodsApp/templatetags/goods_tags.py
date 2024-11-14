from django import template

from goodsApp.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categories():
    
    return Categories.objects.all()
