from django.db import models

# Create your models here.


class Operation(models.Model):
  slackusername = models.CharField(max_length=30, null =True)
  operation_type = models.CharField(max_length=100, null=True)
  x = models.IntegerField(null=True)
  y = models.IntegerField(null=True)
 
  
  

