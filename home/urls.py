from django.urls import path
from .views import homeView

urlpatterns = [
    path('tanvir/', homeView, name='home'),
]
