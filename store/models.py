from django.db import models
from django.utils import timezone

CATEGORY_CHOICES = [
    ('diapers', 'Diapers'),
    ('wipes', 'Wipes'),
    ('toys', 'Toys'),
    ('clothes', 'Clothes'),
    ('pampers', 'Pampers'),
    ('Girls','girls'),
    ('Boys','boys'),
    ('Soaps', 'Soaps'),
    ('stroller', 'Stroller'),
    ('bottle', 'Bottle'),
    ('all', 'All Products'),
    ('offer', 'Offers'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='all')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)


    def __str__(self):
        return self.name
    

