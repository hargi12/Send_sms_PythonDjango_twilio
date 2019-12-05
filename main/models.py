from django.db import models

# Create your models here.
class patient_info(models.Model):
    id =models.AutoField(primary_key=True)
    names = models.CharField(max_length=255, unique=True)
    telephone = models.CharField(max_length=10, null=True)
    supporter_name = models.CharField(max_length=255, null=True)
    supporter_telephone = models.CharField(max_length=10, null=True)


class Treatment(models.Model):
    patient = models.OneToOneField(patient_info, on_delete=models.CASCADE)
    started_treatment = models.DateTimeField()
    first_refill = models.DateTimeField()
    second_refill = models.DateTimeField()

    

#class sms_messages(models.Model):
