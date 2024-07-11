from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    # API Views
    PathListCreate,
    PathRetrieveUpdateDestroy,
    StudentListCreate,
    StudentRetrieveUpdateDestroy,

    # Generic API Views
    StudentGAV,
    StudentDetailGAV,
    PathGAV,
    PathDetailGAV,

    # Concrete API Views
    StudentListCreateCAV,
    StudentRetrieveUpdateDestroyCAV,
    PathListCreateCAV,
    PathRetrieveUpdateDestroy,

    # Model View Sets
    StudentModelViewSet,
    PathModelViewSet
)

router = DefaultRouter()
router.register("paths", PathModelViewSet)
router.register("students", StudentModelViewSet)

urlpatterns = [
    # APIView
    # path("paths/", PathListCreate.as_view()),
    # path("path/<int:pk>", PathRetrieveUpdateDestroy.as_view()),

    # path("students/", StudentListCreate.as_view()),
    # path("student/<int:pk>", StudentRetrieveUpdateDestroy.as_view()),

    # Generic API View
    # path("paths/", PathGAV.as_view()),
    # path("path/<int:pk>", PathDetailGAV.as_view()),
    # path("students/", StudentGAV.as_view()),
    # path("student/<int:pk>", StudentDetailGAV.as_view()),

    # Concrete API Views
    # path("paths/", PathListCreateCAV.as_view()),
    # path("path/<int:pk>", PathRetrieveUpdateDestroy.as_view()),
    # path("students/", StudentListCreateCAV.as_view()),
    # path("student/<int:pk>", StudentRetrieveUpdateDestroyCAV.as_view()),

    # Model View Sets
    path("", include(router.urls))


]
