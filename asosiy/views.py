from django.shortcuts import render
from .models import *
# Create your views here.
def home(requets):
    return render(requets,"home.html")




def hamma_studentlar(request):
    content = {
        "studentlar": Student.objects.all()
    }
    return render(request, "hamma_studentlar.html", content)
