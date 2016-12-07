# Create your views here.
from django.shortcuts import render
import logging
from django.conf import settings
from .models import *
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
    tag_list = []
    try:
        article_list = Article.objects.all()
        for article in article_list:
            tag_list = article.tag.all()

    except Exception as e:
        print(e)
        logger.error(e)
    return render(request, "index.html", locals())


def ad(request):
    return render(request, "my_test.html", locals())


def test(request):
    return render(request, "local_index.html", locals())
