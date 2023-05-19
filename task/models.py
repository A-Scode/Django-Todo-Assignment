from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    id = models.UUIDField( default= uuid.uuid4 , primary_key=True , null=False)
    name = models.CharField(max_length=200 , null=False , blank=False)
    description = models.TextField(null=True , blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.UUIDField( default= uuid.uuid4 , primary_key=True , null=False)
    task_name = models.CharField(max_length=200 , null=False , blank=False)
    description = models.TextField(null=True , blank=True)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(Category , on_delete=models.CASCADE)

    def __str__(self):
        return self.name