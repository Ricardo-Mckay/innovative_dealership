from django.db import models

# Create your models here.


class Car(models.Model):
    cartitle = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='all_media/images/')
    price = models.CharField(max_length=9)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.cartitle