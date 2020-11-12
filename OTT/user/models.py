from django.db import models



# Create your models here.
class Orders(models.Model):
    person = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120)
    productid = models.CharField(max_length=120),
    choice = (
        ("ordered", "ordered"),
        ("cancelled", "cancelled")
    )
    status=models.CharField(max_length=20,choices=choice,default="ordered")
    def __str__(self):
        return self.person
