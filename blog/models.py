from django.db import models

class blog(models.Model):
    blog= models.CharField(max_length=50000)
    date= models.DateTimeField() 



# Create your models here.
