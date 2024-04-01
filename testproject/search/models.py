from django.db import models

# Create your models here.
class accounts(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class News(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class Company(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class Index(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class Faq(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class Contact(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class Service(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class Service2(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField()

class Comment(models.Model):
    content = models.CharField(max_length = 100)


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    details = models.TextField()