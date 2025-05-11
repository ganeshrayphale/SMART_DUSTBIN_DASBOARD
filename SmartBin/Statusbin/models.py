from django.db import models

# Create your models here.
from django.db import models

class Bin(models.Model):
    location = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    waste_level = models.PositiveIntegerField()  # 0 to 100
    status = models.CharField(max_length=10, choices=[
        ('Empty', 'Empty'),
        ('Half', 'Half'),
        ('Full', 'Full')
    ])

    def __str__(self):
        return f"{self.location} - {self.area}"
