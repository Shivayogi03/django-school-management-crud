from django.db import models

# Create your models here.

class School(models.Model):
    scname=models.CharField()
    scloc=models.CharField()

    def __str__(self):
        return self.scname
    
class Students(models.Model):
    stname=models.CharField()
    stage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.stname
               