from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
