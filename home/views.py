from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import FeedbackForm
from .models import Feedback
from .forms import WriteforusForm
from .models import Writeforus


# Create your views here.

#class HomePageView(TemplateView):
    #template_name = 'home/index.html'

def index(request):
    context={

    }
    return render(request, "home/index.html", context)

def guide(request):
    context={

    }
    return render(request, "home/guide.html", context)

def privacy(request):
    context={

    }
    return render(request, "home/privacy.html", context)

def feedback(request):
    form = FeedbackForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Sucessful")
        return HttpResponseRedirect(instance.get_absolute_url_feedback())

    context = {
	   "form": form,
	}
    return render(request, "home/feedback.html", context)

def writeforus(request):
    form = WriteforusForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Sucessful")
        return HttpResponseRedirect(instance.get_absolute_url_writeforus())

    context = {
	   "form": form,
	}
    return render(request, "home/writeforus.html", context)

def career(request):
    context={

    }
    return render(request, "home/career.html", context)

def aboutus(request):
    context={

    }
    return render(request, "home/aboutus.html", context)
