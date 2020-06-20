from django.shortcuts import render
from . import models

def index(request):
    template_name = "sns/index.html"
    return render(request, template_name)

def new(request):
    template_name = "sns/new.html"
    if request.method == "POST":
        models.Article.objects.create(title=request.POST["title"], text=request.POST["text"])
    return render(request, template_name)
