from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def home(requets):
    return render(requets, "home.html")


def hamma_studentlar(request):
    content = {
        "studentlar": Student.objects.all()
    }
    return render(request, "hamma_studentlar.html", content)


def hamma_rejalar(request):
    if request.method == 'POST':
        forma = RejaForm(request.POST)
        if forma.is_valid():
            forma.save()

    content = {
        "rejalar": Malumot.objects.all(),
        "forma": RejaForm()
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


def reja_ochir(request, son):
    Malumot.objects.get(id=son).delete()
    return redirect("/hamma_rejalar/")


def yosh_katta_student(request):
    content = {
        "studentlar": Student.objects.filter(yosh__gt=20)
    }
    return render(request, "yosh_katta_student.html", content)

