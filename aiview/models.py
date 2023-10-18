from django.db import models

# Create your models here.
class OpenapiKey(models.Model):
    key = models.CharField('apikey', max_length=256,unique=True)
    #创建时间
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.key

class User(models.Model):
    '''用户表'''
    name = models.CharField(max_length=128,unique=True,)
    c_time = models.DateTimeField(auto_now_add=True)
    weichatopenid = models.CharField(max_length=128,unique=True,null=True)
    def __str__(self):
        return self.name
