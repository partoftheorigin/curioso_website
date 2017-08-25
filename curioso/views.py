from django.shortcuts import render_to_response 
from django.templates import RequestContext
from django.conf import settings


def handler404(request):
    return render(request, '404.html', status=404)


def handler403(request):
    return render(request, '403.html', status=403)
