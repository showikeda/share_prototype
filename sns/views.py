from django.shortcuts import render, redirect
from django.http import Http404
from django.http.response import JsonResponse
from . import models


def index(request):
    template_name = "sns/index.html"
    context = {"articles": models.Article.objects.all()}
    return render(request, template_name, context)


def new(request):
    template_name = "sns/new.html"
    if request.method == "POST":
        models.Article.objects.create(title=request.POST["title"], text=request.POST["text"])
    return render(request, template_name)


def article_all(request):
    template_name = "sns/article_all.html"
    context = {"articles": models.Article.objects.all()}
    return render(request, template_name, context)


def view_article(request, pk):
    template_name = 'sns/view_article.html'
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    if request.method == "POST":
        models.Comment.objects.create(text=request.POST["text"], article=article)
    context = {"article": article}
    return render(request, template_name, context)


def edit(request, pk):
    template_name = "sns/edit.html"
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    if request.method == "POST":
        article.title = request.POST["title"]
        article.text = request.POST["text"]
        article.save()
        return redirect(view_article, pk)
    context = {"article": article}
    return render(request, template_name, context)


def delete(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    article.delete()
    return redirect(article_all)


def like(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    article.like += 1
    article.save()
    return redirect(view_article, pk)


def api_like(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    article.like += 1
    article.save()
    return JsonResponse({"like": article.like})
