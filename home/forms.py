from django import forms
from .models import Feedback
from .models import Writeforus
from .models import Career

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = [
        "firstname",
        "lastname",
        "email",
        "feedback",
        ]

        widgets = {
            'firstname' : forms.TextInput(attrs={'placeholder' : 'First Name'}),
            'lastname' : forms.TextInput(attrs={'placeholder' : 'Last Name'}),
            'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
            'feedback' : forms.TextInput(attrs={'placeholder' : 'Your Feedback'}),
        }


class WriteforusForm(forms.ModelForm):

    class Meta:
        model = Writeforus
        fields = [
        "firstname",
        "lastname",
        "email",
        "linkedin_profile",
        "title",
        "attachment",
        "category",
        ]

        widgets = {
            'firstname' : forms.TextInput(attrs={'placeholder' : 'First Name'}),
            'lastname' : forms.TextInput(attrs={'placeholder' : 'Last Name'}),
            'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
            'linkedin_profile' : forms.TextInput(attrs={'placeholder' : 'LinkedIn Profile'}),
            'title' : forms.TextInput(attrs={'placeholder' : 'Title'}),
            'category' : forms.TextInput(attrs={'placeholder' : 'Category'}),
        }

class CareerForm(forms.ModelForm):

    class Meta:
        model = Career
        fields = [
        "firstname",
        "lastname",
        "email",
        "attachment",
        "linkedin_profile",
        "github_profile",
        "coding_profile",
        "additional_information",
        ]

        widgets = {
            'firstname' : forms.TextInput(attrs={'placeholder' : 'First Name'}),
            'lastname' : forms.TextInput(attrs={'placeholder' : 'Last Name'}),
            'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
            'linkedin_profile' : forms.TextInput(attrs={'placeholder' : 'LinkedIn Profile'}),
            'github_profile' : forms.TextInput(attrs={'placeholder' : 'Github Profile'}),
            'coding_profile' : forms.TextInput(attrs={'placeholder' : 'Coding Profile'}),
            'additional_information' : forms.TextInput(attrs={'placeholder' : 'Additional Information'}),
        }
