from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at= models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.ForeignKey(Dojo , related_name='dojo' , on_delete=models.CASCADE)
    created_at= models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)