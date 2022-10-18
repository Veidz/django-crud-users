from django.urls import path
from .views import home, create

urlpatterns = [
  path('', home),
  path('create/', create, name='create')
]
