from django.db import models

# Create your models here.

class Companies(models.Model):
    Name = models.CharField(max_length=15)
    GST = models.CharField(max_length=16)

    def __str__(self):
        return self.Name

class Products(models.Model):
    Name = models.CharField(max_length=15)
    Company=models.ForeignKey(Companies,on_delete=models.CASCADE)
    Cost=models.IntegerField()

    def __str__(self):
        return self.Name

