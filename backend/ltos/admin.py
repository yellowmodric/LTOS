from django.contrib import admin

# Register your models here.
from .models import Short
from .models import Lecture

admin.site.register(Short)
admin.site.register(Lecture)