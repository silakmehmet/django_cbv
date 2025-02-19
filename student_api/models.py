from django.db import models


class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"


class Student(models.Model):
    path = models.ForeignKey(
        Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name
