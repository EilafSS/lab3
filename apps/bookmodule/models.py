from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00) 
    def __str__(self):
        return self.title
