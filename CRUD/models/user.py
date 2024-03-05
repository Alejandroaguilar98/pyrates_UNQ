from django.db import models

class User(models.Model):
    complete_name=models.CharField(max_length=30,blank=False,null=False)
    username=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False,unique=True)
    password=models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return f'{self.complete_name}'