from .models import Subject, Homework, Teacher
from rest_framework import viewsets, permissions
from .serializers import SubjectSerializer, HomeworkSerializer, TeacherSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = SubjectSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = HomeworkSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = TeacherSerializer