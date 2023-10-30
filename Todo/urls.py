
from django.contrib import admin
from django.urls import path
from asosiy.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('hamma_studentlar/', hamma_studentlar),
    path('hamma_rejalar/', hamma_rejalar),
    path('bajarilmagan_reja/', bajarilmagan_reja),
    path('student_kurs/', student_kurs),
]
