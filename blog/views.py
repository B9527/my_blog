# coding:utf-8
# Create your views here.
from django.shortcuts import render
import logging
from django.conf import settings
from .models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
# Create your views here.


logger = logging.getLogger('blog.views')


def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
        'WEIBO_SINA': settings.WEIBO_SINA,
        'PRO_RSS': settings.PRO_RSS,
        'PRO_EMAIL': settings.PRO_EMAIL,

    }


def index(request):
    try:
        # 分类信息
        category_list = Category.objects.all()[:6]
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 3)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request, "index.html", locals())



