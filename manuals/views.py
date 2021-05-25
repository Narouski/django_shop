from django.shortcuts import render
from . import models


def authors(request):
    author = models.Authors.objects.get(pk=1)
    ctx = {
        'author': author
    }
    return render(
        request,
        template_name=authors.html,
        context=ctx
    )
