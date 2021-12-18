
from django.urls import path

from .views import create_student
from .views import delete_student
from .views import get_students
from .views import update_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),                        # R
    path('create/', create_student, name='create'),             # C
    path('update/<int:pk>/', update_student, name='update'),    # U
    path('delete/<int:pk>/', delete_student, name='delete'),    # D
]
