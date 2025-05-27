from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentForm

# Create your views here.
def home(request):
    return render(request, 'profiles/home.html')

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('profile', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'profiles/register.html', {'form': form})

def profile(request, student_id):
    student = Students.objects.get(id=student_id)
    return render(request, 'profiles/profile.html', {'student': student})

def all_profiles(request):
    students = Students.objects.all()
    return render(request, 'profiles/all_profiles.html', {'students': students})