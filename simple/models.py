from django.db import models

class database(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()

    def __str__(self):
        return self.name