from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
import datetime


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    start_date = models.DateTimeField('date joined')
    end_date = models.DateTimeField('date exited')
    def __str__(self):
        return self.first_name + " " + self.last_name
#    def was_publised_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Hours(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    week1 = models.IntegerField(default=0)
    week2 = models.IntegerField(default=0)
    week3 = models.IntegerField(default=0)
    week4 = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    def __str__(self):
        return self.emplyee
