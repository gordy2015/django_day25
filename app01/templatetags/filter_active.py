
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def fa1(arg_dict,a1,a2):
    if a1 == a2:
        ret = '<span><a class="active" href = "/search_article-0-%s.html"> 全部 </a></span>' % arg_dict['category_id']
    else:
        ret = '<span><a href = "/search_article-0-%s.html"> 全部</a></span>' % arg_dict['category_id']
    return mark_safe(ret)