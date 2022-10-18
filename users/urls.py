from django.urls import path
from .views import home, create, updateDetails, update

urlpatterns = [
  path('', home),
  path('create/', create, name='create'),
  path('update-details/<int:id>', updateDetails, name='updateDetails'),
  path('update/<int:id>', update, name='update'),
]
