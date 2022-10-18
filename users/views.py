from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User

def home(request):
  users = User.objects.all()
  return render(request, 'index.html', {'users': users})

def create(request):
  name = request.POST.get('name')

  if name == '':
    messages.info(request, 'Name is required')
    return redirect(home)
  if len(name) < 3:
     messages.info(request, 'Name need to be at least 3 characters')
     return redirect(home)
  else:
    User.objects.create(name=name)
    return redirect(home)
    
def updateDetails(request, id):
  user = User.objects.get(id=id)
  return render(request, 'update.html', {'user': user})

def update(request, id):
  name = request.POST.get('name')
  user = User.objects.get(id=id)
  user.name = name
  user.save()
  return redirect(home)

def delete(request, id):
  user = User.objects.get(id=id)
  user.delete()
  return redirect(home)
