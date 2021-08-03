from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    education = models.CharField(max_length=254)
    graduation = models.DecimalField(max_digits=4, decimal_places=0)
    specialisation = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
