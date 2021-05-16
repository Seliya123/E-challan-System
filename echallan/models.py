from django.db import models

# Create your models here.


class challans(models.Model):

    names = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    phonenumber = models.IntegerField(default=None, blank=True, null=True)
    licensenumber = models.CharField(max_length = 200)
    vehiclenumber = models.CharField(max_length = 200)
    vehicletype = models.CharField(max_length=200, default=None, blank=True, null=True)
    creator = models.CharField(max_length = 200)

    def __str__(self):
        return self.licensenumber

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title        