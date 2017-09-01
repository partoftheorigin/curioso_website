from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):

	print(request.user.is_authenticated())
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	title = "Login"
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/')
	return render(request, "form1.html", {"form": form, "title": title})


def register_view(request):
	title = "Signup with Curioso"
	form = UserRegisterForm(request.POST or None)
	next = request.GET.get("next")
	if form.is_valid():
		user = form.save(commit=False)
		firstname = form.cleaned_data.get('firstname')
		lastname = form.cleaned_data.get('lastname')
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		#WELCOME MAIL
		#send_mail(subject, message, from_email, to_list, fail_silentely=True)
		subject = 'Welcome to Curioso'
		message = 'Welcome to Curioso!! We very much appriciate your support. Thanks for being a part of "Curioso Family". Give a boost to your Knowledge of Analytics and Machine Learning.'
		from_email = settings.EMAIL_HOST_USER
		to_list = [user.email, settings.EMAIL_HOST_USER]
		send_mail(subject, message, from_email, to_list, fail_silently=False)
		#mail sended
		#WELCOME MAIL SCRIPT ENDED

		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('/')

	context = {
		"form": form,
		"title": title,
	}
	return render(request, "form.html", context)


def logout_view(request):
	logout(request)
	return redirect('/')
