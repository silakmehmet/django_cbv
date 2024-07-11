from rest_framework import serializers
from .models import Student, Path


class StudentSerializer(serializers.ModelSerializer):
    born_year = serializers.SerializerMethodField()  # read_only
    path_id = serializers.IntegerField()
    path_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "__all__"

    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age

    def get_path_name(self, obj):
        return obj.path.path_name


class PathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Path
        fields = "__all__"
