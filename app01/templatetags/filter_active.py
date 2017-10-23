
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


'''
        <span><a href="/search_article-0-{{ arg_dict.category_id }}.html">全部</a></span>
        
        {% for m in article_type_list %}
            {% if m.id == arg_dict.article_type_id %}
                <a class="active" href="/search_article-{{ m.id }}-{{ arg_dict.category_id }}.html"> {{ m.caption }}</a>
            {% else %}
                <a href="/search_article-{{ m.id }}-{{ arg_dict.category_id }}.html"> {{ m.caption }}</a>
            {% endif %}
        {% endfor %}

'''
'''
        {% if arg_dict.category_id == 0 %}
            <span><a class="active" href="/search_article-{{ arg_dict.article_type_id }}-0.html">全部</a></span>
        {% else %}
            <span><a href="/search_article-{{ arg_dict.article_type_id }}-0.html">全部</a></span>
        {% endif %}
        
        {% for c in category_list %}
            {% if c.id == arg_dict.category_id %}
                <a class="active" href="/search_article-{{ arg_dict.article_type_id }}-{{ c.id }}.html">{{ c.caption }}</a>
            {% else %}
                <a href="/search_article-{{ arg_dict.article_type_id }}-{{ c.id }}.html">{{ c.caption }}</a>
            {% endif %}
        {% endfor %}        
'''

@register.simple_tag
def fa1(arg_dict,k):
    n1 = arg_dict['category_id']
    n2 = arg_dict['article_type_id']
    if k == 'category_id':
        # print('n1: %s ----- n2: %s' %(n1,n2))
        if n2 == 0:
            ret = '<span><a class="active" href = "/search_article-0-%s.html"> 全部 </a></span>' % n1
        else:
            ret = '<span><a href = "/search_article-0-%s.html"> 全部 </a></span>' % n1
    else:
        if n1 == 0:
            ret = '<span><a class="active" href = "/search_article-%s-0.html"> 全部 </a></span>' % n2
        else:
            ret = '<span><a href = "/search_article-%s-0.html"> 全部 </a></span>' % n2
    return mark_safe(ret)


@register.simple_tag
def fa2(arg_dict, article_type_list):
    ret = []
    n1 = arg_dict['category_id']
    n2 = arg_dict['article_type_id']
    for c in article_type_list:
        # print('n2: %s' %n2)
        if c.id == n2:
            data = '<a class ="active" href="/search_article-%s-%s.html">%s</a>' % (c.id, n1, c.caption)
        else:
            data = '<a href="/search_article-%s-%s.html">%s</a>' % (c.id,n1, c.caption)
        ret.append(data)
    else:
        pass
    # print(''.join(ret))
    return mark_safe(''.join(ret))

@register.simple_tag
def fa3(arg_dict,category_list):
    ret = []
    n1 = arg_dict['category_id']
    n2 = arg_dict['article_type_id']
    for c in category_list:
        if c.id == n1:
            data = '<a class ="active" href="/search_article-%s-%s.html">%s</a>' %(n2,c.id,c.caption)
        else:
            data = '<a href="/search_article-%s-%s.html">%s</a>' %(n2,c.id,c.caption)
        ret.append(data)
    return mark_safe(''.join(ret))


#把fa2,fa3合并
@register.simple_tag
def fa5(arg_dict, article_type_list,category_list,k):
    ret = []
    n1 = arg_dict['category_id']
    n2 = arg_dict['article_type_id']
    if k == 'article_type_id':
        for c in article_type_list:
            if c.id == n2:
                data = '<a class ="active" href="/search_article-%s-%s.html">%s</a>' % (c.id, n1, c.caption)
            else:
                data = '<a href="/search_article-%s-%s.html">%s</a>' % (c.id,n1, c.caption)
            ret.append(data)
    else:
        for c in category_list:
            if c.id == n1:
                data = '<a class ="active" href="/search_article-%s-%s.html">%s</a>' % (n2, c.id, c.caption)
            else:
                data = '<a href="/search_article-%s-%s.html">%s</a>' % (n2, c.id, c.caption)
            ret.append(data)
    return mark_safe(''.join(ret))


