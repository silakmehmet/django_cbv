from django.urls import path

from .views import (PathListCreate,
                    PathRetrieveUpdateDestroy,
                    StudentListCreate,
                    StudentRetrieveUpdateDestroy,
                    StudentGAV,
                    StudentDetailGAV,
                    PathGAV,
                    PathDetailGAV
                    )


urlpatterns = [
    # APIView
    # path("paths/", PathListCreate.as_view()),
    # path("path/<int:pk>", PathRetrieveUpdateDestroy.as_view()),

    # path("students/", StudentListCreate.as_view()),
    # path("student/<int:pk>", StudentRetrieveUpdateDestroy.as_view()),

    # Generic API View
    path("paths/", PathGAV.as_view()),
    path("path/<int:pk>", PathDetailGAV.as_view()),
    path("students/", StudentGAV.as_view()),
    path("student/<int:pk>", StudentDetailGAV.as_view()),


]
