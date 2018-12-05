from django.shortcuts import render
from django.http import HttpResponse
from news.models import Column,Article
from django.shortcuts import redirect


# Create your views here.
def index(request):
    home_display_columns = Column.objects.filter(home_display=True)#filter选择符合条件的对象
    nav_display_columns = Column.objects.filter(nav_display=True)

    return render(request,'index.html',{
        'home_display_columns':home_display_columns,
        'nav_display_columns':nav_display_columns,
    })
    #columns=Column.objects.all()
    #return render(request,'index.html',{'columns':columns})
    #return HttpResponse(u'欢迎来到图书馆，我是图书馆馆长')

def column_detail(request,column_slug):
    column=Column.objects.get(slug=column_slug)
    return render(request,'news/column.html',{'column':column})
    #return HttpResponse('column slug:'+column_slug)

def article_detail(request,pk,article_slug):
    #article=Article.objects.filter(slug=article_slug)[0]
    article=Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article,permanent=True)
    return render(request,'news/article.html',{'article':article})
    #return HttpResponse('article slug:'+article_slug)