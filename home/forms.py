from django import forms
from .models import Feedback
from .models import Writeforus

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = [
        "firstname",
        "lastname",
        "email",
        "Feedback",
        ]


class WriteforusForm(forms.ModelForm):

    class Meta:
        model = Writeforus
        fields = [
        "firstname",
        "lastname",
        "Email",
        "Profile",
        "Linkedin_Profile",
        "title",
        "image",
        "category",
        ]
