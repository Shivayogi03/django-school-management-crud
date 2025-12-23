from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    scname=models.CharField()
    scloc=models.CharField()

    def __str__(self):
        return self.scname
    
    def get_absolute_urls(self):
        return reverse('schoo_detail',kwargs={'pk':self.pk})
    
class Students(models.Model):
    stname=models.CharField()
    stage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='student')

    def __str__(self):
        return self.stname
               