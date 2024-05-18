from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lecture
from .forms import LectureForm
def index(request):
    lecture = Lecture.objects.all()
    context = {'lecture': lecture}
    return render(request, 'home.html', context)

def upload(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Assuming you have a lecture list view
    else:
        form = LectureForm()
    return render(request, 'upload.html', {'form': form})
