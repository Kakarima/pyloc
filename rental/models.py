from django.contrib.auth.models import User
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


class Category(models.Model):
    code = models.CharField(max_length=1, unique=True)
    label = models.CharField(max_length=30)
    sample = models.CharField(max_length=30)
    #image = models.ImageField(upload_to='rental/photos', null=True, max_length=300)
    image = models.CharField(max_length=50)
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
        return '{} - {} - {} - {}'.format(self.id, self.code, self.label, self.sample)


class Feature(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            unique=True)
    code = models.CharField(max_length=10,
                            null=False,
                            unique=True)

    class Meta:
        verbose_name = "Fonctionnalités"
        ordering = ['name']

    def __str__(self):
        return '({}) {}'.format(self.code, self.name)


class Vehicle(models.Model):
    brand = models.CharField(max_length=100, null=True)
    manufacturer_name = models.CharField(max_length=32)
    registration = models.CharField(max_length=10, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    agence = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)

    engine_serial_number = models.CharField(max_length=255, null=True, unique=True)
    active = models.BooleanField(null=False, default=True)
    features = models.ManyToManyField(Feature)
    motorisation = models.CharField(max_length=100, null=True)
    code_motorisation = models.CharField(max_length=100, null=True)
    couple = models.CharField(max_length=100, null=True)
    puissance = models.CharField(max_length=100, null=True)
    consommation = models.FloatField(null=True, default=0)
    co2 = models.IntegerField(null=True, default=0)
    cx = models.CharField(max_length=100, null=True)
    poids = models.CharField(max_length=100, null=True)
    kilometrage = models.IntegerField(null=True, default=0)
    boiteVitesse = models.CharField(max_length=100, null=True)
    pneuDimension = models.CharField(max_length=100, null=True)
    type_traction = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Véhicule'
        ordering = ['brand', 'manufacturer_name', 'registration']

    def __str__(self):
        return '{} - {} - {}'.format(self.brand, self.manufacturer_name, self.registration)


class DrivingLicenceScan(models.Model):
    path = models.FilePathField()
    number = models.CharField(max_length=12, null=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    postal_code = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=True)

    licence_scan = models.ImageField(upload_to='customer-licences', blank=True)
    licence_number = models.CharField(max_length=12, null=True)

    receiveAdds = models.BooleanField(default=True)
    creditCardNumber = models.CharField(max_length=16, null=True)
    creditCardValidity = models.CharField(max_length=4, null=True)
    email = models.EmailField(max_length=255, null=True)


class Contract(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agency, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    scheduled_date_end = models.DateTimeField()
    base_price = models.FloatField()
    vat_rate = models.FloatField()
    vat = models.FloatField()
    total_price = models.FloatField()
    remaining_price = models.FloatField()
    fully_paid = models.BooleanField(default=False)
