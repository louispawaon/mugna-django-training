from django.db import models

class Classification (models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Book (models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    classification = models.ForeignKey('Classification', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Author (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
