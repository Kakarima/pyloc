from django.db import models

GEARS_CHOICES = (
    ('M', 'Manuelle'),
    ('A', 'Automatique'),
    ('MA', 'Manuelle ou automatique')
)
ENERGY_CHOICES = (
    ('G', 'Essence'),
    ('D', 'Diesel'),
    ('GD', 'Essence ou diesel'),
    ('E', 'Electrique'),
    ('H', 'Hybride')
)


class Category(models.Model):
    """ This class is use to model the different categories of vehicle that are provided for rental"""
    code = models.CharField(max_length=1)
    label = models.CharField(max_length=30)
    sample = models.CharField(max_length=30)
    image = models.CharField(max_length=80)
    description = models.TextField(null=True)
    nb_seats = models.IntegerField(default=5)
    nb_luggage = models.IntegerField(default=0)
    nb_doors = models.IntegerField(default=5)
    gear = models.CharField(max_length=2, choices=GEARS_CHOICES)
    energy = models.CharField(max_length=2, choices=ENERGY_CHOICES)
    climate_control = models.BooleanField(default=True)
    winter = models.BooleanField(default=False)
    pre_pay = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    equivalent = models.TextField(null=True)

    class Meta:
        verbose_name = 'Categorie'
        ordering = ['code']

    def __str__(self):
        return '{} - {}'.format(self.code, self.label)


class Agency(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    postal_code = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'Agence de location'
        ordering = ['name']

    def __str__(self):
        return '{} - {}'.format(self.name, self.city)
