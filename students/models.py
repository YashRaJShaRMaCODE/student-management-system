from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    marks_obtained = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name