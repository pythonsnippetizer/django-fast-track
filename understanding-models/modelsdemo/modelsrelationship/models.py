from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

# One to One
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    language = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return str(self.email)

# Many to One relationships
class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        blank=False
    )

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Many to Many relationship
class EmployeePerks(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #many to many 
    compensations = models.ManyToManyField(EmployeePerks)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
