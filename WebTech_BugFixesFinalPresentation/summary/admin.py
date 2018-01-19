from django.contrib import admin
from .models import Summary
from .models import Book
from .models import Subject
from .models import University

admin.site.register(Summary)
admin.site.register(Book)
admin.site.register(Subject)
admin.site.register(University)
