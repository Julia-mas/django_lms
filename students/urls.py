
from django.urls import path

from .views import StudentCreateView
from .views import StudentDeleteView
from .views import StudentsListView
from .views import StudentUpdateView


app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),                        # R
    path('create/', StudentCreateView.as_view(), name='create'),             # C
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),   # U
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),    # D
]
