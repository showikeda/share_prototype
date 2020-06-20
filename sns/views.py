from django.shortcuts import render

def index(request):
    template_name = "sns/index.html"
    return render(request, template_name)

def new(request):
    template_name = "sns/new.html"
    return render(request, template_name)
