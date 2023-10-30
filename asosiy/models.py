from django.db import models


class Student(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    kurs = models.SmallIntegerField()
    student_raqam = models.IntegerField(unique=True)

    def __str__(self):
        return self.ism


class Malumot(models.Model):
    sarlavha = models.CharField(max_length=255)
    sana = models.DateField()
    malumot = models.CharField(max_length=255, blank=True)
    bajatilgan = models.BooleanField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
