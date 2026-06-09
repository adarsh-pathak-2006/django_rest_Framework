from django.db import models

class database(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()

    def __str__(self):
        return self.name
    

class info(models.Model):
    name=models.CharField(max_length=100)
    standard=models.IntegerField()

    def __str__(self):
        return self.name