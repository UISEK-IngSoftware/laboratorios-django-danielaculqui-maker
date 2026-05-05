from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=50, null=False)
    height = models.FloatField()
    weight = models.FloatField()
    
    def __str__(self):
        return self.name