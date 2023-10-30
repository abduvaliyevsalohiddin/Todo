from django.contrib import admin
from .models import *


@admin.register(Malumot)
class MalumotAdmin(admin.ModelAdmin):
    list_display = ["id", "sarlavha", "sana", "malumot", "bajatilgan", "student"]
    list_filter = ["bajatilgan"]
    search_fields = ["sarlavha"]
    search_help_text = "Sarlavha ustunlari bo'yicha qidiring"
    list_display_links = ["sarlavha"]
    autocomplete_fields = ["student"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "yosh", "kurs", "student_raqam"]
    list_filter = ["kurs"]
    search_fields = ["ism"]
    search_help_text = "Ism ustunlari bo'yicha qidiring"
    list_display_links = ["ism"]

# admin.site.register(Student)
# admin.site.register(Malumot)
