from django.db import models

# Create your models here.
# class Destination:
#     id :int
#     name :str
#     img :str
#     desc : str
#     price : int

class Destination(models.Model):
    
    name = models.CharField( max_length=100)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()
    offer =models.BooleanField(default= False)
    price = models.IntegerField()