from django.db import models

# Create your models here.


class Animal_info(models.Model):
    name=models.CharField(max_length=50)
    desease_type=models.CharField(max_length=100)
    desease_update= models.CharField(max_length=40)
    age=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name


