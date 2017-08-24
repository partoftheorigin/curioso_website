from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Feedback(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    Feedback = models.TextField()

    def __unicode__(self):
        return self.firstname

    def __str__(self):
        return self.firstname

    def get_absolute_url_feedback(self):
        #return "/post/%s/" %(self.id)
        return reverse("home:feedback")


class Writeforus(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    Email = models.EmailField()
    Profile = models.CharField(max_length=120)
    Linkedin_Profile = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=120)
    image = models.ImageField()
    category= models.CharField(max_length=120)
    content = models.FileField()



    def __unicode__(self):
        return self.firstname

    def __str__(self):
        return self.firstname

    def get_absolute_url_writeforus(self):
        #return "/post/%s/" %(self.id)
        return reverse("home:writeforus")
