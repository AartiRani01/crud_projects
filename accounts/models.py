from django.db import models
# #from django.contrib.auth.models import User

 # Create your models here.

class User(models.Model):
    # fullname = models.CharField(max_length= 100)
    # email = models.EmailField(unique = True)
    # mobilenumber = models.IntegerField(unique= True)
    # username = models.CharField(max_length= 100, unique= True)
    # password = models.CharField(max_length= 100)
    age = models.IntegerField()
    fullname = models.CharField(max_length= 100)

    def __str__(self):
        return self.fullname
    
# print("user")    