from django.urls import path

from .views import main_view
from .views import home_view

urlpatterns = [
    path('', main_view, name='main'),
    path('home/', home_view, name='home')
]