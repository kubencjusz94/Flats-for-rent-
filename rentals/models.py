from django.db import models
import uuid
from django.db import IntegrityError
from django.db.models import Q
from datetime import datetime
from django.urls import reverse
from django.core.validators import RegexValidator

class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'{self.name}'

class Flat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=50)
    prize = models.IntegerField()
    deposit = models.BooleanField()
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='media', blank=True)
    FLAT_STATUS = (
        ('a', 'available'),
        ('u', 'unavailable')
    )
    status = models.CharField(
        max_length=1,
        choices=FLAT_STATUS,
        blank=True,
        default='m',
    )

    def get_absolute_url(self):
        return reverse('flat_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.city}, {self.adress}'

class Reservations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    flat = models.ForeignKey('Flat', on_delete=models.SET_NULL, null=True)
    lastname = models.CharField(max_length=30, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999 999 999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    date_of_rent = models.DateField(null=True, blank=True)
    date_of_surrender = models.DateField (null=True, blank=True)

    class Meta:
        verbose_name_plural = "Reservations"

    def save(self, *args, **kwargs):
        try:
            Reservations.objects.get(Q(flat = self.flat) & (Q(date_of_rent__range = [self.date_of_rent, self.date_of_surrender]) | Q(date_of_surrender__range = [self.date_of_rent, self.date_of_surrender]) | Q(date_of_rent__lt = self.date_of_rent, date_of_surrender__gt = self.date_of_surrender)))
            raise IntegrityError('That appartment is busy at this time')
        except Reservations.DoesNotExist:
            super(Reservations,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.id}, {self.flat}, {self.date_of_surrender}, {self.date_of_surrender}'
