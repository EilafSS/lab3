from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)

    def __str__(self):
        return self.title

class Address(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city
    
class Card(models.Model):
    card_number = models.IntegerField()
    def __str__(self):
        return f"Card #{self.card_number}"
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()
    def __str__(self):
        return f"{self.title} ({self.code})"
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null = True)
    courses = models.ManyToManyField(Course, related_name="students", blank=True)
    def __str__(self):
        return self.name