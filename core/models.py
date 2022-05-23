from email.policy import default
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.CharField(max_length=155)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.body[:30]}'


class AboutUsModel(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='image/aboutus')

    def __str__(self):
        return self.body[:30]


class Gallery(models.Model):
    title = models.CharField(max_length=155)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='image/gallery')

    def __str__(self):
        return self.title


class HomeSlider(models.Model):
    title = models.CharField(max_length=155)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='image/gallery')


class Stuff(models.Model):
    name = models.CharField(max_length=155)
    skill = models.CharField(max_length=155)
    # social media
    facebook = models.URLField()
    twitter = models.URLField()
    google_plus = models.URLField()
    image = models.ImageField(default='image/stuff_profile/stuff-img-01.jpg', upload_to='image/stuff_profile')
    def __str__(self):
        return f'{self.name} - {self.skill}'
