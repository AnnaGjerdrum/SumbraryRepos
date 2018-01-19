from django.db import models
from django.utils import timezone


class Summary(models.Model):
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    rating = models.PositiveIntegerField()
    numRates = models.PositiveIntegerField()
    filepath = models.TextField()
    subject = models.TextField(max_length=200)
    book = models.TextField(max_length=200)
    university = models.TextField(max_length=100, null=True)
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    university = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    subjectCode = models.CharField(max_length=10)
    subjectName = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    university = models.CharField(max_length=100, null=True)
    book = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.subjectName

class University(models.Model):
    universityName = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    country = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.universityName
