from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone = models.DecimalField(max_digits=20, decimal_places=0)
    email = models.CharField(max_length=50)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name