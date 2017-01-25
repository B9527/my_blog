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
    # 分类信息
    category_list = Category.objects.all()[:6]
    # 文章归档
    archive_list = Article.objects.distinct_date()
    # 标签
    tag_list = Tag.objects.all()[:13]
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
        'WEIBO_SINA': settings.WEIBO_SINA,
        'PRO_RSS': settings.PRO_RSS,
        'PRO_EMAIL': settings.PRO_EMAIL,
        'category_list': category_list,
        'archive_list': archive_list,
        'tag_list': tag_list,
    }


def index(request):
    try:
        # 文章信息
        article_list = Article.objects.all()
        # 分页处理
        article_list = getPage(request, article_list)

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request, "index.html", locals())


def archive(request):
    try:
        # 先获取客户信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        # 文章信息
        article_list = Article.objects.filter(date_publish__icontains=year + '-' + month)
        # 分页处理
        article_list = getPage(request, article_list)

    except Exception as e:
        logger.error(e)
    return render(request, "archive.html", locals())


def tag(request):
    try:
        # 先获取客户信息
        tag_name = request.GET.get('tag', None)
        tag = Tag.objects.get(name=tag_name)
        # 文章信息
        article_list = Article.objects.filter(tag=tag)
        # 分页处理
        article_list = getPage(request, article_list)

    except Exception as e:
        logger.error(e)
    return render(request, "archive.html", locals())


# 分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 3)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list
