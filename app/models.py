from django.db import models

class Students(models.Model):
    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    students_Age = models.IntegerField()
    student_gender = models.CharField(max_length=30)
    student_speciality = models.CharField(max_length=50)
    student_laptop_type = models.CharField(max_length=50)
    students_bio = models.TextField()
    
    
    def __str__(self):
        return self.student_first_name
    
