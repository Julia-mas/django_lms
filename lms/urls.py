
"""lms URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from groups.views import get_groups
from students.views import index, get_students, create_student, update_student
from teachers.views import get_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('students/', get_students, name='get_students'),               #R
    path('students/create/', create_student, name='create_student'), #C
    path('teachers/', get_teachers, name='get_teachers'),
    path('students/update/<int:pk>/', update_student, name='update_student'),
    path('groups/', get_groups, name='get_groups')
]
