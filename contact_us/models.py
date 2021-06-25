from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    site=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    # Country=models.CharField(max_length=100)
    text=models.TextField()
    # state=models.CharField(max_length=100)
    # zip_code=models.IntegerField()
    phone=models.IntegerField()
    def __str__(self):
        return self.name