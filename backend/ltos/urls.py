from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # path('/upload', upload_views.upload)
]