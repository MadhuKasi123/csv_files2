from django.db import models

# Create your models here.

class Business_Data_Collection(models.Model):
    Series_reference=models.CharField(max_length=100)
    Period=models.DecimalField(max_digits=15,decimal_places=3)
    data_value=models.CharField(max_length=100,null=True)
    suppresed=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100)
    magnitude=models.IntegerField()
    subject=models.CharField(max_length=100,null=True)
    group=models.CharField(max_length=100,null=True)
    series_title_1=models.CharField(max_length=100,null=True)
    series_title_2=models.CharField(max_length=100,null=True)
    series_title_3=models.CharField(max_length=100,null=True)
    series_title_4=models.CharField(max_length=100,null=True)
    series_title_5=models.CharField(max_length=100,null=True)

