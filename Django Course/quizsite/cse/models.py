from django.db import models

# Create your models here.
class ExcelFile(models.Model):
    Qn_No=models.IntegerField()
    Question=models.CharField(max_length=1000)
    Option_A=models.CharField(max_length=1000)
    Option_B=models.CharField(max_length=1000)
    Option_C=models.CharField(max_length=1000)
    Option_D=models.CharField(max_length=1000)
    Answer=models.CharField(max_length=1000)
