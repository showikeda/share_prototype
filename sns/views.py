from django.shortcuts import render, redirect
from django.http import Http404
from django.http.response import JsonResponse
from . import models
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.views.generic import ListView
from django.db.models import Q


class IndexList(ListView):
    template_name = 'sns/index.html'
    queryset = Article.objects.order_by('-posted_at')
    paginate_by = 5
    model = Article

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Article.objects.filter(
                Q(title__icontains=q_word) | Q(text__icontains=q_word)
            )
        else:
            object_list = Article.objects.all()
        return object_list


@login_required
def new(request):
    template_name = "sns/new.html"
    if request.method == "POST":
        models.Article.objects.create(
            title=request.POST["title"],
            text=request.POST["text"]
        )
        # return redirect(index)
        return redirect(IndexList)
    return render(request, template_name)
    # return redirect(article_all)



class ArticleList(ListView):
    template_name = "sns/article_all.html"
    queryset = Article.objects.order_by('-posted_at')
    model = Article


def view_article(request, pk):
    comment = CommentForm(request.GET)
    template_name = 'sns/view_article.html'
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    if request.method == "POST":
        models.Comment.objects.create(text=request.POST["text"], article=article)
    context = {
        "article": article,
        "comment": comment
    }
    return render(request, template_name, context)


@login_required
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


@login_required
def delete(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    article.delete()
    # return redirect(article_all)
    return redirect(ArticleList)


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
