from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins

from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer


class PathListCreate(APIView):

    def get(self, request):
        list_all = Path.objects.all()
        serializer = PathSerializer(list_all, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PathSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"detail": "Path başarılı bir şekilde kaydedildi"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentListCreate(APIView):

    def get(self, request):
        list_all = Student.objects.all()
        serializer = StudentSerializer(list_all, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"detail": "Öğrenci başarılı bir şekilde kaydedildi"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PathRetrieveUpdateDestroy(APIView):

    def get(self, request, pk):
        one_path = get_object_or_404(Path, id=pk)
        serializer = PathSerializer(one_path)
        return Response(serializer.data)

    def put(self, request, pk):
        one_path = get_object_or_404(Path, id=pk)
        serializer = PathSerializer(instance=one_path, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"detail": "Path başarılı bir şekilde güncellendi"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        one_path = get_object_or_404(Path, id=pk)
        one_path.delete()
        message = {"detail": "Path başarılı bir şekilde silindi"}
        return Response(message)


class StudentRetrieveUpdateDestroy(APIView):

    def get(self, request, pk):
        one_student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(one_student)
        return Response(serializer.data)

    def put(self, request, pk):
        one_student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=one_student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"detail": "Path başarılı bir şekilde güncellendi"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        one_student = get_object_or_404(Student, id=pk)
        one_student.delete()
        message = {"detail": "Öğrenci başarılı bir şekilde silindi"}
        return Response(message)


class PathGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PathDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
