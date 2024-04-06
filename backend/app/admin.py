from django.contrib import admin
from .models import Lecture, Short

class LectureAdmin(admin.ModelAdmin):
    search_fields = ['lecture_name', 'title']

class ShortAdmin(admin.ModelAdmin):
    search_fields = ['lecture__lecture_name', 'lecture__title', 'semi_title']

admin.site.register(Lecture, LectureAdmin)
admin.site.register(Short, ShortAdmin)
