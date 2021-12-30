from django.db import models

# Create your models here.
class Record(models.Model):
    owner = models.CharField(max_length=30)
    brand = models.CharField(max_length=20)
    chasi_number = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=20)
    registration_date = models.DateField()
    engine_no = models.CharField(max_length=20)
    vehicle_class = models.CharField(max_length=10)
    fuel = models.CharField(max_length=10)
    #mfg = models.CharField(max_length=20)


    entry = models.DateTimeField(null=False,blank=False)
    exit = models.DateTimeField(null=False,blank=False)
    entry_pic = models.TextField()
    exit_pic = models.TextField()