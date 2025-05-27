from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.TextField()
    courses = models.TextField()
    achievements = models.TextField()


    def __str__(self):
        return self.name
