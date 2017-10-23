from django.shortcuts import render

# Create your views here.
from app01 import models
from django import forms
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets
from django.urls import reverse
class UserInfoModelForm(forms.ModelForm):

    class Meta:
        model = models.UserInfo
        fields = '__all__'
        labels = {
            'username': '用户名',
            'email': '邮箱'
        }
        help_texts = {
            'username' : '请输入用户名'
        }
        widgets = {
            'username': Fwidgets.Textarea(attrs={'class':'c1'})
        }
        error_messages = {
            # '__all__': {
            #     'required': '不能为空'
            # },
            'email':{
                'required' : '邮箱不能为空'
            }
        }
        field_classes = {
            # 'email': Ffields.URLField
        }
        localized_fields = ('ctime',)


def test(request):
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request, 'test.html', {'obj':obj})

    elif request.method == 'POST':
        obj = UserInfoModelForm(request.POST)
        # print(obj.is_valid())
        # print(obj.cleaned_data)
        # print(obj.errors.as_json)
        if obj.is_valid():
            obj.save()
        return render(request, 'test.html', {'obj':obj})


#--------------------------------------------------------

def search_article(request,*args,**kwargs):
    # print(request.path_info) #获取当前URL
    # url = reverse('article',kwargs=kwargs)
    # print(url)
    # print(kwargs.items())
    article_type_list = models.ArticleType.objects.all()
    category_list = models.Category.objects.all()
    # for i in category:
    #     print(i.caption)
    con = {}
    for k,v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            con[k] = v

    article_list = models.Article.objects.filter(**con)
    # print(article)
    return render(request,'search_article.html', {'article_list': article_list, 'article_type_list': article_type_list, 'category_list': category_list,'arg_dict':kwargs})



