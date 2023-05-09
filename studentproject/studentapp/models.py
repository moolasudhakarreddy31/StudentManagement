from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    dob = models.DateField()
    marks_percentage = models.IntegerField()
    class_group = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name