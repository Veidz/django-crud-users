from django.shortcuts import redirect, render
from django.contrib import messages

from users.utils.validations import Validations
from .models import User

def home(request):
  users = User.objects.all()
  return render(request, 'index.html', {'users': users})

def create(request):
  name = request.POST.get('name')

  if name == '':
    messages.info(request, 'Name can not be empty')
    return redirect(home)
  elif len(name) < 3:
    messages.info(request, 'Name must be at least 3 characters long')
    return redirect(home)
  elif Validations.containsNumber(name):
    messages.info(request, 'Name cannot contain numbers')
    return redirect(home)

  User.objects.create(name=name)
  return redirect(home)
    
def updateDetails(request, id):
  user = User.objects.get(id=id)
  return render(request, 'update.html', {'user': user})

def update(request, id):
  name = request.POST.get('name')

  if name == '':
      messages.info(request, 'New name can not be empty')
      return redirect(updateDetails, id)
  elif len(name) < 3:
      messages.info(request, 'New name must be at least 3 characters long')
      return redirect(updateDetails, id)
  elif Validations.containsNumber(name):
      messages.info(request, 'New name cannot contain numbers')
      return redirect(updateDetails, id)

  user = User.objects.get(id=id)
  user.name = name
  user.save()
  return redirect(home)

def delete(request, id):
  user = User.objects.get(id=id)
  user.delete()
  return redirect(home)
