from django.db import models
#from django.contrib.auth.models import User


DEPARTMENT1 = '1'
DEPARTMENT2 = '2'


class Task(models.Model):
    department = models.CharField(choices=((DEPARTMENT1, 'DEPARTMENT 1'), (DEPARTMENT2, 'DEPARTMENT 2')),   max_length=16)
    task = models.CharField(max_length=250)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    status = models.CharField(max_length=16,choices=(
        ('0', 'Pending'),
        ('1', 'OnProgress'),
        ('2', 'Completed')
    ))

    def __str__(self):
        return 'Task: %s' % self.pk


class User(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=16,choices=((DEPARTMENT1, 'DEPARTMENT 1'), (DEPARTMENT2, 'DEPARTMENT 2')))

    def __str__(self):
        return self.name
