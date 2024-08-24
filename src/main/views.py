from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def main_view(request):
    return render(request, "views/main.html", {"name":"AutoMax"})#dynamically injection data in html
    # return HttpResponse("<h1>Welcome To Automax</h1>")

@login_required
def home_view(request):
    return render(request, "views/home.html")
