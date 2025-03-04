from django.db import models

# Create your models here.


class login(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
    

class Register(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
