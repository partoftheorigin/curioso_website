from django.contrib.contenttypes.models import ContentType
from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404


from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q

from comments.models import Comment
from comments.forms import CommentForm

from .forms import PostForm
from .models import Post


#def handler404(request):
    #return render(request, '404.html', status=404)

def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Sucessful")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
	   "form": form,
	}
    return render(request, "curiosoblog/create.html", context)



def detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    share_string = quote_plus(instance.content)

    initial_data = {
            "content_type": instance.get_content_type,
            "object_id": instance.id,
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated():

        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
			user=request.user,
			content_type=content_type,
			object_id=obj_id,
			content=content_data,
            parent=parent_obj,

            )

        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    comments = instance.comments#Comment.objects.filter_by_instance(instance)
    context = {
              "title": instance.title,
              "instance" : instance,
              "share_string": share_string,
              "comments": comments,
              "comment_form": form,
    }

    return render(request, "curiosoblog/detail.html", context)

def list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active()#.order_by("-timestamp")
    if request.user.is_staff or not request.user.is_superuser:                #display list(curiosoblog)
        queryset_list = Post.objects.all()#including draft

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
     ).distinct()

    paginator = Paginator(queryset_list, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
        # If page is not an integer, deliver first page.
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
		# If page is out of range (e.g. 9999), deliver last page of results.
    context = {
              "object_list" : queryset,
              "title":"list",
              "page_request_var": page_request_var,
              "today": today,
               }

    return render(request, "curiosoblog/list.html", context)

def update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessful")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
              "title": instance.title,
              "instance" : instance,
              "form" : form,
              }
    return render(request, "curiosoblog/create.html", context)


def delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Sucessful Deleted")
    return redirect("curiosoblog:list")


def handler404(request):
    return render(request, '404.html', status=404)


def handler403(request):
    return render(request, '403.html', status=403)
