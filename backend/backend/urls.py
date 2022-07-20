from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', views.student_list),
    path('api/students/([0-9])/', views.students_detail)
]
