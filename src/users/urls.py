from django.urls import path

from .views import login_view
from .views import RegisterView
from .views import logout_view
from .views import ProfileView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view() , name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]
