from django.db import models

# Create your models here.
class Student(models.Model):
    STUDENT_STATUS_PENDING = 'P'
    STUDENT_STATUS_ENROLLED = 'E'
    STUDENT_STATUS_GRADUATED = 'G'
    STUDENT_STATUS_REJECTED = 'R'

    '''
        A list of tuples, where:
            The 1st value in each tuple is the stored value in the database (i.e, 'P', 'E')
            The 2nd value is the human-readable label displayed in forms or admin panels.
    '''
    STUDENT_STATUS = [
        (STUDENT_STATUS_PENDING, 'Pending'),
        (STUDENT_STATUS_ENROLLED, 'Enrolled'),
        (STUDENT_STATUS_GRADUATED, 'Graduated'),
        (STUDENT_STATUS_REJECTED, 'Rejected'),
    ]

    MALE = 'M'
    FEMALE = 'F'

    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    SECTION = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('D', 'D'),
    ]

    GRADE = [(i, str(i)) for i in range(1,13)]

    full_name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, blank=False)
    address = models.CharField(max_length=255, blank=False)
    
    grade = models.IntegerField(choices=GRADE, blank=False)
    section = models.CharField(max_length=1, choices=SECTION, blank=False)
    status = models.CharField(max_length=1, choices=STUDENT_STATUS, default=STUDENT_STATUS_PENDING)

class Person(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    hobbies = models.JSONField(default=list)