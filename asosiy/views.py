from django.shortcuts import render
from .models import *


# Create your views here.
def home(requets):
    return render(requets, "home.html")


def hamma_studentlar(request):
    content = {
        "studentlar": Student.objects.all()
    }
    return render(request, "hamma_studentlar.html", content)


def hamma_rejalar(request):
    content = {
        "rejalar": Malumot.objects.all()
    }
    return render(request, "hamma_rejalar.html", content)


def bajarilmagan_reja(request):
    content = {
        "rejalar": Malumot.objects.filter(bajatilgan=False)
    }
    return render(request, "bajarilmagan_reja.html", content)


def student_kurs(request):
    content = {
        "studentlar": Student.objects.filter(kurs__gte=3)
    }
    return render(request, "student_kurs.html", content)
