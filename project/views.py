from django.shortcuts import render

def home(request):
    templates_name = "index.html"
    return render(request, templates_name)
