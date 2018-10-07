from django.db import models
import uuid
from datetime import datetime

class Cities(models.Model):
    nazwa = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Cities"
    def __str__(self):
        return f'{self.nazwa}'

class Flats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikatowy klucz id')
    miasto = models.ForeignKey('Cities', on_delete=models.SET_NULL, null=True)
    adres = models.CharField(max_length=50)
    cena = models.IntegerField()
    kaucja = models.BooleanField()
    opis = models.TextField(max_length=500)
    zdjecie = models.ImageField(upload_to='media', blank=True)
    FLAT_STATUS = (
        ('d', 'Dostępne'),
        ('n', 'Niedostępne')
    )
    status = models.CharField(
        max_length=1,
        choices=FLAT_STATUS,
        blank=True,
        default='m',
        help_text='Dostępność mieszkania',
    )

    class Meta:
        verbose_name_plural = "Flats"

    def __str__(self):
        return f'{self.miasto}, {self.adres}'

class Reservations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikatowy klucz id')
    mieszkanie = models.ForeignKey('Flats', on_delete=models.SET_NULL, null=True)
    telefon = models.CharField(max_length=15, help_text='Telefon kontaktowy', null=True)
    data_wynajecia = models.DateField(null=True, blank=True)
    data_oddania = models.DateField (null=True, blank=True)

    class Meta:
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f'{self.id}, {self.mieszkanie}, {self.data_wynajecia}, {self.data_oddania}'
