
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
from django.urls import path, include

from core.views import index
from groups.views import get_groups, create_groups, index_group, update_group
from teachers.views import get_teachers, create_teacher, update_teacher, index_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('students/', include('students.urls')),
    path('t/', index_teachers, name='index_teachers'),
    path('teachers/create/', create_teacher, name='create_teacher'),
    path('teachers/', get_teachers, name='get_teachers'),
    path('teachers/update/<int:pk>/', update_teacher, name='update_teacher'),
    path('g/', index_group, name='index_teachers'),
    path('groups/', get_groups, name='get_groups'),
    path('groups/create/', create_groups, name='create_groups'),
    path('groups/update/<int:pk>/', update_group, name='update_group'),
]
