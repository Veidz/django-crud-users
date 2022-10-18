from django.shortcuts import redirect, render
from .models import User

def home(request):
  users = User.objects.all()
  return render(request, 'index.html', {'users': users})

def create(request):
  name = request.POST.get('name')
  User.objects.create(name=name)
  return redirect(home)
