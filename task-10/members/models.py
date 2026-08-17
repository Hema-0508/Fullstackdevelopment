from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)


class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task