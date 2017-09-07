from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Feedback(models.Model):
    firstname = models.CharField(max_length=120,verbose_name=u"")
    lastname = models.CharField(max_length=120,verbose_name=u"")
    email = models.EmailField(verbose_name=u"")
    feedback = models.TextField(verbose_name=u"")

    def __unicode__(self):
        return self.firstname

    def __str__(self):
        return self.firstname

    def get_absolute_url_feedback(self):
        return reverse("home:feedback")


class Writeforus(models.Model):
    firstname = models.CharField(max_length=120,verbose_name=u"",help_text="Field does not contain blankspace if added, it will be automatically removed")
    lastname = models.CharField(max_length=120,verbose_name=u"")
    email = models.EmailField(verbose_name=u"")
    linkedin_profile = models.CharField(max_length=120, null=True,blank=True,verbose_name=u"")
    title = models.CharField(max_length=120,verbose_name=u"")
    attachment = models.FileField(verbose_name=u"",help_text="Upload your content here Doc/pdf")
    category= models.CharField(max_length=120,verbose_name=u"")

    def __unicode__(self):
        return self.firstname

    def __str__(self):
        return self.firstname

    def get_absolute_url_writeforus(self):
        return reverse("home:writeforus")

class Career(models.Model):
    firstname = models.CharField(max_length=120,verbose_name="")
    lastname = models.CharField(max_length=120,verbose_name="")
    email = models.EmailField(verbose_name=u"")
    attachment = models.FileField(verbose_name=u"",help_text="Upload your Resume here Doc/pdf")
    linkedin_profile = models.CharField(max_length=120, null=True,blank=True,verbose_name=u"")
    github_profile = models.CharField(max_length=120, null=True,blank=True,verbose_name=u"")
    coding_profile = models.CharField(max_length=120, null=True,blank=True,verbose_name=u"")
    additional_information  = models.TextField(null=True,blank=True,verbose_name=u"")


    def __unicode__(self):
        return self.firstname

    def __str__(self):
        return self.firstname

    def get_absolute_url_career(self):
        return reverse("home:career")
