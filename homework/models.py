from tabnanny import verbose
from django.db import models

class Subject(models.Model):
    name = models.CharField(verbose_name="Предмет", max_length=50)

    def __str__(self):
        return self.name

class Homework(models.Model):
    name = models.CharField(verbose_name="Д/з", max_length=20)
    file = models.FileField(upload_to="files/", blank=True)
    text = models.CharField(verbose_name="Задача", max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=20)
    second_name = models.CharField(verbose_name="Фамилия", max_length=20)
    patronymic = models.CharField(verbose_name="Отчество", max_length=20)
    subject = models.ManyToManyField(Subject, verbose_name="Предмет", max_length=50)

    def __str__(self):
        return self.second_name

