from django.shortcuts import render
from . import models


def authors(request, author_id):
    author = models.Authors.objects.get(pk=author_id)
    ctx = {
        'author': author
    }
    return render(
        request,
        template_name='authors.html',
        context=ctx
    )


def author_list(request):
    authors_list = models.Authors.all()
    ctx = {
        'authors_list': authors_list
    }
    return render(
        request,
        template_name='authors_list.html',
        context=ctx
    )