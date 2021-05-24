from django.db import models
from django.db.models.fields import TimeField

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    
def register(name , passwd):
    Users.objects.create(name = name , password = passwd)

def check_user(name, passwd):
    user = Users.objects.filter(name = name) #suppose the name is unique value as email
    if user == None:
        return False
    if user[0].password == passwd: #suppose its the first element,  we should use foor loop to check all elements
        return True
    
    return False
