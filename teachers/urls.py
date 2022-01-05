from django.urls import path

from .views import TeacherCreateView
from .views import TeacherListView
from .views import TeacherUpdateView
from .views import TeacherDeleteView

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TeacherDeleteView.as_view(), name='delete')
]
