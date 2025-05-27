from django.db import models
#database part
# Create your models here.
class Tasks(models.Model):
    tasktitle = models.CharField(max_length=100)
    taskdescription = models.TextField()
    deadline = models.DateField()
    completed = models.BooleanField(default = False)


    def __str__(self):
        return self.title
