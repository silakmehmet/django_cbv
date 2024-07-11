from django.urls import path

from .views import PathListCreate, PathRetrieveUpdateDestroy, StudentListCreate, StudentRetrieveUpdateDestroy


urlpatterns = [
    # Paths
    path("paths/", PathListCreate.as_view()),
    path("path/<int:pk>", PathRetrieveUpdateDestroy.as_view()),
    # Students
    path("students/", StudentListCreate.as_view()),
    path("student/<int:pk>", StudentRetrieveUpdateDestroy.as_view()),

]
