from django.shortcuts import render
from .models import User

def home(request):
  users = User.objects.all()
  return render(request, 'index.html', {'users': users})
