from django.shortcuts import render
from .models import News
# Create your views here.

def news(request):

    news = News.objects.all()

    return render(request, 'news/news.html', {'news': news})


def news_info(request, news_id):

    news = News.objects.get(pk=news_id)

    return render(request, 'news/news_content.html', {'news': news})
