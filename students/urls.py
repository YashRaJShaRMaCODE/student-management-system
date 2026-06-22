from django.urls import path

from .views import (
    StudentCreateView,
    StudentListView,
    AverageMarksView,
    PassedStudentsCountView,
)

urlpatterns = [
    path(
        "students/add/",
        StudentCreateView.as_view()
    ),

    path(
        "students/",
        StudentListView.as_view()
    ),

    path(
        "students/average/",
        AverageMarksView.as_view()
    ),

    path(
        "students/count/",
        PassedStudentsCountView.as_view()
    ),
]